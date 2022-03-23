from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, IntegerField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.widgets import TextArea

class PropertyForm(FlaskForm):
    title = StringField("Title",validators=[DataRequired()])
    num_bed = IntegerField("Bedrooms",validators=[DataRequired()])
    num_bath = IntegerField("Bathrooms",validators=[DataRequired()])
    prop_location = StringField("Location",validators=[DataRequired()])
    price = DecimalField("Price",validators=[DataRequired()],places=2)
    prop_type = SelectField("Type", validators=[DataRequired()], choices=[('ap','Apartment'),('hs','House')])
    desc = StringField('Description', validators=[DataRequired()], widget=TextArea())
    image = FileField("Image", validators=[FileRequired(),FileAllowed(["jpg","png","Images only!"])])



