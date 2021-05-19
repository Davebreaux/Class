from flask_app.config.sqlconnection import connectToMySQL
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.message import Message

@app.route('/messages')
def messages():
    if 'email' not in session:
        flash('You must be logged in to see messages.')
        return redirect('/')
    return render_template('messages.html')

