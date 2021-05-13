from flask_app.config.sqlconnection import connectToMySQL

class User:
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    
    def get_all_users(cls):
        mysql = connectToMySQL('users_schema')
        users = mysql.query_db('select * from users')

        results = []
        for user in users:
            results.append(cls(user))
        
        return results

    @classmethod
    
    def user_create(cls, data):
        mysql = connectToMySQL('users_schema')
        query = query =('insert into users (first_name, last_name, email) values (%(fn)s, %(ln)s, %(email)s )')
        new_user = mysql.query_db(query, data)

        return new_user

    @classmethod
    def user_data_update(cls, data):
        mysql = connectToMySQL('users_schema')
        query =('update users set first_name = %(fn)s, last_name = %(ln)s, email = %(email)s where id = %(id)s;')
        new_user = mysql.query_db(query, data)
        return new_user

    @classmethod
    def user_data_delete(cls, data):
        mysql = connectToMySQL('users_schema')
        query =('delete from users where id = %(id)s;')
        mysql.query_db(query, data)
        return None

    @classmethod
    def user_show(cls, data):
        mysql = connectToMySQL('users_schema')
        query = ('select * from users where id = %(id)s;')
        users = mysql.query_db(query, data)
        return users

    @classmethod
    def user_update(cls, data):
        mysql = connectToMySQL('users_schema')
        query = ('select * from users where id = %(id)s;')
        users = mysql.query_db(query, data)
        return users

