from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home_exer.html')


@app.route("/report")
def report():
    userName = request.args.get('user_name')
    cond1 = False
    cond2 = False
    cond3 = False
    for letter in userName:
        if letter.islower():
            cond1 = True
        if letter.isupper():
            cond2 = True
    if userName[-1].isdigit():
        cond3 = True
    return render_template('report_exer.html', cond1=cond1, cond2=cond2, cond3=cond3)


if __name__ == "__main__":
    app.run(debug=True)
