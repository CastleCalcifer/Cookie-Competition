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
    form = VotingForm()
    # if form.validate_on_submit():
    #     cookie1 = form.cookie1.data
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)