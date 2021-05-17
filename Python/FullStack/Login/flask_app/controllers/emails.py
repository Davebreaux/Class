from flask_app.config.sqlconnection import connectToMySQL
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.email import Email
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add_email', methods=['POST'])
def add_email():
    if not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address")
            return redirect('/')
    
    data = {
        "email" : request.form['email']
    }
    if not Email.is_unique(data):
        flash("Email address already in use.")
        return redirect('/')
    
    Email.add_email(data)
    flash(f"The email you created {data['email']} is valid!")
    return redirect('/success')

@app.route('/success')
def success():
    emails = Email.get_all()
    return render_template('success.html', emails = emails)


@app.route('/delete/<id>')
def delete(id):
    data = {
        "id" : id
    }
    Email.delete(data)
    return redirect('/success')