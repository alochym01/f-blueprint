# https://mitchellbusby.com/2016/08/20/tutorial-roll-your-own-user-authorisation-management-with-flask-login.html
# https://andypi.co.uk/2015/11/27/multiple-user-roles-python-flask/
# https://www.reddit.com/r/flask/comments/9f940z/best_way_to_integrate_roles_into_an_already/

from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))