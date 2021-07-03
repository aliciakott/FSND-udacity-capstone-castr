import os
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DATABASE_URL = os.environ.get('DATABASE_URL')

def setup_db(app, DATABASE_URL=DATABASE_URL):
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()

filmography = db.Table('filmography',
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True),
    db.Column('actor_id', db.Integer, db.ForeignKey('actors.id'), primary_key=True)
)

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    actors = db.relationship('Actor', secondary=filmography, backref=db.backref('movies', lazy=True))

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

    def __repr__(self):
        return f'<Project ID: {self.id}, title: {self.title}, release_date: {self.release_date}>'


class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(), nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    def __repr__(self):
        return f'<Talent ID: {self.id}, name: {self.name}, age: {self.age}, gender: {self.gender}>'
