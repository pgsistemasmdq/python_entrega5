# Menú e ingreso de datos desde la consola.

# Muestra el menú y devuelve la opción elegida.
def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    try:
        opcion = int(input("Selecciona una opción (1-5): "))
        return opcion
    except ValueError:
        print("Error: debés ingresar un número del 1 al 5.")
        return 0


# Pide un texto al usuario y elimina espacios al principio y al final.
def pedir_texto(mensaje):
    return input(mensaje).strip()
