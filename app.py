from flask import Flask, render_template, url_for, redirect, request, Response, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_of_the_work.db'
db = SQLAlchemy(app)


class Arcticle(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, autoincrement=True)

    def __repr__(self):
        return '<Arcticle %r>' % self.id


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/posts')
def posts():
    posts_ = Arcticle.query.all()
    return render_template('posts.html', posts=posts)


@app.route('/email')
def email():
    return render_template('email.html')


@app.route('/mail_uber')
def mail_uber():
    return render_template('letter_example_1.html')


@app.route("/mail_other")
def mail_other():
    return render_template("letter_example_2.html")


@app.route("/mail_new")
def mail_new():
    return render_template("letter_example_3.html")


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        post_ = Arcticle(title=title, text=text)

        try:
            db.session.add(post_)
            db.session.commit()
            return redirect('/')

        except:
            return "При добавлении статьи произошла ошибка"

    else:
        return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)
