from flask_app.config.sqlconnection import connectToMySQL
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        flash('You must be logged in to view this page.')
        return redirect('/')
    data = {
        "user_id" : session['user_id']
    }
    recipes = Recipe.get_all(data)
    return render_template('dashboard.html', recipes = recipes)


@app.route('/new_recipe')
def new_recipe():
    if 'email' not in session:
        flash('You must be logged in to view this page.')
        return redirect('/')
    
    return render_template('new_recipe.html')

@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    if 'email' not in session:
        flash('You must be logged in to view this page.')
        return redirect('/')
    if not Recipe.validate(request.form):
        return redirect('/new_recipe')
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "cook_time" : request.form['cook_time'],
        "user_id" : session['user_id']
    }
    
    recipe = Recipe.create(data)
    return redirect('/dashboard')


@app.route('/instructions/<int:id>/view')
def view_recipe(id):
    if 'email' not in session:
        flash('You must be logged in to view this page.')
        return redirect('/')
    data = {
        "id" : id
    }
    recipe = Recipe.view_recipe(data)
    return render_template('view_recipe.html', recipe = recipe)

@app.route('/recipe/<int:id>/edit')
def edit_recipe(id):
    if 'email' not in session:
        flash('You must be logged in to view this page.')
        return redirect('/')
    data = {
        "id" : id
    }
    recipe = Recipe.view_recipe(data)
    return render_template('edit_recipe.html', recipe = recipe)

@app.route('/change_recipe', methods=['POST'])
def change_recipe():
    if 'email' not in session:
        flash('You must be logged in to view this page.')
        return redirect('/')
    if not Recipe.validate(request.form):
        return redirect(f"/recipe/{request.form['recipe_id']}/edit")
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "cook_time" : request.form['cook_time'],
        "user_id" : session['user_id'],
        "recipe_id" : request.form['recipe_id']
    }
    
    recipe = Recipe.edit(data)
    return redirect('/dashboard')


@app.route('/recipe/<int:id>/delete')
def delete_recipe(id):
    if 'email' not in session:
        flash('You must be logged in to view this page.')
        return redirect('/')
    data = {
        "id" : id
    }
    Recipe.delete(data)
    return redirect('/dashboard')