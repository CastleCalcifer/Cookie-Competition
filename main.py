import os

from flask_migrate import Migrate
from databaseModels import db
from flask import Flask, render_template, redirect, url_for, request


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
    
@app.route('/')
def index():

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")