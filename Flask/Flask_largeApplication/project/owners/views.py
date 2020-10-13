# project/puppies/views.py
from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.owners.forms import AddForm
from project.models import Puppy, Owner

owners_blueprints = Blueprint(
    'owners', __name__, template_folder='templates/owners')


@owners_blueprints.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()
    if form.validate_on_submit():

        id_puppy = form.id_puppy.data
        owner = form.owner.data

        if owner != "" and id_puppy != "":
            puppy = Puppy.query.get(id_puppy)
            if puppy != None and puppy.owner == None:
                owner = Owner(owner, id_puppy)

                db.session.add(owner)
                db.session.commit()
                return redirect(url_for('puppies.list'))
            else:
                return render_template("error.html", error="Puppy id you provided is not valid")
        else:
            return render_template("error.html", error="Please enter owner's name and puppy id.")

    return render_template("addOwner.html", form=form)
