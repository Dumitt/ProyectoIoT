import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector
from datetime import datetime

# Configurar el lector RFID
reader = SimpleMFRC522()

# Conexión a la base de datos
db_connection = mysql.connector.connect(
    host="localhost",
    user="dumit",
    passwd="qwerty",
    database="proyectoIoT"
)
cursor = db_connection.cursor()

try:
    print("Acerca una tarjeta para registrarla...")
    id, text = reader.read()
    print("ID de la tarjeta: ", id)
    
    # Pedir el nombre del usuario
    nombre_usuario = input("Introduce el nombre del usuario: ")
    
    # Fecha de registro
    fecha_registro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Insertar el nuevo usuario en la base de datos
    insert_query = "INSERT INTO usuarios_registrados (id_tarjeta, nombre_usuario, fecha_registro) VALUES (%s, %s, %s)"
    insert_values = (id, nombre_usuario, fecha_registro)
    cursor.execute(insert_query, insert_values)
    db_connection.commit()
    
    print("Tarjeta registrada correctamente.")
    print(f"ID de la tarjeta: {id}")
    print(f"Nombre del usuario: {nombre_usuario}")
    print(f"Fecha de registro: {fecha_registro}")

finally:
    GPIO.cleanup()
    cursor.close()
    db_connection.close()
