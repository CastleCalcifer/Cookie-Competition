import os

from flask_migrate import Migrate
from sqlalchemy import desc
from databaseModels import db, Cookie, Year
from flask import Flask, render_template, redirect, url_for, request, session
from forms import BakerVotingForm, VotingForm, AwardsForm, BakerForm
from utilities import parseVote
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQL_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "TEMP KEY"
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db.init_app(app)
Migrate(app, db)


admin = Admin(app)
admin.add_view(ModelView(Year, db.session))

with app.app_context():
    db.create_all()
    cookie = Cookie.query.filter_by(cookie_name="Chocolate Grocery Store").first()
    if not cookie:
        db.session.add(Year(year=2024))
        db.session.add(Cookie(cookie_name="Chocolate Grocery Store", year=2024, baker_name="Christopher", image="https://assets.bonappetit.com/photos/5ca534485e96521ff23b382b/1:1/w_2560%2Cc_limit/chocolate-chip-cookie.jpg"))
        db.session.add(Cookie(cookie_name="Gingerbread Royal Cream", year=2024, baker_name="Michael", image="https://www.thepkpway.com/wp-content/uploads/2017/12/gingerbread-cookies-3f.jpg"))
        db.session.add(Cookie(cookie_name="Tiramisu Cookie", year=2024, baker_name="Maria", image="https://thelittlevintagebakingcompany.com/wp-content/uploads/2023/03/Sprinkle-Sugar-Cookies-15.jpg"))
        db.session.add(Cookie(cookie_name="Italian Ricotta", year=2024, baker_name="Bridget", image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQh4k251xFF_9ijySYa4PoRBwdRDOixcZmkhw&s"))
        db.session.commit()
        
        
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/voting', methods=["GET", "POST"])
def voting():
    form:VotingForm = VotingForm()      
    yearly_cookies:list[Cookie] = db.session.query(Cookie).filter(Cookie.year==2024).all()
    if form.validate_on_submit():
        results:list[str] = [form.cookie1.data, form.cookie2.data, form.cookie3.data, form.cookie4.data]
        for i in range(len(yearly_cookies)):
            yearly_cookies[i].score = Cookie.score + parseVote(results[i])
        db.session.commit()
        return redirect(url_for("awards"))
    else:
        print(form.errors)
        return render_template('voting.html', cookie1_name=yearly_cookies[0].cookie_name.upper(), cookie1_image=yearly_cookies[0].image, 
                                cookie2_name=yearly_cookies[1].cookie_name.upper(), cookie2_image=yearly_cookies[1].image,
                                cookie3_name= yearly_cookies[2].cookie_name.upper(), cookie3_image= yearly_cookies[2].image,
                                cookie4_name=yearly_cookies[3].cookie_name.upper(), cookie4_image=yearly_cookies[3].image,
                                form=form)

@app.route("/results")
def results():
    if db.session.query(Year).filter(Year.year == 2024).first().resultsViewable:
        rankings = db.session.query(Cookie).filter(Cookie.year == 2024).order_by(desc(Cookie.score)).all()
        rankings.reverse()
        presentation = db.session.query(Cookie).filter(Cookie.year == 2024).order_by(desc(Cookie.presentation_points)).first()
        creative = db.session.query(Cookie).filter(Cookie.year == 2024).order_by(desc(Cookie.creative_points)).first()
        return render_template('results.html', 
                            cookie1_name=rankings[0].cookie_name.upper(), cookie1_image=rankings[0].image, cookie1_score = rankings[0].score,
                            cookie2_name=rankings[1].cookie_name.upper(),cookie2_image=rankings[1].image, cookie2_score = rankings[1].score,
                            cookie3_name= rankings[2].cookie_name.upper(), cookie3_image= rankings[2].image, cookie3_score = rankings[2].score,
                            cookie4_name=rankings[3].cookie_name.upper(), cookie4_image=rankings[3].image, cookie4_score = rankings[3].score,
                            presentation_name=presentation.cookie_name.upper(), presentation_image=presentation.image, presentation_score = presentation.presentation_points,
                            creative_name=creative.cookie_name.upper(), creative_image=creative.image, creative_score = creative.creative_points) 
    else: 
        return render_template('waiting.html')


@app.route("/awards", methods=["GET", "POST"])
def awards():
    form:AwardsForm = AwardsForm()
    baker_cookie = db.session.query(Cookie).filter(Cookie.year == 2024).filter(Cookie.baker_name == session.get("baker")).first()
    if form.validate_on_submit():
        results = [form.best_presentation.data, form.most_creative.data]
        print(results)
        yearly_cookies:list[Cookie] = db.session.query(Cookie).filter(Cookie.year==2024).all()
        for cookie in yearly_cookies:
            if results[0] == cookie.cookie_name:
                cookie.creative_points = Cookie.creative_points + 1
            if results[1] == cookie.cookie_name:
                cookie.presentation_points = Cookie.presentation_points + 1
        db.session.commit()
        return redirect(url_for("results"))
    if baker_cookie == None:
        return render_template("awards.html", baker_cookie="", form=form)
    else:
        return render_template("awards.html", baker_cookie=baker_cookie.cookie_name, form=form)

@app.route('/bakers', methods=["GET", "POST"])
def bakers():
    form:BakerForm = BakerForm()
    if form.validate_on_submit():
        session["baker"] = form.baker.data
        return redirect(url_for('bakervoting'))
    else:
        print(form.errors)
    return render_template('bakers.html', form=form)


@app.route('/bakervoting', methods=["GET", "POST"])
def bakervoting():
    print(session["baker"])
    form:BakerVotingForm = BakerVotingForm()      
    yearly_cookies:list[Cookie] = db.session.query(Cookie).filter(Cookie.year==2024).filter( Cookie.baker_name != session["baker"]).all()
    if form.validate_on_submit():
        results:list[str] = [form.cookie1.data, form.cookie2.data, form.cookie3.data]
        for i in range(len(yearly_cookies)):
            yearly_cookies[i].score = Cookie.score + parseVote(results[i])
        db.session.commit()
        return redirect(url_for("awards"))
    else:
        print(form.errors)
        for i in yearly_cookies:
            print(i)
        return render_template('bakervoting.html', cookie1_name=yearly_cookies[0].cookie_name.upper(), cookie1_image=yearly_cookies[0].image, 
                                cookie2_name=yearly_cookies[1].cookie_name.upper(), cookie2_image=yearly_cookies[1].image,
                                cookie3_name= yearly_cookies[2].cookie_name.upper(), cookie3_image= yearly_cookies[2].image,
                                form=form)




if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port="5000", debug=True)