
from db_connector import User
import setup
import rest_app 
from flask import Flask


""" 
app = Flask(__name__)

@app.route("/users/get_user_data/<USER_ID>")
def get_user_name(USER_ID):
    
    adding = User.query.get(USER_ID)
    usering = str(adding)
    if usering != "None":
        return "<H1>" + usering + "</H1>"
    else:       
        return "<H1>" + "no such user:" + USER_ID + "</H1>" 

if __name__ == '__main__':
 app.run(debug = True ,port =5001, host = 'localhost')



@app.route("/stop_server")
def stop_server():
    os.kill(os.getpid(),signal.CTRL_C_EVENT)
    return 'Server stoped'
"""


