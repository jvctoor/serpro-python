import sqlite3
from user_dao import *
from sql_queries import *
from fastapi import *
from user_controller import router as user_controller
databaseName = "db-homolog"

app = FastAPI()
app.include_router(user_controller)

with sqlite3.connect(databaseName) as connection:

    cursor = connection.cursor()
    cursor.execute(drop_table_user)
    cursor.execute(create_table_user)

    userdao = userDAO(connection)

    userdao.insertUser("Alice", "alice@example.com", "12345678901")
    userdao.insertUser("Carlos", "carlos@example.com", "98765432109")
    userdao.insertUser("Mariana", "mariana@example.com", "56789012345")
    userdao.insertUser("Eduardo", "eduardo@example.com", "45678901234")
    userdao.insertUser("Isabela", "isabela@example.com", "67890123456")
    userdao.insertUser("André", "andre@example.com", "78901234567")
    userdao.insertUser("Sofia", "sofia@example.com", "89012345678")
    userdao.insertUser("Pedro", "pedro@example.com", "23456789012")
    userdao.insertUser("Larissa", "larissa@example.com", "34567890123")
    userdao.insertUser("Gabriel", "gabriel@example.com", "45678901235")

    print(userdao.getAllUsers())

