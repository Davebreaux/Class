from types import MethodDescriptorType
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.dojo import Dojo

@app.route('/')
def dojo_main():

    return render_template('index.html', dojos = Dojo.get_all_dojos())

@app.route('/new_dojo', methods = ['POST'])
def create_dojo():
    data = {
        "name" : request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect('/')

@app.route('/dojo/<id>')
def show_dojo(id):
    data = {
        "id" : id
    }
    
    return render_template('ninjas.html', ninjas = Dojo.get_ninja(data), dojo = Dojo.get_dojo(data))

@app.route('/add_ninja')
def add_ninja():

    return render_template('add_ninja.html', dojos = Dojo.get_all_dojos())

@app.route('/create_ninja', methods = ['POST'])
def create_ninja():
    data = {
        "dojo_id" : request.form["dojos"],
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"]
    }
    Dojo.create_ninja(data)
    return redirect('/dojo/'+data['dojo_id'])