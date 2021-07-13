from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
import time
#from forms import RegistrationForm, LoginForm
from flask_marshmallow import Marshmallow ,Schema
from flask import Flask ,Blueprint
from setup import db, ma , app
import os





basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#User = Blueprint('User',__name__)

#User Class/Model
class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    #private_id = db.Column(db.String(50), unique=True)
    user_name = db.Column(db.String(50) , unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False )
    creation_date = db.Column(db.DateTime, auto_now_add=True)
    password = db.Column(db.String(100), nullable=False)
    #creation_date = db.Column(default=timezone.now)

"""
options for creation date to batter save mode from updates

from django.utils import timezone
 class User(models.Model):
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs) 


"""
     
 



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
users_schema = UserSchema(many=True)

if __name__ == '__main__':
	app.run(debug=True, port=5000)



