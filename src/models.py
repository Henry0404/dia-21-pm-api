from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    height = db.Column(db.String(250))
    mass = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250))

    def save(self):
        db.session.add(self)  # INSERT
        db.session.commit()  # Guarda el INSERT

    def update(self):
        db.session.commit()  # Guarda el UPDATE

    def delete(self):
        db.session.delete(self)  # DELETE
        db.session.commit()  # Guarda el DELETE

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }