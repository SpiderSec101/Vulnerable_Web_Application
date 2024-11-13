from application import db
from flask_login import LoginManager, UserMixin, login_user


class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)# setting unique to flase because this will hold all the user data 
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.password}')"    

