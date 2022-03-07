"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
#juan F Rivera
import os, requests
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Person
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/people', methods=['GET'])
def get_people():
    request_people = request
    print(request.data)
    return("hola"), 200
    #return jsonify(response_body), 200

base_url = "https://www.swapi.tech/api/"
@app.route('/poblar-personaje', methods=['GET'])
def get_poblar_personaje():
    response =  requests.get(f"{base_url}{'people'}/?page=1")
    results = response.json()['results']
    count = 0 
    for xdict in results:
        response = requests.get(xdict['url'])
        detaresponse = response.json()['result']['properties']
        person = Person.created(**detaresponse) 
        if person != None:
           count = count  + 1
         
    return jsonify({'count':count}),200













# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
