import sqlite3
import random
from database import DB_PATH

def obtener_categorias():
    """
    Devuelve una lista de todas las categorías desde la base de datos.
    """
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute('SELECT id, nombre FROM categorias')
    categorias = cursor.fetchall()  # Devuelve [(id, nombre), ...]
    conexion.close()
    return categorias

def obtener_variantes_por_categoria(categoria_id):
    """
    Devuelve una lista de variantes de búsqueda asociadas a una categoría.
    """
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute('SELECT variante FROM variantes_busqueda WHERE categoria_id = ?', (categoria_id,))
    variantes = [fila[0] for fila in cursor.fetchall()]
    conexion.close()
    return variantes

def obtener_links_por_categoria(categoria_id):
    """
    Devuelve una lista de links de productos asociados a una categoría.
    """
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute('SELECT link FROM productos WHERE categoria_id = ?', (categoria_id,))
    links = [fila[0] for fila in cursor.fetchall()]
    conexion.close()
    return links

def seleccionar_categoria_aleatoria():
    """
    Selecciona aleatoriamente una categoría y devuelve su ID y nombre.
    """
    categorias = obtener_categorias()
    if categorias:
        return random.choice(categorias)  # Devuelve (id, nombre)
    else:
        return None

def seleccionar_variante_aleatoria(categoria_id):
    """
    Selecciona aleatoriamente una variante de búsqueda asociada a una categoría.
    """
    variantes = obtener_variantes_por_categoria(categoria_id)
    if variantes:
        return random.choice(variantes)
    else:
        return None

def seleccionar_link_aleatorio(categoria_id):
    """
    Selecciona aleatoriamente un link de producto asociado a una categoría y devuelve su ID y link.
    """
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute('SELECT id, link FROM productos WHERE categoria_id = ?', (categoria_id,))
    productos = cursor.fetchall()  # Devuelve [(id, link), ...]
    conexion.close()

    if productos:
        return random.choice(productos)  # Devuelve (id, link)
    else:
        return None

