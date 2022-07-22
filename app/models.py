from app import db

# SQLAlchemy ORM models

class Unit(db.Model):
    __tablename__ = 'units'
    query = db.session.query_property()
    uuid = db.Column(db.String(50), primary_key=True)
    updateTime = db.Column(db.DateTime, nullable=False, unique=False)
    name = db.Column(db.String(50), nullable=False, unique=False)
    ntype = db.Column(db.Integer, nullable=False, unique=False)
    parentId = db.Column(db.String(50), nullable=True, unique=False)
    price = db.Column(db.Integer, nullable=True, unique=False)
    def to_json(self):
        return {
            'uuid': self.uuid,
            'date': self.updateTime,
            'name': self.name,
            'type': self.ntype,
            'parentId': self.parentId,
            'price': self.price,
        }

class History(db.Model):
    __tablename__ = 'history'
    query = db.session.query_property()
    uuid = db.Column(db.String(50), db.ForeignKey(Unit.uuid), primary_key=True)
    updateTime = db.Column(db.DateTime, primary_key=True)
    price = db.Column(db.Integer, nullable=False, primary_key=True, default=-1)
    def to_json(self):
        return {
            'uuid': self.uuid,
            'date': self.updateTime,
            'price': self.price
        }