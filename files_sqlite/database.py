import sqlite3
from user_dao import *
from sql_queries import *

databaseName = "databasev1"

with sqlite3.connect(databaseName) as connection:

    userdao = userDAO(connection)

    print(userdao.getUserByCPF(50196230837))
    #print(userdao.insertUser("Gabriel", "gbressane@hotmail.com", "50196230838"))
    print(userdao.getUserById(2))





