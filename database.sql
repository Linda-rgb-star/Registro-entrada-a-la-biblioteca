-- ============================================
-- CREAR BASE DE DATOS
-- ============================================

CREATE DATABASE IF NOT EXISTS biblioteca;
USE biblioteca;

-- ============================================
-- TABLA USUARIOS
-- ============================================

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    identificacion VARCHAR(50) NOT NULL UNIQUE,
    huella_registrada BOOLEAN DEFAULT 0,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- TABLA LOCKERS
-- ============================================

CREATE TABLE IF NOT EXISTS lockers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero INT NOT NULL UNIQUE,
    disponible BOOLEAN DEFAULT 1
);

-- ============================================
-- TABLA ASIGNACIONES
-- ============================================

CREATE TABLE IF NOT EXISTS asignaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    locker_id INT NOT NULL,
    fecha_asignacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_liberacion TIMESTAMP NULL,

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (locker_id) REFERENCES lockers(id)
);

-- ============================================
-- INSERTAR LOCKERS INICIALES
-- ============================================

INSERT INTO lockers (numero, disponible) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 1),
(11, 1),
(12, 1),
(13, 1),
(14, 1),
(15, 1),
(16, 1),
(17, 1),
(18, 1),
(19, 1),
(20, 1);
