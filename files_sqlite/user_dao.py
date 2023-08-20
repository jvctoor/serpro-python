from typing import List

from user import *
import sqlite3


class userDAO:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def getUserById(self, id: int) -> User:
        query = "SELECT * FROM user WHERE id = ?"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        self.connection.commit()
        return User(result[1], result[2], result[3])

    def getAllUsers(self) -> List[User]:
        query = "SELECT * FROM user;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getUserByCPF(self, cpf: str) -> User:
        query = "SELECT * FROM user WHERE cpf = ?"
        self.cursor.execute(query, (cpf,))
        result = self.cursor.fetchone()
        self.connection.commit()
        return User(result[1], result[2], result[3])

    def insertUser(self, name: str, email: str, cpf: str) -> User:
        query = "INSERT INTO user(name, email, cpf) VALUES(?, ?, ?)"
        self.cursor.execute(query, (name, email, cpf))
        result = self.cursor.rowcount
        if result > 0:
            self.connection.commit()
            return User(name, email, cpf)

    def atualizarUserById(self, id: int, name: str, email: str, cpf: str) -> User:
        query = "UPDATE user SET name = ?, email = ?, cpf = ? WHERE id = ?"
        self.cursor.execute(query, (name, email, cpf, id))
        result = self.cursor.rowcount
        if result > 0:
            self.connection.commit()
            return User(name, email, cpf)

    def atualizarUserByCPF(self, cpf: str, name: str, email: str) -> User:
        query = "UPDATE user SET name = ?, email = ? WHERE cpf = ?"
        self.cursor.execute(query, (name, email, cpf))
        result = self.cursor.rowcount
        if result > 0:
            self.connection.commit()
            return User(name, email, cpf)

    def deleteUserById(self, id: int) -> bool:
        query = "DELETE FROM user WHERE id = ?"
        self.cursor.execute(query, (id,))
        result = self.cursor.rowcount
        if result > 0:
            self.connection.commit()
            return True
        else:
            return False









