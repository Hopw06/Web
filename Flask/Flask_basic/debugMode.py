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
    return "<h1>100th letter: {}</h1>".format(name[100]) # make an error


if __name__ == "__main__":
    app.run(debug=True) # run in debug mode