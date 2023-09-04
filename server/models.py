from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from app import app

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    species = db.Column(db.String)
    zookeeper = db.relationship('zookeepers', backref='animals')
    enclosure = db.relationship('enclosures', backref='animals')

    def __repr__(self):
        return f'<Animal is {self.name}>'

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    birthday = db.Columns(db.String)
    animals = db.relationship('animals', backref='zookeepers')

    def __repr__(self):
        return f'<Zookeeper is {self.name}>'

class Enclosure(db.Model):
    __tablename__ = 'enclosures'
    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)
    animals = db.relationship('animals', backref='enclosures')

    def __repr__(self):
        return f'<Enclosure is {self.environment}>'


