from .extensions import celery, db
from .models import Unit, History
import os
from enum import Enum, auto
from datetime import datetime, timedelta
import re

class Type(Enum):
    OFFER = auto()
    CATEGORY = auto()
    INVALID = auto()
UUID_TEMPLATE = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)
# Validate input data
def validateData(data):
    type = Type.INVALID
    try:
        if(UUID_TEMPLATE.match(data['uuid'])):
            if(data['type'] == 'OFFER'):
                if(data['price'] is not None and data['price'] >= 0):
                    type = Type.OFFER
            elif(data['type'] == 'CATEGORY'):
                if(data['price'] is None):
                    type = Type.CATEGORY
    except KeyError:
        pass
    return type

# Format response data
def formatData(data):
    data['type'] = 'OFFER' if data['type'] == Type.OFFER.value else 'CATEGORY'
    return data

# Calculate average price in category
def getAverageCategory(uuid):
        childrens = [unit.to_json() for unit in Unit.query.filter_by(parentId=uuid)]
        if(len(childrens)):
            return sum([children['price'] \
                for children in childrens if children['price'] is not None])/len(childrens)
        else:
            return None

# Import node celery task
@celery.task
def importNode(data):
    result = []
    for entry in data:
        type = validateData(entry)
        if(type is Type.INVALID):
            return None
        # Define unit object
        time = datetime.now()
        if(entry['price'] is None):
            entry['price'] = -1
        new_unit = Unit(
            updateTime=time,
            uuid=entry['uuid'],
            name=entry['name'],
            ntype=type.value,
            parentId=entry['parentId'],
            price=entry['price'],
        )
        # Define history object
        historyEntry = History(
            uuid=entry['uuid'],
            updateTime=time,
            price=entry['price']
        )
        db.session.add(historyEntry)
        result.append(formatData(new_unit.to_json()))
        exists = Unit.query.get(entry['uuid'])
        # Update existing entry
        if(exists is not None):
            data = new_unit.to_json()
            data['updateTime'] = data['date']
            del data['date']
            data['ntype'] = data['type']
            del data['type']
            Unit.query.filter_by(uuid=exists.uuid).update(data)
        # Add new entry
        else:
            db.session.add(new_unit)
        # Update parent history
        if(type is Type.OFFER):
            parent = Unit.query.get(entry['parentId'])
            if(entry['parentId'] is not None and parent is not None):
                parent.updateTime = time
                price = i = 0
                for res in result:
                    if(res['uuid'] == entry['parentId']):
                        i+=1
                        price+=res['price']
                parent.price = getAverageCategory(parent.uuid)
                #parent.price += price/i
                parentHistoryEntry = History(
                    uuid=parent.uuid,
                    updateTime=time,
                    price=parent.price
                )
                db.session.add(parentHistoryEntry)
    # Commit changes 
    db.session.commit()
    return result

# Delete unit celery task
@celery.task
def deleteNode(uuid):
    unit = Unit.query.get(uuid)
    if(not UUID_TEMPLATE.match(uuid)):
        return 400
    elif(unit is None):
        return 404
    # Delete unit and it's history and 
    # Get all children units and delete it and it's history
    childrens = Unit.query.filter_by(parentId=unit.uuid)
    for entry in childrens:
        db.session.delete(entry)
        history = History.query.filter_by(uuid=entry.uuid)
        for entry in history:
            db.session.delete(entry)
    history = History.query.filter_by(uuid=unit.uuid)
    for entry in history:
        db.session.delete(entry)
    db.session.delete(unit)
    db.session.commit()
    return 200

# Get unit celery task
@celery.task
def getNode(uuid):
    entry = Unit.query.get(uuid)
    if(not UUID_TEMPLATE.match(uuid)):
        return {"code": 400}
    elif(entry is None):
        return {"code": 404}
    entry = entry.to_json()
    # Get children units if it's category
    if(entry['type'] == Type.CATEGORY.value):
        childrens = [formatData(unit.to_json()) \
            for unit in Unit.query.filter_by(parentId=entry['uuid'])]
        entry['children'] = childrens
    else:
        entry['children'] = None
    entry = formatData(entry)
    entry['code'] = 200
    return entry

# Get sales updated in hour celery task
@celery.task
def getSales(time):
    try:
        now = datetime.fromisoformat(time)
    except ValueError:
        return None
    # Find all entries updated an hour before given date
    result = [formatData(unit.to_json()) for unit in Unit.query \
        .filter(Unit.updateTime <= now) \
        .filter(Unit.updateTime >= now - timedelta(hours=1))]
    return result

# Get unit statistics by given time celery task
@celery.task
def getNodeStatistics(uuid, dateStart, dateEnd):
    try:
        dateStart = datetime.fromisoformat(dateStart)
        dateEnd = datetime.fromisoformat(dateEnd)
    except ValueError:
        return {"code": 400}
    data = Unit.query.get(uuid)
    if(data is None):
        return {"code": 404}
    # Find price history in database updated between given dates
    unit = formatData(data.to_json())
    history = History.query.filter(History.uuid == uuid)\
        .filter(History.updateTime >= dateStart)\
        .filter(History.updateTime < dateEnd)
    result = []
    for entry in history:
        resultEntry = unit.copy()
        resultEntry['date'] = entry.updateTime
        resultEntry['price'] = entry.price
        result.append(resultEntry)
    return {"result": result, "code": 200}
        

