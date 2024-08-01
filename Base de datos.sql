-- Crear la base de datos
CREATE DATABASE proyectoIoT;

-- Usar la base de datos creada
USE proyectoIoT;

-- Crear la tabla usuarios_registrados
CREATE TABLE usuarios_registrados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_tarjeta VARCHAR(255) NOT NULL,
    nombre_usuario VARCHAR(255) NOT NULL,
    fecha_registro DATETIME NOT NULL
);
