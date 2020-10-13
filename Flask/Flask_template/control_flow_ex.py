from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    puppies = ['Fluffy', 'Rufus', 'Spike']
    return render_template("control_flow_ex.html", puppies=puppies)


if __name__ == "__main__":
    app.run(debug=True)
