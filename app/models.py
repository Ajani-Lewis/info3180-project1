from . import db

class Property(db.Model):
    
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    num_bed = db.Column(db.Integer)
    num_bath = db.Column(db.Integer)
    prop_location = db.Column(db.String(255))
    price = db.Column(db.Float)
    prop_type = db.Column(db.String(50))
    desc = db.Column(db.String(255))
    photo = db.Column(db.String(255))

    def __init__(self,title,num_bed,num_bath,prop_location,price,prop_type,photo,desc):
        self.title = title
        self.num_bed = num_bed
        self.num_bath = num_bath
        self.prop_location = prop_location
        self.price = price
        self.prop_type = prop_type
        self.photo = photo
        self.desc = desc

