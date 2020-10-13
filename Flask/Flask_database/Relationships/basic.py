# Create entries into the table.
from models import db, Puppy, Owner, Toy

# Create two puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')

db.session.add_all([rufus, fido])
db.session.commit()

# Check
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()

# Create owner object
jose = Owner('Jose', rufus.id)

# Give toy to Rufus.
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

# Grap Rufus after those additions.
rufus = Puppy.query.filter_by(name="Rufus").first()
print(rufus)
rufus.report_toys()
