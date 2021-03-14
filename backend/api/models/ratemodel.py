import datetime
from flask_sqlalchemy import SQLAlchemy

# initialize our db
db = SQLAlchemy()

class RateModel(db.Model):
    """Storage Rate Model"""
    
    # table name
    __tablename__ = 'rates'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    market = db.Column(db.String(128), nullable=False)
    size = db.Column(db.String(128), nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    features = db.Column(db.String(128), nullable=False)
    avail = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    
    # class constructor
    def __init__(self, data):
        """Class constructor"""
        self.name = data.get('name')
        self.market = data.get('market')
        self.size = data.get('size')
        self.rate = data.get('rate')
        self.features = data.get('features')
        self.avail = data.get('avail')
        self.created_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    # def update(self, data): Don't need this

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_rates():
        return RateModel.query.all()
    
    # Might need to fix this method call
    @staticmethod
    def get_one_size(size):
        return RateModel.query.get(size)

    def __repr(self):
        return '<id {}>'.format(self.id)