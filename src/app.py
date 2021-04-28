from flask import Flask, json, jsonify, request
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db, Person

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'delevelopment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db.init_app(app)
Migrate(app, db)
CORS(app)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

@app.route("/people", methods=['GET'])
def getPeople():
    people = Person.query.all()
    people = list(map(lambda person: person.to_dict(), people))
    return jsonify(people), 200

@app.route("/people", methods=['POST'])
def createPerson():
    person = Person()
    person.name = request.json.get('name')
    person.height = request.json.get('height')
    person.mass = request.json.get('mass')
    person.hair_color = request.json.get('hair_color')
    person.skin_color = request.json.get('skin_color')
    person.eye_color = request.json.get('eye_color')
    person.birth_year = request.json.get('birth_year')
    person.gender = request.json.get('gender')
    person.save()
    
    return jsonify(person.to_dict()), 201

@app.route("/people/<int:person_id>", methods = ["GET"])
def getPerson(person_id):
    person = Person.query.get(person_id)
    
    if person:
        return jsonify(person.to_dict())

    return jsonify({"message": "Person not found"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3425, debug=False)