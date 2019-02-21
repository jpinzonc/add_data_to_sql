from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('hello.cfg')
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column('todo_id', db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    text = db.Column(db.String)
    done = db.Column(db.Boolean)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False
        self.pub_date = datetime.utcnow()

class Album(db.Model):
    """"""
    __tablename__ = "albums"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.String)
    Price = db.Column(db.String)
    Competitors_name = db.Column(db.String)

@app.route('/')
def show_all():
    return render_template('show_all.html',
        todos=Album.query.order_by(Album.release_date.desc()).all()
    )

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['title']:
            flash('Title is required', 'error')
        elif not request.form['Price']:
            flash('Text is required', 'error')
        else:
            todo = Album(request.form['title'], request.form['Price'])
            db.session.add(todo)
            db.session.commit()
            flash(u'Todo item was successfully created')
            return redirect(url_for('show_all'))
    return render_template('new.html')


@app.route('/update', methods=['POST'])
def update_done():
    for todo in Album.query.all():
        todo.done = ('done.%d' % todo.id) in request.form
    flash('Updated status')
    db.session.commit()
    return redirect(url_for('show_all'))


if __name__ == '__main__':
    app.run()
