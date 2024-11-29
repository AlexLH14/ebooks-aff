from insert_data import insertar_categoria, insertar_variante, insertar_producto
from categories import obtener_categorias, obtener_variantes_por_categoria, obtener_links_por_categoria
import sqlite3
from database import DB_PATH, inicializar_db, obtener_comentarios


# Inicializar la base de datos y crear las tablas si no existen
'''
inicializar_db()
print("Base de datos y tablas inicializadas correctamente.")
'''

'''
# Conectar a la base de datos
conexion = sqlite3.connect(DB_PATH)
cursor = conexion.cursor()

# Mostrar las tablas creadas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()
conexion.close()

print("Tablas creadas:", tablas)
'''

#CATEGORIAS
#1 smartphones
#2 tenis


#INSERTAR DATOS SI NO EXISTEN USANDO LAS FUNCIONES DE INSERT_DATA
#'''
#insertar_categoria("tenis")
#insertar_variante("mejores tenis", 2)  # ID de la categoría
#insertar_producto("", 2)  # ID de la categoría
#'''


#VERIFICAR DATOS INSERTADOS
#'''
# Verificar categorías
print("Categorías:", obtener_categorias())

# Verificar variantes de búsqueda
print("Variantes de búsqueda:", obtener_variantes_por_categoria(1))  # 1: ID de la categoría "smartphones"

# Verificar productos
print("Productos:", obtener_links_por_categoria(1))  # 1: ID de la categoría "smartphones"
#'''


# Obtener y mostrar los comentarios
comentarios = obtener_comentarios()
print("Comentarios registrados:")
for comentario in comentarios:
    video_url = f"https://www.youtube.com/watch?v={comentario[4]}"  # Construir el link completo del video
    print(f"ID: {comentario[0]}")
    print(f"Comentario: {comentario[1]}")
    print(f"Producto: {comentario[2]}")
    print(f"Categoría: {comentario[3]}")
    print(f"Video ID: {comentario[4]}")
    print(f"Timestamp: {comentario[5]}")
    print(f"Video URL: {video_url}")  # Mostrar el link del video
    print("-" * 40)