# Reglas para validar la estructura de las publicaciones.
from blog.datos import estados_post


# Devuelve True si el post es válido o False junto con la causa del error.
def validar_post(post):
    if not isinstance(post, dict):
        return False, "El post no es un diccionario"

    claves_obligatorias = ("id", "titulo", "contenido", "autor", "tags", "estado")

    for clave in claves_obligatorias:
        if clave not in post:
            return False, f'Falta la clave "{clave}"'

    if not isinstance(post["titulo"], str) or not post["titulo"].strip():
        return False, "El título está vacío o es incorrecto"

    if not isinstance(post["contenido"], str) or not post["contenido"].strip():
        return False, "El contenido está vacío o es incorrecto"

    autor = post["autor"]
    if not isinstance(autor, dict):
        return False, "El autor debe ser un diccionario"

    nombre_autor = autor.get("nombre")
    if not isinstance(nombre_autor, str) or not nombre_autor.strip():
        return False, 'Falta el nombre del autor o está vacío'

    if not isinstance(post["tags"], list):
        return False, "Los tags deben estar en una lista"

    for etiqueta in post["tags"]:
        if not isinstance(etiqueta, str):
            return False, "Los tags deben contener textos"

    if post["estado"] not in estados_post:
        return False, "El estado no es válido"

    return True, ""


# Recorre la lista y muestra cuáles publicaciones son válidas.
def validar_todos_los_posts(lista):
    print("\n--- VALIDACIÓN DE POSTS ---")
    numero = 1

    for post in lista:
        es_valido, mensaje = validar_post(post)

        if isinstance(post, dict):
            identificador = post.get("id", numero)
        else:
            identificador = numero

        if es_valido:
            print(f"Post {identificador}: válido")
        else:
            print(f"Post {identificador}: error - {mensaje}")

        numero += 1
