import MySQLdb
import random

# -----------------------------------------------------------
# Establece la conexión con la base de datos MySQL
# -----------------------------------------------------------
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="NuevaContraseña123",
    db="Unidad4"
)

cursor = db.cursor()

# -----------------------------------------------------------
# Lista de códigos de géneros literarios:
# F - Ficción, N - No Ficción, C - Ciencia, H - Historia,
# R - Romance, A - Aventura, T - Terror, B - Biografía
# -----------------------------------------------------------
generos = ['F', 'N', 'C', 'H', 'R', 'A', 'T', 'B']

# -----------------------------------------------------------
# Componentes lingüísticos para construir títulos ficticios
# -----------------------------------------------------------
articulos = ['El', 'La', 'Los', 'Las', 'Un', 'Una', 'Unos', 'Unas']

sustantivos_sing = [
    'Eco', 'Viaje', 'Destino', 'Laberinto', 'Reino', 'Secreto', 'Códice',
    'Silencio', 'Fuego', 'Amanecer', 'Legado', 'Susurro', 'Oráculo', 'Espejo',
    'Juramento', 'Refugio', 'Despertar', 'Trono', 'Corazón', 'Misterio'
]

sustantivos_plural = [
    'Sombras', 'Almas', 'Estrellas', 'Mentiras', 'Recuerdos', 'Caminos',
    'Voces', 'Cenizas', 'Suspiros', 'Relámpagos', 'Secretos', 'Enigmas',
    'Llamas', 'Visiones', 'Guerreros', 'Espíritus'
]

lugares = [
    'Bosque', 'Abismo', 'Infierno', 'Templo', 'Castillo', 'Océano', 'Cielo',
    'Desierto', 'Montaña', 'Isla', 'Ruina', 'Torre', 'Ciudad', 'Pradera', 'Pantano'
]

adjetivos = [
    'Oscuro', 'Eterno', 'Perdido', 'Prohibido', 'Misterioso', 'Olvidado', 'Sagrado',
    'Maldito', 'Resplandeciente', 'Infinito', 'Roto', 'Tenebroso', 'Sombrío',
    'Encantado', 'Ancestral'
]

# -----------------------------------------------------------
# Listas de nombres y apellidos para autores ficticios
# -----------------------------------------------------------
nombres = [
    'Ana', 'Luis', 'Carlos', 'Elena', 'Marta', 'Jorge', 'Lucía', 'Pedro',
    'Sofía', 'Miguel', 'Laura', 'Andrés', 'Claudia', 'Diego', 'Paula',
    'Antonio', 'Isabel', 'Manuel', 'Valeria', 'David', 'María', 'Fernando',
    'Alejandra', 'Raúl', 'Camila', 'Iván', 'Beatriz', 'Óscar', 'Natalia', 'Rubén'
]

apellidos = [
    'Pérez', 'Gómez', 'Rodríguez', 'López', 'Martínez', 'Hernández', 'Díaz', 'Fernández',
    'Sánchez', 'Ramírez', 'Torres', 'Ruiz', 'Moreno', 'Jiménez', 'Álvarez', 'Romero',
    'Navarro', 'Domínguez', 'Vargas', 'Castro', 'Ortega', 'Silva', 'Ramos', 'Molina'
]

# -----------------------------------------------------------
# Función que genera títulos ficticios con estructuras variadas
# -----------------------------------------------------------
def generar_titulo():
    estructura = random.choice([
        "art_sing sust_sing de sust_sing",
        "art_pl sust_pl de sust_sing",
        "Crónicas de sust_sing",
        "El adj sust_sing",
        "Memorias de un sust_sing",
        "En el lugar",
        "Bajo las sust_pl"
    ])

    if estructura == "art_sing sust_sing de sust_sing":
        return f"{random.choice(['El', 'La', 'Un', 'Una'])} {random.choice(sustantivos_sing)} del {random.choice(sustantivos_sing)}"
    elif estructura == "art_pl sust_pl de sust_sing":
        return f"{random.choice(['Los', 'Las', 'Unos', 'Unas'])} {random.choice(sustantivos_plural)} de {random.choice(sustantivos_sing)}"
    elif estructura == "Crónicas de sust_sing":
        return f"Crónicas de {random.choice(sustantivos_sing)}"
    elif estructura == "El adj sust_sing":
        return f"El {random.choice(adjetivos)} {random.choice(sustantivos_sing)}"
    elif estructura == "Memorias de un sust_sing":
        return f"Memorias de un {random.choice(sustantivos_sing)}"
    elif estructura == "En el lugar":
        return f"En el {random.choice(lugares)}"
    elif estructura == "Bajo las sust_pl":
        return f"Bajo las {random.choice(sustantivos_plural)}"

# -----------------------------------------------------------
# Función que genera nombres de autores ficticios
# -----------------------------------------------------------
def generar_autor():
    return f"{random.choice(nombres)} {random.choice(apellidos)}"

# -----------------------------------------------------------
# Generación de 2000 títulos únicos y ensamblado de registros
# -----------------------------------------------------------
titulos_unicos = set()
libros = []

while len(titulos_unicos) < 2000:
    titulo = generar_titulo()
    if titulo not in titulos_unicos:
        titulos_unicos.add(titulo)
        autor = generar_autor()
        año = random.randint(1900, 2025)
        genero = random.choice(generos)
        libros.append((len(titulos_unicos), titulo, autor, año, genero))

# -----------------------------------------------------------
# Inserción de los registros en la tabla LIBROS de la base de datos
# -----------------------------------------------------------
for libro in libros:
    cursor.execute(
        "INSERT INTO LIBROS (ID_LIBRO, TITULO, AUTOR, AÑO_PUBLICACION, GENERO) VALUES (%s, %s, %s, %s, %s)",
        libro
    )

# -----------------------------------------------------------
# Confirmación de los cambios y cierre de la conexión
# -----------------------------------------------------------
db.commit()
cursor.close()
db.close()
