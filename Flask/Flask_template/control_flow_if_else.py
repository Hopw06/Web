from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def index():
    num = random.randint(0, 1000)
    return render_template("control_flow_if_else.html", num=num)


if __name__ == "__main__":
    app.run(debug=True)
