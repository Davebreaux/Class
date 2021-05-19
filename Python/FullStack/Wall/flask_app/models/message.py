from flask import flash
from flask_app.config.sqlconnection import MySQLConnection

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.contents = data['contents']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.sender_id = data['sender_id']

    