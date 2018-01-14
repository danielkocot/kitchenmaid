from flask import render_template, flash, redirect, url_for

from app import app, db
from app.forms import NewForm
from app.models import Grocery


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    groceries = Grocery.query.all()
    return render_template('list.html', groceries=groceries)

@app.route('/new', methods=['GET','POST'])
def new():
    form = NewForm()
    if form.validate_on_submit():
        grocery = Grocery(name=form.name.data, stock=form.stock.data, best_before=form.best_before_date.data)
        db.session.add(grocery)
        db.session.commit()
        flash('Congrats, the Grocery is added')
        return redirect(url_for('new'))
    return render_template('new.html', form=form)

@app.route('/edit/<id>', methods=['GET','POST'])
def edit(id):
    pass

@app.route('/delete/<id>', methods=['GET','POST'])
def delete():
    pass

@app.route('/add/<id>', methods=['GET','POST'])
def add(id):
    grocery = Grocery.query.get(id)
    grocery.stock += 1
    db.session.commit()
    return redirect(url_for('list'))

@app.route('/take/<id>', methods=['GET','POST'])
def take(id):
    grocery = Grocery.query.get(id)
    grocery.stock -= 1
    db.session.commit()
    return redirect(url_for('list'))