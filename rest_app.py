"""d
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

#import pymysql, json, flask, selenium 
from flask_marshmallow import Marshmallow 
from db_connector import User ,  UserSchema
from flask import Flask , jsonify , request
from setup import db , app, ma
from marshmallow import Schema
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  

class UserSchema(ma.Schema):
  class Meta:
    fields = ('user_id', 'user_name', 'email', 'creation_date', 'password')


# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)



#@app.route('/')
#def hello():
#    return "hello world"

name_list = {}
user_name = {}
# Make the WSGI interface available at the top level so wfastcgi can get it.
#wsgi_app = app.wsgi_app
"""

@app.route('/users/<USER_ID>', methods=['POST'])
def add_user():
    user =  '{"status":"ok", "user_added":"<user_name>"}' , 200
    return jsonify(user)
   

    return {"user_name":"string"}

@app.route('/users/<USER_ID>', methods=['GET'])
def get_exiting_user_data(self):
    for i in user_name:
        if i['user_name'] == name:
            return i
    return {'user_name': None}
"""

@app.route('/' , methods=['GET'])
def check():
    return jsonify({ 'text': 'Hello World!' })

    
"""

@app.route('/users' , methods=['POST'])
def exiting_user_data():
    #get name from user and put it in user_name
    print("its work?")
    user_name['name'] = 'value'
    name = json.dumps(user_name)
    return  'user_name: ', name
"""

"""
@app.route('/users', methods=['GET'])
def get_exiting_user_data():
    response = {
        'massage' : 'hello there , enter your name: '
    }
    return json(response), 200
"""
#@app.route('/users', methods=['GET'])
#def get_exiting_user_data():
    #return jsonify({'user_name' : user_name})

"""
@app.route('/users/<USER_ID>', methods=['PUT'])
def update_user():
    

@app.route('/users/<USER_ID>', methods=['DELETE'])
def delete_user(self):


"""

#create a user
@app.route('/users', methods=['POST'])
def add_user():
  user_id = request.json['user_id'] 
  user_name = request.json['user_name']
  email = request.json['email']
  password = request.json['password']
  #creation_date = request.json['creation_date']

  new_user = User(user_id, user_name, email  , password) #creation_date

  db.session.add(new_user)
  db.session.commit()

  return user_schema.jsonify(new_user)


# Get All Users
@app.route('/users', methods=['GET'])
def get_users():
  all_users = User.query.all()
  result = user_schema.dump(all_users, many=True )
  return jsonify(result)

# Get Single user
@app.route('/users/<USER_ID>', methods=['GET'])
def get_user(user_id):
  user = User.query.get(USER_ID)
  return user_schema.jsonify(users)


# Update a User
@app.route('/users/<USER_ID>', methods=['PUT'])
def update_user(USER_ID):
  user = User.query.get(USER_ID)

  user_id = request.json['user_id']
  user_name = request.json['user_name']
  email = request.json['email']
  password = request.json['password']
  creation_date = request.json['creation_date']


  user.user_id = user_id
  user.user_name = user_name
  user.email = email
  user.password = password
  user.creation_date = creation_date

  db.session.commit()

  return product_schema.jsonify(users)


# Delete User
@app.route('/users/<USER_ID>', methods=['DELETE'])
def delete_user(user_id):
  user = User.query.get(user_id)
  db.session.delete(user)
  db.session.commit()

  return user_schema.jsonify(users)




if __name__ == '__main__':
	app.run(debug=True, port=5000 , host='localhost')
