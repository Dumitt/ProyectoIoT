import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector
from datetime import datetime
import time

# Configuración de GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Configuración del lector RFID
reader = SimpleMFRC522()

# Configuración del servo motor
SERVO_PIN = 17
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz
pwm.start(0)

def move_servo():
    # Mueve el servo de 180 a 80 grados
    time.sleep(2)  # Pequeña pausa para asegurar el movimiento final
    set_servo_angle(180)
    set_servo_angle(80)
    time.sleep(5)  # Espera 5 segundos en 90 grados
    # Regresa el servo a 180 grados
    set_servo_angle(180)


def set_servo_angle(angle):
    duty_cycle = (angle / 18) + 2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Tiempo suficiente para mover el servo
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

# Configuración de la base de datos
db_connection = mysql.connector.connect(
    host="localhost",
    user="dumit",
    passwd="qwerty",
    database="proyectoIoT"
)
cursor = db_connection.cursor()

scan_count = 0
max_scans = 1

try:
    while scan_count < max_scans:
        print("Esperando a que se acerque una tarjeta...")
        try:
            id, text = reader.read()
            print("ID de la tarjeta: ", id)
            print("Contenido de la tarjeta: ", text)

            hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            cursor.execute("SELECT COUNT(*) FROM usuarios_registrados WHERE id_tarjeta = %s", (id,))
            result = cursor.fetchone()

            if result[0] > 0:
                print("ACCESO PERMITIDO")
                insert_query = "INSERT INTO historial_tarjetas (id_tarjeta, hora_escaneo) VALUES (%s, %s)"
                insert_values = (id, hora_actual)
                cursor.execute(insert_query, insert_values)
                db_connection.commit()

                # Mueve el servo motor de 180 a 80 grados, espera y luego regresa a 180 grados
                move_servo()
            else:
                print("ACCESO DENEGADO")

            print(f"Tarjeta escaneada a las {hora_actual}. Historial registrado.")
        except Exception as e:
            print(f"Error al leer la tarjeta: {e}")

        scan_count += 1

finally:
    # Detén el PWM y limpia los recursos
    pwm.stop()
    GPIO.cleanup()
    cursor.close()
    db_connection.close()
