"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.models import Property
from app.forms import PropertyForm
from werkzeug.utils import secure_filename
import os


###
# Routing for your application.
###

@app.route('/',methods=['GET', 'POST'])
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/add_property', methods=['POST', 'GET'])
def add_property():
    form = PropertyForm()
    if request.method == "POST":

        if form.validate_on_submit:
            title = form.title.data
            num_bed = form.num_bed.data
            num_bath = form.num_bed.data
            prop_location = form.prop_location.data
            price = form.price.data
            prop_type = form.prop_type.data
            desc = form.desc.data
            image = form.image.data

            img_filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))

            entry = Property(title=title, num_bed= num_bed, num_bath=num_bath, prop_location=prop_location, price=price, prop_type=prop_type,photo=img_filename, desc=desc)
            db.session.add(entry)
            db.session.commit()

            flash('Property Added', 'success')
            return redirect(url_for('home'))
            
    return render_template("add_property.html", form=form)

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
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
