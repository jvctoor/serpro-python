from user import *
import sqlite3

class userDAO:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def getUserById(self, id):
        query = "SELECT * FROM user WHERE id = ?"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        return User(result[1], result[2], result[3])






