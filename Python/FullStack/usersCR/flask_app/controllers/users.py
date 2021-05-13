from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.config.sqlconnection import connectToMySQL

from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html', users = User.get_all_users())

@app.route('/user_add')
def user_add():
    return render_template('user_add.html')


@app.route('/user/create', methods = ['post'])
def user_create():
    data = {
        "fn": request.form['first_name'],
        "ln": request.form['last_name'],
        "email": request.form['email']
    }

    return redirect('/user/show/'+ str(User.user_create(data)))

@app.route('/user/update', methods = ['post'])
def user_data_update():
        data = {
        "fn": request.form['first_name'],
        "ln": request.form['last_name'],
        "email": request.form['email'],
        "id": request.form['id']
        }
        User.user_data_update(data)
        return redirect('/')

@app.route('/user/delete/<id>')
def user_data_delete(id):
    data = {
        "id": id
    }
    User.user_data_delete(data)
    return redirect('/')

@app.route('/user/show/<id>')
def user_show(id):
    data = {
        "id": id
    }
    users = User.user_show(data)
    return render_template('show_user.html', users = users)

@app.route('/user/update/<id>')
def user_update(id):
    data = {
        "id": id
    }
    users = User.user_update(data)
    return render_template('update_user.html', users = users)
