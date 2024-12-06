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
    if not cookie:
        db.session.add(Cookie(cookie_name="Chocolate Chip", year=2024, image="https://assets.bonappetit.com/photos/5ca534485e96521ff23b382b/1:1/w_2560%2Cc_limit/chocolate-chip-cookie.jpg"))
        db.session.add(Cookie(cookie_name="Gingerbread", year=2024, image="https://www.thepkpway.com/wp-content/uploads/2017/12/gingerbread-cookies-3f.jpg"))
        db.session.add(Cookie(cookie_name="Sugar", year=2024, image="https://thelittlevintagebakingcompany.com/wp-content/uploads/2023/03/Sprinkle-Sugar-Cookies-15.jpg"))
        db.session.add(Cookie(cookie_name="Oreo", year=2024, image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQh4k251xFF_9ijySYa4PoRBwdRDOixcZmkhw&s"))
        db.session.add(Cookie(cookie_name="Red Velvet", year=2024, image="https://bakingamoment.com/wp-content/uploads/2023/12/IMG_0082-red-velvet-chocolate-chip-cookies.jpg"))
        db.session.commit()
        
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
        return render_template('index.html', cookie1_name=yearly_cookies[0].cookie_name, cookie1_image=yearly_cookies[0].image, cookie2_name=yearly_cookies[1].cookie_name, cookie2_image=yearly_cookies[1].image,
                                cookie3_name= yearly_cookies[2].cookie_name, cookie3_image= yearly_cookies[2].image, cookie4_name=yearly_cookies[3].cookie_name, cookie4_image=yearly_cookies[3].image,
                                cookie5_name=yearly_cookies[4].cookie_name, cookie5_image=yearly_cookies[4].image, form=form)

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port="5000", debug=True)