from flask_app.config.sqlconnection import connectToMySQL
from flask import flash


class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name']) < 2:
            flash("Name must be at least 2 characters long.")
            is_valid = False
        if len(data['location']) < 3:
            flash("Location must be at least 3 characters long.")
            is_valid = False
        return is_valid

    @classmethod
    def survey(cls, data):
        mysql = connectToMySQL('dojo_survey')
        query = ('insert into survey (name, location, language, comments) values (%(name)s, %(location)s, %(language)s, %(comments)s)')
        new_survey = mysql.query_db(query, data)
        return new_survey