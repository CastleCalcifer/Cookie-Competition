import os

from flask_migrate import Migrate
from databaseModels import db, Cookie
from flask import Flask, render_template, redirect, url_for, request
from forms import VotingForm
from utilities import parseVote
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
    cookie = Cookie.query.filter_by(cookie_name="Chocolate Chip").first()
        
@app.route('/', methods=["GET", "POST"])
def index():
    form:VotingForm = VotingForm()      
    yearly_cookies:list[Cookie] = db.session.query(Cookie).filter(Cookie.year==2024).all()
    if form.validate_on_submit():
        results:list[str] = [form.cookie1.data, form.cookie2.data, form.cookie3.data, form.cookie4.data, form.cookie5.data]
        for i in range(len(yearly_cookies)):
            yearly_cookies[i].score = Cookie.score + parseVote(results[i])

        db.session.commit()
        return render_template('results.html')
    else:
        print(form.errors)
        yearly_cookies = db.session.query(Cookie).filter(Cookie.year==2024).all()
        cookie1 = yearly_cookies[0]
        cookie2 = yearly_cookies[1]
        cookie3 = yearly_cookies[2]
        cookie4 = yearly_cookies[3]
        cookie5 = yearly_cookies[4]
        return render_template('index.html', cookie1_name=cookie1.cookie_name, cookie1_image=cookie1.image, cookie2_name=cookie2.cookie_name, cookie2_image=cookie2.image,
                                cookie3_name=cookie3.cookie_name, cookie3_image=cookie3.image, cookie4_name=cookie4.cookie_name, cookie4_image=cookie4.image,
                                cookie5_name=cookie5.cookie_name, cookie5_image=cookie5.image, form=form)


if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port="5000", debug=True)