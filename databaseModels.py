from flask_sqlalchemy import SQLAlchemy


db:SQLAlchemy = SQLAlchemy()

class Cookie(db.Model):
    __tablename__="Cookie"
    
    id = db.Column(db.Integer, primary_key = True)
    cookie_name = db.Column(db.Text)
    score = db.Column(db.Integer)
    baker_name = db.Column(db.Text)
    year = db.Column(db.Integer)
    image = db.Column(db.Text)
    # creative_points = db.Column(db.Integer)
    # presentation_points = db.Column(db.Integer)

    def __init__(self, cookie_name:str, year:int, image:str):
        self.cookie_name = cookie_name
        self.score = 0
        # self.baker_id = baker_id
        self.year = year
        self.image = image
        
        
    def __repr__(self):
        return f"ID: {self.id} cookie_name: {self.cookie_name} score: {self.score}"
    
# class Baker(db.Model):
#     __tablename__ = "Baker"
    
#     id = db.Column(db.Integer, primary_key = True)
#     baker_name = db.Column(db.Text)
#     hasVoted = db.Column(db.Boolean)
#     cookie_id = db.Column(db.Integer, db.ForeignKey('Cookie.id'))