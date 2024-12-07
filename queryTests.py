from sqlalchemy import desc
from databaseModels import db, Cookie
from main import app

with app.app_context():
    cookies = db.session.query(Cookie).filter(Cookie.year == 2024).order_by(desc(Cookie.score)).all()
    print(cookies)