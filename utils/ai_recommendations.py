import cohere
from database.db_config import insert_log

def generate_recommendation(title):
    co = cohere.Client("An1plkGRHSk5uRBTAsHfBLXh6zeDC66ypTATLpRG")
    prompt = (
        f"Escribe una recomendación personal sobre el siguiente producto: {title}. "
        "Haz que parezca que realmente lo has probado o usado. Sé breve, directo y auténtico, como si estuvieras contando tu experiencia a un amigo."
    )
    try:
        response = co.generate(
            model="command-xlarge-nightly",
            prompt=prompt,
            max_tokens=250,
            temperature=0.7
        )
        recommendation = response.generations[0].text.strip()

        # Log de éxito
        insert_log('success', f'Recomendación generada exitosamente para el producto: {title}')
        return recommendation
    except Exception as e:
        # Log de error
        insert_log('error', 'Error al generar recomendación', details=str(e))
        raise  # Relanzar la excepción para que el llamador pueda manejarla
