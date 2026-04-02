from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, IntegerField, DecimalField, SelectField
from wtforms.validators import DataRequired, NumberRange


class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    bedrooms = IntegerField('No. of Bedrooms', validators=[DataRequired(), NumberRange(min=1)])
    bathrooms = IntegerField('No. of Bathrooms', validators=[DataRequired(), NumberRange(min=1)])
    location = StringField('Location', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)], places=2)
    property_type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')],
                                validators=[DataRequired()])
    photo = FileField('Property Photo', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
