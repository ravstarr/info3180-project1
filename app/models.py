"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the models for your application.
"""

from app import db


class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    no_of_rooms = db.Column(db.Integer, nullable=False)
    no_of_bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    property_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Property {}>'.format(self.title)
