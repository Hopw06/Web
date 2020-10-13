import os
from forms import AddForm, DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

#######################
##### SQL Database #####
#######################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

######################
#### Models ###########
######################


class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    owner = db.relationship("Owner", backref="puppy", uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner == None:
            return "Puppy name: {}, and has not owner yet".format(self.name)
        return "Puppy name {}, and has owner: {}".format(self.name, self.owner.name)


class Owner(db.Model):

    __tablename__ = 'owner'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    id_pup = db.Column(db.Integer, db.ForeignKey("puppies.id"))

    def __init__(self, name, id_pup):
        self.name = name
        self.id_pup = id_pup


#######################################
###### View functions - Have Forms ########
#######################################

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/add", methods=["GET", "POST"])
def add_pup():

    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        if name != None and name != "":
            exists = Puppy.query.filter_by(name=name).first()
            if exists == None:
                new_pup = Puppy(name)
                db.session.add(new_pup)
                db.session.commit()
                return redirect(url_for('list_pups'))
            else:
                return render_template("error.html", error="Puppy is already in system.")
        else:
            return render_template("error.html", error="Please enter puppy name.")

    return render_template("add.html", form=form)


@app.route("/list")
def list_pups():
    puppies = Puppy.query.all()
    return render_template("list.html", puppies=puppies)


@app.route("/delete", methods=["GET", "POST"])
def delete_pup():

    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        if pup != None:
            db.session.delete(pup)
            db.session.commit()
            return redirect(url_for('list_pups'))
        else:
            return render_template("error.html", error="Id you provided is not valid.")

    return render_template("delete.html", form=form)


@app.route("/addOwner", methods=["GET", "POST"])
def add_owner():

    form = AddOwnerForm()
    if form.validate_on_submit():

        id_puppy = form.id_puppy.data
        owner = form.owner.data

        if owner != "" and id_puppy != "":
            puppy = Puppy.query.get(id_puppy)
            if puppy != None and puppy.owner == None:
                owner = Owner(owner, id_puppy)

                db.session.add(owner)
                db.session.commit()
                return redirect(url_for('list_pups'))
            else:
                return render_template("error.html", error="Puppy id you provided is not valid")
        else:
            return render_template("error.html", error="Please enter owner's name and puppy id.")

    return render_template("addOwner.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
