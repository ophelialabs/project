from flask_login import UserMixin
from datetime import datetime
from . import db

# Add to User model
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    # Add these fields to existing User model
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    # Add indexes for frequently queried fields
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)

    # Add relationship for user roles
    roles = db.relationship('Role', secondary='user_roles',
                          backref=db.backref('users', lazy='dynamic'))

    def avatar(self, size):
        return f'static/profile_pics/{self.image_file}'
import jwt
from time import time
from flask import current_app

class User(UserMixin, db.Model):
    # Add to existing User model
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                          algorithms=['HS256'])['reset_password']
        except:
            return None
        return User.query.get(id)

    def get_token(self, expires_in=3600):
        return jwt.encode(
            {'user_id': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )

    @staticmethod
    def check_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                         algorithms=['HS256'])['user_id']
        except:
            return None
        return User.query.get(id)