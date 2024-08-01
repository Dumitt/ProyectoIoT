# ProyectoIoT
# Proyecto de Registro de Ingresos mediante identificación por RFID 


OBJETIVOS GENERALES
- Desarrollar un prototipo de registros de ingreso por caseta a estudiantes de una universidad obteniendo el id que ingresa; y la fecha y hora que lo hace, almacenándolo en una base de datos para tener un historial de entradas y salidas garantizando la seguridad de accesos y denegando el ingreso a tarjetas no registradas o que intenten ingresar dos veces sin haber registrado la salida previamente, esto para garantizar el denegar el acceso a tarjetas que pudiesen haber sido clonadas


DESCRIPCION DEL PROYECTO
- Este proyecto utiliza un lector RFID RC522 para leer las tarjetas utilizando la librería SimpleMFRC522 y, por medio de un código en Python se comprueba si la tarjeta leída esta previamente registrada o no; en caso de estar registrada manda a la base de datos subida en un servidor local el registro de ingreso para así generar un historial 

OBJETIVOS ESPECIFICOS DEL PROYECTO
- Comprobar y registrar en un historial los ingresos a la universidad  
- Hacer mas seguros los ingresos, y denegar el acceso a personas no autorizadas

COMPONENTES UTILIZADOS
- 1 Raspberry Pi4
- 1 Servomotor SG90
- Jumps hembra a macho
- Jumps macho a macho
- 1 Lector RFID RC522
- 1 Protoboard
- 1 Extensor de puertos GPIO

LIBRERÍAS UTILIZADAS
- RPi.GPIO 
// Utilizada para controlar los pines GPIO de una Raspberry Pi.

- mfrc522.SimpleMFRC522 
// Una biblioteca específica para interactuar con el lector RFID RC522.

- mysql.connector 
// Utilizado para conectarse y realizar operaciones con una base de datos MySQL.

- datetime 
// Proporciona clases para manipular fechas y horas.

- time 
// Proporciona varias funciones relacionadas con el tiempo, como pausas y medición de tiempo.


CONEXIONES FISICAS EN LOS MODULOS Y LA RASPBERRY PI 4
RFID RC522
SDA - Pin físico 24
SCK - Pin físico 23
MOSI - Pin físico 19
MISO - Pin físico 21
RST - Pin físico 22
VCC (3.3V) - Pin físico 17
GND - Pin físico 20

Servomotor SG90
Señal (GPIO 11) - Pin físico 23
VCC (5V) - Pin físico 2
GND - Pin físico 6




CONFIGURACIÓN DEL ENTORNO
# Actualizar los paquetes del sistema:
#sudo apt update
#sudo apt upgrade

# Instala Apache2
#sudo apt install apache2

# Configura Apache2 para que se inicie automáticamente
#sudo systemctl enable apache2

# Instalar el servidor de MariaDB
#sudo apt install mariadb-server

# Iniciar el servicio de MariaDB
#sudo systemctl start mariadb

# Habilitar MariaDB para que se inicie automaticamente al iniciar el sistema
#sudo systemctl enable mariadb

# Configurar la seguridad de MariaDB
#sudo mysql_secure_installation

# Acceder a la consola de MariaDB
#sudo mysql -u root -p



CONFIGURACION DEL ENTORNO GRAFICO DE LA BDD
# Instala phpMyAdmin
#sudo apt install phpmyadmin

# Configura Apache2 para que incluya phpMyAdmin
#sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin

# Habilitar acceso remoto en MariaDB
#sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf

# Encuentra la linea bind-address y cambiala por esto:
bind-address = 0.0.0.0

# Guarda el archivo y reinicia MariaDB
#sudo systemctl restart mariadb

# Concede permisos para que MariaDB puedo conectarse de cualquier host
GRANT ALL PRIVILEGES ON *.* TO 'usuario'@'%' IDENTIFIED BY 'contraseña';
FLUSH PRIVILEGES;

CONFIGURACION DEL ENTORNO VIRTUAL
# Instala Python3
#sudo apt install python3

# Instala venv
#sudo apt install python3-venv

# Crea un entorno virtual
#python3 -m venv nombre_del_entorno

# Activa el entorno virtual
#source nombre_del_entorno/bin/activate


Este proyecto fue realizado en el marco del curso IoT Essentials Developer impartido por [Codigo IoT ](https://www.codigoiot.com/) y organizado por la [Asociación Mexicana del Internet de las Cosas](https://www.asociacioniot.org/).
