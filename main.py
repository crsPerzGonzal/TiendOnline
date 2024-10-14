from fastapi import FastAPI, HTTPException
import mysql.connector
from backend.core.confi import get_connetion
from backend.models.user import User


app = FastAPI()


@app.get("/")
def read_root():
    return {"hola" : "mundo"}

@app.post("/users")
async def get_user_info(user: User):
    connection = get_connetion()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE username = %s AND password_hash = %s"
    
    try:
        cursor.execute(query, (user.username, user.password_hash))
        user_result = cursor.fetchone()
        
        if user_result:
            return user_result  # Devuelve la información del usuario
        else:
            raise HTTPException(status_code=404, detail="Usuario no encontrado o contraseña incorrecta.")
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f'Error al conectar con MySQL: {err}')
    finally:
        cursor.close()
        connection.close()
