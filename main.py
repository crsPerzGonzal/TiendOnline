from fastapi import FastAPI, HTTPException
import mysql.connector
from core.confi import connetion
from models.user import User
app = FastAPI()


@app.get("/")
def read_root():
    return {"hola" : "mundo"}

@app.get("/user")
async def login(dato: User):
    cursor = connetion.cursor(dictionary=True)
    query = "select * from user where Username = %s and password = %s"

    try:
        cursor.execute(query)
        users = cursor.fetchall()
        return users
    except mysql.connector.Error as err: 
        raise HTTPException(status_code=500, detail=f'error al conectar con mysql : {err}')
    finally:
        cursor.close()


