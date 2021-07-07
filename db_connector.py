from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
import time
#from forms import RegistrationForm, LoginForm
from flask_marshmallow import Marshmallow ,Schema
from flask import Flask
import os

app = Flask(__name__)

db = SQLAlchemy(app)
ma = Marshmallow(app)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#User Class/Model
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    #private_id = db.Column(db.String(50), unique=True)
    user_name = db.Column(db.String(50) , unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False )
    creation_date = db.Column(db.DateTime, nullable=False)
    password = db.Column(db.String(100), nullable=False)


     
    def __init__(self,user_id  , user_name, email , creation_date , password):
      self.user_id = user_id
      self.user_name  = user_name
      self.email  = email
      self.creation_date  = creation_date
      self.password = password

    def __repr__(self):
        return f"User('{self.user_name}' '{self.email}') "


"""

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nulllabel=False)


    def user_info(self,user_id,user_name,email,creation_date):
      self.user_id = user_id
      self.user_name  = user_name
      self.email  = email
      self.creation_date  = creation_date


"""
#user schema
class UserSchema(ma.Schema):
  class Meta:
    fields = ('user_id', 'user_name', 'email', 'creation_date', 'password')


# Init schema
user_schema = UserSchema()
users_schema = UserSchema()

if __name__ == '__main__':
	app.run(debug=True, port=5000)



