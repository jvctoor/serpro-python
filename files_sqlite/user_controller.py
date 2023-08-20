from fastapi import *
from user_dao import userDAO
import sqlite3

router = APIRouter()

@router.get("/users")
def getAllUsers():
    dao = userDAO(sqlite3.connect("db-homolog"))
    return dao.getAllUsers()

