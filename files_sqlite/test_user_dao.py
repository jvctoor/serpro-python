import unittest
from user_dao import userDAO
import sqlite3
from user import *
from sql_queries import *

class UserDAOTest(unittest.TestCase):

    def test_setup_banco(self):
        conn = sqlite3.connect("db-test")
        cursor = conn.cursor()
        cursor.execute(drop_table_user)
        cursor.execute(create_table_user)

    def test_inserir_usuario(self):
        conn = sqlite3.connect("db-test")
        dao = userDAO(conn)
        userInserido = dao.insertUser("João", "joao@gmail.com", "12345678910")
        self.assertEqual(userInserido.get_name(), "João")
        self.assertEqual(userInserido.get_email(), "joao@gmail.com")
        self.assertEqual(userInserido.get_cpf(), "12345678910")





if __name__ == '__main__':
    unittest.main()