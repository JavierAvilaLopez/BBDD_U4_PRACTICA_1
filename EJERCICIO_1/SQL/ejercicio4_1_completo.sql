-- Ejercicio 1: Creación de base de datos y operaciones sobre la tabla LIBROS

-- a) Crear la base de datos Unidad4
CREATE DATABASE Unidad4;

-- Seleccionar la base de datos
USE Unidad4;

-- b) Crear la tabla LIBROS
CREATE TABLE LIBROS (
    ID_LIBRO INT NOT NULL,
    TITULO VARCHAR(150) NOT NULL,
    AUTOR VARCHAR(100) NOT NULL,
    AÑO_PUBLICACION INT NOT NULL CHECK (AÑO_PUBLICACION <= 2025),
    GENERO VARCHAR(1) NOT NULL
);

-- (La inserción de 2000 registros se realiza desde un script Python auxiliar,
-- por lo que no se incluye aquí. Se verifica posteriormente con SELECT COUNT(*))

-- c) Consulta de libros publicados después del año 2000 con género 'Ficción'
-- representado como 'F'. Se incluye análisis con EXPLAIN.
EXPLAIN
SELECT * FROM LIBROS
WHERE AÑO_PUBLICACION > 2000 AND GENERO = 'F';

-- d) Creación de índice para mejorar rendimiento en la consulta
CREATE INDEX idx_libros_publicacion
ON LIBROS (AÑO_PUBLICACION);

-- Repetir la consulta para verificar mejora en el plan de ejecución
EXPLAIN
SELECT * FROM LIBROS
WHERE AÑO_PUBLICACION > 2000 AND GENERO = 'F';

-- Comprobar existencia del índice creado
SHOW INDEX FROM LIBROS;
