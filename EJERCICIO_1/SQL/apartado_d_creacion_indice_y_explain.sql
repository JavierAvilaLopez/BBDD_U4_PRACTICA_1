-- d) Creación de índice para mejorar rendimiento en la consulta
CREATE INDEX idx_libros_publicacion
ON LIBROS (AÑO_PUBLICACION);

-- Repetir la consulta para verificar mejora en el plan de ejecución
EXPLAIN
SELECT * FROM LIBROS
WHERE AÑO_PUBLICACION > 2000 AND GENERO = 'F';

-- Comprobar existencia del índice creado
SHOW INDEX FROM LIBROS;
