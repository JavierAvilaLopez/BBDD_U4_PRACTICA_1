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