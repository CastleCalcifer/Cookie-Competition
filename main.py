import os

from flask_migrate import Migrate
from databaseModels import db
from flask import Flask, render_template, redirect, url_for, request
from forms import VotingForm

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQL_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "TEMP KEY"
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

db.init_app(app)
Migrate(app, db)

with app.app_context():
    db.create_all()
    
@app.route('/', methods=["GET", "POST"])
def index():
    form:VotingForm = VotingForm()      
    if form.validate_on_submit():
        cookieList = [form.cookie1.data, form.cookie2.data, form.cookie3.data, form.cookie4.data, form.cookie5.data]
        for i in cookieList:
            print(i)
    cookieList = [form.cookie1.data, form.cookie2.data, form.cookie3.data, form.cookie4.data, form.cookie5.data]
    for i in cookieList:
        print(i)
    print(form.errors)
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)