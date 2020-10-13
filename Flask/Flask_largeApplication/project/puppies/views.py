# project/puppies/views.py
from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import Puppy
from project.puppies.forms import AddForm, DelForm

puppies_blueprints = Blueprint(
    'puppies', __name__, template_folder='templates/puppies')


@puppies_blueprints.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        if name != None and name != "":
            exists = Puppy.query.filter_by(name=name).first()
            if exists == None:
                new_pup = Puppy(name)
                db.session.add(new_pup)
                db.session.commit()
                return redirect(url_for('puppies.list'))
            else:
                return render_template("error.html", error="Puppy is already in system.")
        else:
            return render_template("error.html", error="Please enter puppy name.")

    return render_template("add.html", form=form)


@puppies_blueprints.route("/list")
def list():
    puppies = Puppy.query.all()
    return render_template("list.html", puppies=puppies)


@puppies_blueprints.route('/del', methods=['GET', 'POST'])
def delete():

    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        if pup != None:
            db.session.delete(pup)
            db.session.commit()
            return redirect(url_for('puppies.list'))
        else:
            return render_template("error.html", error="Id you provided is not valid.")

    return render_template("delete.html", form=form)
