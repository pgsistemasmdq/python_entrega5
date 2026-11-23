# ---------------------------------------------
# Preentrega 5: Organización modular del blog
# ---------------------------------------------

# Conservamos las estructuras de datos de las entregas anteriores.
perfil_autor = {
    "nombre": "Carlos Mendoza",
    "bio": "Ingeniero de Software y apasionado por la inteligencia artificial y la ciencia de datos.",
    "especialidad": "Data Science y Machine Learning",
    "redes_sociales": ["@carlos_ai", "@cmendoza_dev", "@carlos_tech"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"Python", "AI", "Data Science", "Machine Learning", "Pandas", "Deep Learning"}

# Lista de publicaciones del blog.
posts = [
    {
        "id": 1,
        "titulo": "Introducción a la Ciencia de Datos con Python",
        "contenido": "En este artículo exploramos las librerías fundamentales de Python para el análisis de datos como Pandas y NumPy.",
        "autor": perfil_autor,
        "categoria": "Ciencia de Datos",
        "tags": ["Python", "Data Science"],
        "estado": estados_post[1]
    },
    {
        "id": 2,
        "titulo": "Construyendo tu primer modelo de Machine Learning",
        "contenido": "Guía paso a paso para entrenar un modelo de clasificación con Scikit-Learn de manera sencilla.",
        "autor": perfil_autor,
        "categoria": "Inteligencia Artificial",
        "tags": ["Machine Learning", "AI", "Python"],
        "estado": estados_post[0]
    },
    {
        "id": 3,
        "titulo": "Limpieza y preparación de datos sin morir en el intento",
        "contenido": "Estrategias efectivas para tratar datos nulos y valores atípicos en tus datasets usando Pandas.",
        "autor": perfil_autor,
        "categoria": "Análisis de Datos",
        "tags": ["Python", "Pandas", "Data Science"],
        "estado": estados_post[2]
    },
    {
        "id": 4,
        "titulo": "Redes Neuronales desde Cero con Python",
        "contenido": "Una introducción conceptual y matemática a los fundamentos del Deep Learning y la Inteligencia Artificial.",
        "autor": perfil_autor,
        "categoria": "Inteligencia Artificial",
        "tags": ["Deep Learning", "AI", "Python"],
        "estado": estados_post[1]
    },
    {
        "id": 5,
        "titulo": "Visualización de Datos Impactante",
        "contenido": "Aprende a comunicar hallazgos complejos a través de gráficos estadísticos claros y profesionales.",
        "autor": perfil_autor,
        "categoria": "Visualización",
        "tags": ["Data Science", "Python"],
        "estado": estados_post[1]
    },
    {
        # Este post tiene un error intencional para probar la validación.
        "id": 6,
        "titulo": "Primeros pasos con Inteligencia Artificial",
        "autor": perfil_autor,
        "categoria": "Inteligencia Artificial",
        "tags": ["AI", "Python"],
        "estado": estados_post[0]
        # Falta la clave "contenido".
    }
]
