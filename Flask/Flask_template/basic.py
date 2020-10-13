from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('basic.html') # use render_template to render the html file


if __name__ == '__main__':
    app.run(debug=True)
