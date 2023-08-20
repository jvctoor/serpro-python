import sqlite3
from user_dao import *
from sql_queries import *

databaseName = "databasev1"

with sqlite3.connect(databaseName) as connection:
    cursor = connection.cursor()

    dao = userDAO(connection)

    print(dao.getUserById(1))
    print(dao.insertUser("Gabriel", "gbressane@hotmail.com", "50196230838"))





