from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello Puppy!</h1>"


@app.route('/information')
def info():
    return "<h1>Puppies are cute</h1>"


@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This page is for {}</h1>".format(name)

###############################
# Convert puppy name to latin_name:
# If name ends with 'y', change 'y' to 'iful'
# Else add 'y' to end of name.
###############################
@app.route('/puppy_latin/<name>')
def puppy_latin(name): 
    latin_name = ""
    if name[-1] == 'y':
        latin_name = name[:-1] + "iful"
    else:
        latin_name = name + "y"
    return "<h1>Hi {}, this is your latin name {} </h1>".format(name, latin_name)


if __name__ == "__main__":
    app.run()
