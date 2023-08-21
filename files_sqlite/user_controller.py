from fastapi import *
from user_dao import userDAO
import sqlite3

router = APIRouter()


@router.get("/users")
def getAllUsers():
    dao = userDAO(sqlite3.connect("db-homolog"))
    return dao.getAllUsers()

@router.post("/users/")
def postUser(data: dict):
    dao = userDAO(sqlite3.connect("db-homolog"))
    return dao.insertUser(data.get("name", None), data.get("email", None), data.get("cpf", None))
