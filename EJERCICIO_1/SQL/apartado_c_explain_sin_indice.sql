-- c) Consulta de libros publicados después del año 2000 con género 'Ficción'
-- representado como 'F'. Se incluye análisis con EXPLAIN.
EXPLAIN
SELECT * FROM LIBROS
WHERE AÑO_PUBLICACION > 2000 AND GENERO = 'F';