from app import db

# SQLAlchemy ORM models

class Unit(db.Model):
    __tablename__ = 'units'
    query = db.session.query_property()
    uuid = db.Column(db.String(30), primary_key=True)
    updateTime = db.Column(db.DateTime, nullable=False, unique=False)
    name = db.Column(db.String(50), nullable=False, unique=False)
    ntype = db.Column(db.String(10), nullable=False, unique=False)
    parentId = db.Column(db.String(30), nullable=True, unique=False)
    price = db.Column(db.Integer, nullable=False, unique=False)
    children = db.Column(db.String(100), nullable=False, unique=False)
    def to_json(self):
        return {
            'uuid': self.uuid,
            'updateTime': self.updateTime,
            'name': self.name,
            'ntype': self.ntype,
            'parentId': self.parentId,
            'price': self.price,
            'children' : self.children
        }