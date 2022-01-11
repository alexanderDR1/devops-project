"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""


from flask_marshmallow import Marshmallow
from datetime import datetime
from db_connector import User
from flask import Flask, jsonify, request, url_for
from setup import db, app, ma
from marshmallow import schema
import os 



app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'user.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  


class UserSchema(ma.Schema):
  class Meta:
    fields = ('user_id', 'user_name', 'email', 'password', 'creation_date')


# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/')
def opening():
    return """
            <body style="background-color:black;"> 
            <h1 style='color: green;font-size:100px;text-align: center;'> REST API WEB  </h1>
            </body>
    """
#create a user
@app.route('/users', methods=['POST'])
def add_user():
  try:
    user_id = request.json['user_id']
    user_name = request.json['user_name']
    email = request.json['email']
    password = request.json['password']
    creation_date = datetime.now()
    
    new_user = User(user_id, user_name, email  , password, creation_date )
    
    db.session.add(new_user)
    db.session.commit()

   
    return user_schema.jsonify(new_user),200
  except: 
    return jsonify({'status': 'error', 'reason': 'bad request'}), 400

    
# Get All Users
@app.route('/users', methods=['GET'])
def get_users():
  try:     
     all_users = User.query.all()
     result = user_schema.dump(all_users, many=True )
     return jsonify(result),200
  
  except: 
      return jsonify({'status': 'error', 'reason': 'not found any user'}), 404


# Get Single user
@app.route('/users/<USER_ID>', methods=['GET'])
def get_user(USER_ID):
    user = User.query.get(USER_ID)
    usering = str(user)
    if usering != "None":
        return user_schema.jsonify(user), 200
    if usering == "None":
        return jsonify({'status': 'error', 'reason': 'no such id'}) , 404



# Update a User
@app.route('/users/<USER_ID>', methods=['PUT'])
def update_user(USER_ID):
  
 try:    
  user = User.query.get(USER_ID)

  
  user_id = request.json['user_id']
  user_name = request.json['user_name']
  email = request.json['email']
  password = request.json['password']
  creation_date = datetime.now()


  user.user_id = user_id
  user.user_name = user_name
  user.email = email
  user.password = password
  user.creation_date = creation_date

  db.session.commit()

  return jsonify({'status': 'ok', 'user updated successfully': 'user:' + USER_ID}), 200
 except:
  return jsonify({'status': 'error', 'reason': 'no such id'}), 404


# Delete User
@app.route('/users/<USER_ID>', methods=['DELETE'])
def delete_user(USER_ID): 
  try:  
    user = User.query.get(USER_ID)
    
    db.session.delete(user)
    db.session.commit()

    return {'status': 'ok', 'user_deleted': USER_ID}, 200
  except:
     return {'status': 'error', 'reason': 'no such id'} ,500



@app.route("/users/get_user_data/<USER_ID>")
def get_user_name(USER_ID):
    
    adding = User.query.get(USER_ID)
    usering = str(adding)
    if usering != "None":
        return "<H1>" + usering + "</H1>"
    else:       
        return "<H1>" + "no such user:" + USER_ID + "</H1>" 

@app.route("/stop_server")
def stop_server():
    os.kill(os.getpid(),signal.CTRL_C_EVENT)
    return 'Server stoped'


if __name__ == '__main__':
	app.run(host='0.0.0.0')
