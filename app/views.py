"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import os
from uuid import uuid4

from flask import flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from app import app
from app.forms import PropertyForm
from app.models import Property, db


@app.route('/')
def home():
    """Render website's home page."""
    return redirect(url_for('properties'))


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/properties/create', methods=['GET', 'POST'])
def create_property():
    form = PropertyForm()
    if form.validate_on_submit():
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        ext = os.path.splitext(filename)[1]
        unique_filename = f"{uuid4().hex}{ext}"
        upload_dir = app.config['UPLOAD_FOLDER']
        os.makedirs(upload_dir, exist_ok=True)
        photo.save(os.path.join(upload_dir, unique_filename))

        property_item = Property(
            title=form.title.data,
            bedrooms=form.bedrooms.data,
            bathrooms=form.bathrooms.data,
            location=form.location.data,
            price=form.price.data,
            type=form.type.data,
            description=form.description.data,
            photo=unique_filename,
        )
        db.session.add(property_item)
        db.session.commit()
        flash('Property successfully added.', 'success')
        return redirect(url_for('properties'))

    if form.is_submitted() and form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{getattr(form, field).label.text}: {error}", 'danger')

    return render_template('create_property.html', form=form)


@app.route('/properties')
def properties():
    property_list = Property.query.order_by(Property.id.desc()).all()
    return render_template('properties.html', properties=property_list)


@app.route('/properties/<int:propertyid>')
def property_detail(propertyid):
    property_item = Property.query.get_or_404(propertyid)
    return render_template('property.html', property=property_item)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be ten seconds.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
