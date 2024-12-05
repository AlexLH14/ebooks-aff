import sqlite3
from db_config import DB_PATH

def insert_category(nombre):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    try:
        cursor.execute('INSERT INTO categorias (nombre) VALUES (?)', (nombre,))
        conexion.commit()
    except sqlite3.IntegrityError:
        print(f"La categoría '{nombre}' ya existe.")
    conexion.close()

def insert_variant(variante, categoria_id):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO variantes_busqueda (variante, categoria_id) VALUES (?, ?)', (variante, categoria_id))
    conexion.commit()
    conexion.close()

def insert_product(link, categoria_id):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    try:
        cursor.execute('INSERT INTO productos (link, categoria_id) VALUES (?, ?)', (link, categoria_id))
        conexion.commit()
    except sqlite3.IntegrityError:
        print(f"El producto '{link}' ya existe.")
    conexion.close()
