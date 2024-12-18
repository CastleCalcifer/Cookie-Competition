import os

from flask_migrate import Migrate
from sqlalchemy import desc
from databaseModels import db, Cookie
from flask import Flask, render_template, redirect, url_for, request
from forms import VotingForm, AwardsForm
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
    cookie = Cookie.query.filter_by(cookie_name="Chocolate Grocery Store").first()
    if not cookie:
        db.session.add(Cookie(cookie_name="Chocolate Grocery Store", year=2024, image="https://assets.bonappetit.com/photos/5ca534485e96521ff23b382b/1:1/w_2560%2Cc_limit/chocolate-chip-cookie.jpg"))
        db.session.add(Cookie(cookie_name="Gingerbread Royal Cream", year=2024, image="https://www.thepkpway.com/wp-content/uploads/2017/12/gingerbread-cookies-3f.jpg"))
        db.session.add(Cookie(cookie_name="Tiramisu Cookie", year=2024, image="https://thelittlevintagebakingcompany.com/wp-content/uploads/2023/03/Sprinkle-Sugar-Cookies-15.jpg"))
        db.session.add(Cookie(cookie_name="Italian ricotta", year=2024, image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQh4k251xFF_9ijySYa4PoRBwdRDOixcZmkhw&s"))
        db.session.add(Cookie(cookie_name="Red Velvet", year=2024, image="https://bakingamoment.com/wp-content/uploads/2023/12/IMG_0082-red-velvet-chocolate-chip-cookies.jpg"))
        db.session.commit()
        
        
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/voting', methods=["GET", "POST"])
def voting():
    form:VotingForm = VotingForm()      
    yearly_cookies:list[Cookie] = db.session.query(Cookie).filter(Cookie.year==2024).all()
    if form.validate_on_submit():
        results:list[str] = [form.cookie1.data, form.cookie2.data, form.cookie3.data, form.cookie4.data, form.cookie5.data]
        for i in range(len(yearly_cookies)):
            yearly_cookies[i].score = Cookie.score + parseVote(results[i])
        db.session.commit()
        return redirect(url_for("results"))
    else:
        print(form.errors)
        yearly_cookies = db.session.query(Cookie).filter(Cookie.year==2024).all()
        return render_template('voting.html', cookie1_name=yearly_cookies[0].cookie_name.upper(), cookie1_image=yearly_cookies[0].image, 
                                cookie2_name=yearly_cookies[1].cookie_name.upper(), cookie2_image=yearly_cookies[1].image,
                                cookie3_name= yearly_cookies[2].cookie_name.upper(), cookie3_image= yearly_cookies[2].image,
                                cookie4_name=yearly_cookies[3].cookie_name.upper(), cookie4_image=yearly_cookies[3].image,
                                cookie5_name=yearly_cookies[4].cookie_name.upper(), cookie5_image=yearly_cookies[4].image,
                                form=form)

@app.route("/results")
def results():
    rankings = db.session.query(Cookie).filter(Cookie.year == 2024).order_by(desc(Cookie.score)).all()
    return render_template('results.html', 
                           cookie1_name=rankings[0].cookie_name.upper(), cookie1_image=rankings[0].image, cookie1_score = rankings[0].score,
                           cookie2_name=rankings[1].cookie_name.upper(),cookie2_image=rankings[1].image, cookie2_score = rankings[1].score,
                           cookie3_name= rankings[2].cookie_name.upper(), cookie3_image= rankings[2].image, cookie3_score = rankings[2].score,
                           cookie4_name=rankings[3].cookie_name.upper(), cookie4_image=rankings[3].image, cookie4_score = rankings[3].score,
                           cookie5_name=rankings[4].cookie_name.upper(), cookie5_image=rankings[4].image, cookie5_score = rankings[4].score,) 

@app.route("/awards")
def awards():
    form:AwardsForm = AwardsForm()
    return render_template("awards.html", form=form)


if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port="5000", debug=True)