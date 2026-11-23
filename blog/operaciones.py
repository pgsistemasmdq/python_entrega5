# Funciones para listar, buscar y filtrar los posts.

# Muestra el título y el nombre del autor de cada publicación.
def listar_posts(lista):
    if not lista:
        print("No hay publicaciones para mostrar.")
        return

    for post in lista:
        if not isinstance(post, dict):
            print("- Publicación con formato incorrecto.")
            continue

        titulo = post.get("titulo", "Sin título")
        autor = post.get("autor", {})

        if not isinstance(titulo, str) or not titulo.strip():
            titulo = "Sin título"

        if isinstance(autor, dict):
            nombre_autor = autor.get("nombre", "Autor desconocido")
        else:
            nombre_autor = "Autor desconocido"

        estado = post.get("estado", "Sin estado")
        print(f"- {titulo} | Autor: {nombre_autor} | Estado: {estado}")


# Devuelve los posts cuyo título contiene el término buscado.
def buscar_por_titulo(lista, termino):
    resultados = []
    termino = termino.strip().lower()

    if not termino:
        return resultados

    for post in lista:
        if not isinstance(post, dict):
            continue

        titulo = post.get("titulo", "")
        if isinstance(titulo, str) and termino in titulo.lower():
            resultados.append(post)

    return resultados


# Devuelve los posts que contienen el tag solicitado.
def filtrar_por_tag(lista, tag):
    resultados = []
    tag = tag.strip().lower()

    if not tag:
        return resultados

    for post in lista:
        if not isinstance(post, dict):
            continue

        tags = post.get("tags", [])
        if not isinstance(tags, list):
            continue

        for etiqueta in tags:
            if isinstance(etiqueta, str) and etiqueta.lower() == tag:
                resultados.append(post)
                break

    return resultados
