from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField("Name of Puppy: ")
    submit = SubmitField("Add Puppy")


class DelForm(FlaskForm):

    id = IntegerField("Id Number of Puppy to remove: ")
    submit = SubmitField("Remove")


class AddOwnerForm(FlaskForm):

    owner = StringField("Owner's name: ")
    id_puppy = IntegerField("Id of puppy: ")
    submit = SubmitField("Add Owner")
