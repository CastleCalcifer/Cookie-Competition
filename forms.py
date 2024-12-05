from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class VotingForm(FlaskForm):
    cookie1 = SelectField(id="1", choices=[("---"), ("1st"), ("2nd"), ("3rd"), ("4th"), ("5th")])
    cookie2 = SelectField(id="2",choices=[("---"), ("1st"), ("2nd"), ("3rd"), ("4th"), ("5th")])
    cookie3 = SelectField(id="3",choices=[("---"), ("1st"), ("2nd"), ("3rd"), ("4th"), ("5th")])
    cookie4 = SelectField(id="4",choices=[("---"), ("1st"), ("2nd"), ("3rd"), ("4th"), ("5th")])
    cookie5 = SelectField(id="5",choices=[("---"), ("1st"), ("2nd"), ("3rd"), ("4th"), ("5th")])
    submit = SubmitField("Submit Vote", id="submitButton")