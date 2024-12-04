from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class VotingForm(FlaskForm):
    cookie1 = SelectField(choices=[("1st", "1st"), ("2nd, 2nd"), ("3rd", "3rd"), ("4th", "4th"), ("5th", "5th")])
    cookie2 = SelectField(choices=[("1st", "1st"), ("2nd, 2nd"), ("3rd", "3rd"), ("4th", "4th"), ("5th", "5th")])
    cookie3 = SelectField(choices=[("1st", "1st"), ("2nd, 2nd"), ("3rd", "3rd"), ("4th", "4th"), ("5th", "5th")])
    cookie4 = SelectField(choices=[("1st", "1st"), ("2nd, 2nd"), ("3rd", "3rd"), ("4th", "4th"), ("5th", "5th")])
    cookie5 = SelectField(choices=[("1st", "1st"), ("2nd, 2nd"), ("3rd", "3rd"), ("4th", "4th"), ("5th", "5th")])
    submit = SubmitField("Submit Vote")