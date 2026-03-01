import mysql.connector

def obtener_conexion():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # En XAMPP normalmente está vacío
        database="biblioteca"
    )
    return conexion