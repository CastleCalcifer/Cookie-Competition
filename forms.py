from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, RadioField

class VotingForm(FlaskForm):
    cookie1 = SelectField(id="1", choices=[("---"), ("1st"), ("2nd"), ("3rd"), ("4th")])
    cookie2 = SelectField(id="2",choices=[("---"), ("1st"), ("2nd"), ("3rd"), ("4th")])
    cookie3 = SelectField(id="3",choices=[("---"), ("1st"), ("2nd"), ("3rd"), ("4th")])
    cookie4 = SelectField(id="4",choices=[("---"), ("1st"), ("2nd"), ("3rd"), ("4th")])
    submit = SubmitField("Submit Vote", id="submitButton")

class BakerVotingForm(FlaskForm):
    cookie1 = SelectField(id="1", choices=[("---"), ("1st"), ("2nd"), ("3rd")])
    cookie2 = SelectField(id="2",choices=[("---"), ("1st"), ("2nd"), ("3rd")])
    cookie3 = SelectField(id="3",choices=[("---"), ("1st"), ("2nd"), ("3rd")])
    submit = SubmitField("Submit Vote", id="submitButton")
    

class AwardsForm(FlaskForm):
    most_creative = SelectField(id="awardDropdown0", choices =[("---"), ("Chocolate Grocery Store"), ("Gingerbread Royal Cream"), ("Tiramisu Cookie"), ("Italian Ricotta")])
    best_presentation = SelectField(id="awardDropdown1", choices =[("---"), ("Chocolate Grocery Store"), ("Gingerbread Royal Cream"), ("Tiramisu Cookie"), ("Italian Ricotta")])
    submit = SubmitField("Submit Vote", id="submitButton")
    
class BakerForm(FlaskForm):
    baker = RadioField("baker", choices=[("Christopher", "Christopher"), ("Bridget", "Bridget"), ("Michael", "Michael"), ("Maria", "Maria")])
    submit = SubmitField("Submit", id="submitButton")