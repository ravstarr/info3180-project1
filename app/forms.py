from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms import DecimalField, IntegerField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, NumberRange


class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    bedrooms = IntegerField('Bedrooms', validators=[DataRequired(), NumberRange(min=0)])
    bathrooms = IntegerField('Bathrooms', validators=[DataRequired(), NumberRange(min=0)])
    location = StringField('Location', validators=[DataRequired()])
    price = DecimalField('Price', places=2, validators=[DataRequired(), NumberRange(min=0)])
    type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
