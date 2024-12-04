from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Cookie(db.Model):
    __tablename__="Cookie"
    
    id = db.Column(db.Integer, primary_key = True)
    cookie_name = db.Column(db.Text)
    score = db.Column(db.Integer)
    
    def __init__(self, cookie_name, score):
        self.cookie_name = cookie_name
        self.score = score
        
    def __repr__(self):
        return f"ID: {self.id} cookie_name: {self.cookie_name} score: {self.score}"
    
    