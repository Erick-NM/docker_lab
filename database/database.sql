-- ===================================================
-- Script de Base de Datos para MySQL
-- ===================================================

-- Creación de BDD
CREATE DATABASE IF NOT EXISTS directorio_empresa;
USE directorio_empresa;


-- Tabla 'contactos'
CREATE TABLE IF NOT EXISTS contactos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    departamento VARCHAR(100) NOT NULL
);

-- Seed de datos 
INSERT INTO contactos (nombre, telefono, departamento) VALUES
('Juan Pérez', '+593 99 123 4567', 'Tecnología / TI'),
('María López', '+593 98 765 4321', 'Recursos Humanos'),
('Carlos Gómez', '+593 97 112 2334', 'Contabilidad y Finanzas'),
('Ana Martínez', '+593 96 223 3445', 'Marketing y Comunicaciones'),
('David Rodríguez', '+593 95 334 4556', 'Ventas y Comercial'),
('Sofía Morales', '+593 94 445 5667', 'Atención al Cliente'),
('Luis Fernández', '+593 93 556 6778', 'Infraestructura y Cloud'),
('Andrea Castillo', '+593 92 667 7889', 'Legal y Cumplimiento'),
('Jorge Mendoza', '+593 91 778 8990', 'Operaciones y Logística'),
('Elena Torres', '+593 99 889 9001', 'Seguridad de la Información'),
('Mateo Herrera', '+593 98 990 0112', 'Diseño y Experiencia (UI/UX)'),
('Valeria Paredes', '+593 97 001 1223', 'Recursos Humanos'),
('Gabriel Ortiz', '+593 96 112 2335', 'Desarrollo de Software'),
('Camila Salazar', '+593 95 223 3446', 'Auditoría Interna'),
('Felipe Silva', '+593 94 334 4557', 'Compras y Adquisiciones');
