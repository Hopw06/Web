# forms.py underneath the owners folder.
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    owner = StringField("Owner's name: ")
    id_puppy = IntegerField("Id of puppy: ")
    submit = SubmitField("Add Owner")
