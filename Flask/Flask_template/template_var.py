from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    name = "Phong"
    letter = list(name)
    myInfo = {"name": "Phong", "age": 24}
    return render_template("template_var.html", name=name, letter=letter, myInfo=myInfo)


if __name__ == "__main__":
    app.run(debug=True)
