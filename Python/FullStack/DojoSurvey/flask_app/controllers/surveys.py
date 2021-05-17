from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.config.sqlconnection import connectToMySQL

from flask_app.models.survey import Survey

@app.route('/')
def dojo_survey():

    return render_template('index.html')

@app.route('/survey', methods=["POST"])
def survey_done():
    if not Survey.validate(request.form):
        return redirect('/')
    print(request.form)
    data = {
    "name" : request.form['name'],
    "location" : request.form['location'],
    "language" : request.form['favorite_language'],
    "comments" : request.form['comments']
    }
    Survey.survey(data)
    return render_template('survey.html', name = data['name'], location = data['location'], favorite_language = data['language'], comments = data['comments'])

