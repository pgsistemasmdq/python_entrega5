# Preentrega 5: Organización modular del blog.
# Este archivo inicia el sistema y coordina sus funciones.

from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_todos_los_posts


def main():
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            print("\nPosts disponibles:")
            listar_posts(posts)

        elif opcion == 2:
            termino = pedir_texto("Buscar por título: ")

            if not termino:
                print("Ingresá un término para realizar la búsqueda.")
            else:
                encontrados = buscar_por_titulo(posts, termino)
                print(f"\nResultados para '{termino}':")

                if encontrados:
                    listar_posts(encontrados)
                else:
                    print("No se encontraron publicaciones con ese término.")

        elif opcion == 3:
            tag_buscado = pedir_texto("Ingresá el tag a filtrar: ")

            if not tag_buscado:
                print("Ingresá un tag para realizar el filtrado.")
            else:
                encontrados = filtrar_por_tag(posts, tag_buscado)
                print(f"\nPosts con el tag '{tag_buscado}':")

                if encontrados:
                    listar_posts(encontrados)
                else:
                    print("No se encontraron publicaciones con ese tag.")

        elif opcion == 4:
            validar_todos_los_posts(posts)

        elif opcion == 5:
            print("\nGracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("\nOpción inválida, intentá de nuevo.")


if __name__ == "__main__":
    main()
