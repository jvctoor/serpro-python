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
        self.connection.commit()
        return User(result[1], result[2], result[3])

    def insertUser(self, name, email, cpf):
        query = "INSERT INTO user(name, email, cpf) VALUES(?, ?, ?)"
        self.cursor.execute(query, (name, email, cpf))
        result = self.cursor.rowcount
        if result > 0:
            self.connection.commit()
            return User(name, email, cpf)




