from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']

    @classmethod
    def get_all_dojos(cls):
        mysql = connectToMySQL('dojos_and_ninjas_schema')
        dojos = mysql.query_db('select * from dojos')

        results = []

        for dojo in dojos:
            results.append(cls(dojo))
        
        return results

    @classmethod
    def create_dojo(cls, data):
        mysql = connectToMySQL('dojos_and_ninjas_schema')
        query = ('insert into dojos (name) values (%(name)s);')

        new_dojo = mysql.query_db(query, data)
        return new_dojo

    @classmethod
    def get_ninja(cls, data):
        mysql = connectToMySQL('dojos_and_ninjas_schema')
        query = ('select * from ninjas where ninjas.dojo_id = (%(id)s);')
        result = mysql.query_db(query, data)
        return result

    @classmethod
    def get_dojo(cls, data):
        mysql = connectToMySQL('dojos_and_ninjas_schema')
        query = ('select * from dojos where id = (%(id)s);')
        result = mysql.query_db(query, data)
        return result

    @classmethod
    def create_ninja(cls, data):
        mysql = connectToMySQL('dojos_and_ninjas_schema')
        query = ('insert into ninjas (first_name, last_name, age, dojo_id) values (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);')

        new_ninja =mysql.query_db(query, data)
        return new_ninja