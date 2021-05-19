from flask import flash
from flask_app.config.sqlconnection import MySQLConnection

class Recipe:
    def __init__(self, data):
        self.id = int(data['id'])
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.cook_time = data['cook_time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name']) < 3:
            is_valid = False
            flash('Name must be at least 3 characters')
        if len(data['description']) < 3:
            is_valid = False
            flash('Description must be at least 3 characters')
        if len(data['instructions']) < 3:
            is_valid = False
            flash('Instructions must be at least 3 characters')
        return is_valid

    @classmethod
    def create(cls, data):
        mysql = MySQLConnection('recipe_schema')
        query = ("insert into recipes (name, description, instructions, cook_time, user_id) values (%(name)s, %(description)s, %(instructions)s, %(cook_time)s, %(user_id)s)")

        recipe = mysql.query_db(query, data)
        return recipe

    @classmethod
    def get_all(cls, data):
        mysql = MySQLConnection('recipe_schema').query_db('select * from recipes where recipes.user_id = %(user_id)s', data)
        recipes = []
        for item in mysql:
            new = Recipe(item)
            recipes.append(new)
        return recipes

    @classmethod
    def view_recipe(cls, data):
        
        mysql = MySQLConnection('recipe_schema').query_db('select * from recipes where recipes.id = %(id)s', data)

        print(mysql)
        recipe = Recipe(mysql[0])
        return recipe

    @classmethod
    def edit(cls, data):
        mysql = MySQLConnection('recipe_schema')
        query = ("update recipes set name = %(name)s, description = %(description)s, instructions = %(instructions)s, cook_time = %(cook_time)s where id = %(recipe_id)s;")

        recipe = mysql.query_db(query, data)
        return recipe

    @classmethod
    def delete(cls, data):
        MySQLConnection('recipe_schema').query_db('delete from recipes where recipes.id = %(id)s', data)
