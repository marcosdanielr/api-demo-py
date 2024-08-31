from flask import Flask, request

from models import db, Animals
import json

app = Flask(__name__)

db.connect()
db.create_tables([Animals])

@app.route('/animals', methods=['GET'])
def handle_list_animals():
    animals = Animals.select().execute()

    animals_list = [animal.__data__ for animal in animals]
    return json.dumps(animals_list)

@app.route('/animals', methods=['POST'])
def handle_create_animal():
    name = request.get_json()['name']
    age = request.get_json()['age']

    Animals.insert({
        Animals.name: name,
        Animals.age: age
    }).execute()

    return {
        "message": "animal created"
    }
