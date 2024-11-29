from amazon import obtener_titulo_producto_amazon
from ai_recommendations import generate_recommendation
from youtube import search_and_play_youtube_video
from categories import (
    seleccionar_categoria_aleatoria,
    seleccionar_variante_aleatoria,
    seleccionar_link_aleatorio
)
from database import inicializar_db

inicializar_db()

# Selección aleatoria de categoría
categoria = seleccionar_categoria_aleatoria()
if categoria:
    categoria_id, categoria_nombre = categoria

    # Selección aleatoria de variante
    search_variant = seleccionar_variante_aleatoria(categoria_id)

    # Selección aleatoria de link y producto ID
    link_data = seleccionar_link_aleatorio(categoria_id)
    if link_data:
        producto_id, selected_link = link_data

        if search_variant:
            # Obtener el título del producto
            titulo_producto = obtener_titulo_producto_amazon(selected_link)

            # Generar comentario con Cohere
            try:
                recommendation = generate_recommendation(titulo_producto)
                print(f"Comentario generado:\n{recommendation}")

                # Publicar comentario en YouTube
                search_and_play_youtube_video(search_variant, recommendation, producto_id, categoria_id, selected_link)
            except Exception as e:
                print("Error al generar recomendación:", e)
        else:
            print("No se encontraron variantes para la categoría seleccionada.")
    else:
        print("No se encontraron productos para la categoría seleccionada.")
else:
    print("No hay categorías disponibles en la base de datos.")