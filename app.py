from flask import Flask, render_template


app = Flask(__name__)


@app.route('/mail_uber')
def uber():
    return render_template('letter_example_1.html')


@app.route("/mail_other")
def mail_other():
    return render_template("letter_example_2.html")


@app.route("/mail_new")
def mail_new():
    return render_template("letter_example_3.html")


if __name__ == "__main__":
    app.run(debug=True)
