from flask import flash
from flask_app.config.sqlconnection import MySQLConnection


class Email:
    def __init__(self, data):
        self.id = data['id']
        self.id = data['email']


    @classmethod
    def add_email(cls, data):
        mysql = MySQLConnection('email_schema')
        query = ("insert into emails (email_address) values (%(email)s)")

        new_email = mysql.query_db(query, data)
        return new_email

    @classmethod
    def get_all(cls):
        mysql = MySQLConnection('email_schema')
        query = ('select * from emails')

        all_emails = mysql.query_db(query)
        return all_emails

    @classmethod
    def is_unique(cls, data):
        is_valid = True
        mysql = MySQLConnection('email_schema')
        query = ("select * from emails where email_address = (%(email)s)")
        test = mysql.query_db(query, data)
        if len(test) > 0:
            is_valid = False
        return is_valid

    @classmethod
    def delete(cls, data):
        mysql = MySQLConnection('email_schema')
        query = ("delete from emails where id = %(id)s")
        mysql.query_db(query, data)
        return None
