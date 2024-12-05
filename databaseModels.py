from flask_sqlalchemy import SQLAlchemy


db:SQLAlchemy = SQLAlchemy()

class Cookie(db.Model):
    __tablename__="Cookie"
    
    id = db.Column(db.Integer, primary_key = True)
    cookie_name = db.Column(db.Text)
    score = db.Column(db.Integer)
    baker_id = db.Column(db.Integer, db.ForeignKey('Baker.id'))
    
    def __init__(self, cookie_name, score):
        self.cookie_name = cookie_name
        self.score = score
        
    def __repr__(self):
        return f"ID: {self.id} cookie_name: {self.cookie_name} score: {self.score}"
    
class Baker(db.Model):
    __tablename__ = "Baker"
    
    id = db.Column(db.Integer, primary_key = True)
    baker_name = db.Column(db.Text)
    hasVoted = db.Column(db.Boolean)
    cookie_id = db.Column(db.Integer, db.ForeignKey('Cookie.id'))