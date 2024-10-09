from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birthDate = db.Column(db.Date, nullable=False)

    posts = db.relationship('Post', backref='user', lazy=True)

    @property
    def age(self):
        today = datetime.today()
        age = today.year - self.birthDate.year 
        
        if (today.month, today.day) < (self.birthDate.month, self.birthDate.day):
            age -=1
            
        return age
