import cohere

def generate_recommendation(title):
    co = cohere.Client("An1plkGRHSk5uRBTAsHfBLXh6zeDC66ypTATLpRG")
    prompt = (
        f"Escribe una recomendación personal sobre el siguiente producto: {title}. "
        "Haz que parezca que realmente lo has probado o usado. Sé breve, directo y auténtico, como si estuvieras contando tu experiencia a un amigo."
    )
    response = co.generate(
        model="command-xlarge-nightly",
        prompt=prompt,
        max_tokens=250,
        temperature=0.7
    )
    return response.generations[0].text.strip()
