from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
from flask_marshmallow import Marshmallow ,Schema
from setup import db, ma, app
import os
from sqlalchemy import Integer, String, Column ,DateTime



basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'user.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#User Class/Model
class User(db.Model):
    __tablename__ = 'user.sqlite'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50) ,nullable=False)
    email = Column(String(80), unique=True, nullable=False )
    creation_date = Column(DateTime,default = datetime.now)
    password = Column(String(100), nullable=False)

    def __init__(self,user_id  , user_name, email  , password, creation_date ): 
      self.user_id = user_id
      self.user_name  = user_name
      self.email  = email
      self.creation_date  = creation_date
      self.password = password
    
    #return info from db to outside 
    def __repr__(self):
        return f" {self.user_name}"

    def to_json(self):
 	    return {

            'date_created': self.creation_date
        }

db.create_all()

     
 
def __init__(self,user_id  , user_name, email  , password, creation_date ): 
      self.user_id = user_id
      self.user_name  = user_name
      self.email  = email
      self.creation_date  = creation_date
      self.password = password
      
      def __repr__(self):
        return '<User %r>' % self.user_name 


if __name__ == '__main__':
    app.run(debug=True, port=5000)



