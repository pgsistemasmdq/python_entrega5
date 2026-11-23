# Preentrega 5: Organización modular del blog

Este proyecto continúa la **Entrega 4** del curso de Python. Conserva los mismos datos,
las búsquedas, los filtros y las validaciones, pero ahora cada parte del programa
está ubicada en un módulo diferente.

## Cómo ejecutar

1. Descargá y descomprimí el proyecto.
2. Abrí la carpeta `blog_consola` en Visual Studio Code.
3. Abrí la terminal integrada (**Terminal > Nueva terminal**).
4. Desde la carpeta donde está `main.py`, ejecutá:

   ```bash
   python main.py
   ```

   En Windows también podés usar `py main.py`.

**Importante:** se ejecuta `main.py`, no los archivos dentro de `blog/`.

## Estructura del proyecto

```text
blog_consola/
├── main.py
├── README.md
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

- **main.py:** inicia el programa y conecta las funciones mediante imports.
- **blog/__init__.py:** identifica a `blog` como paquete.
- **blog/datos.py:** contiene `perfil_autor`, `estados_post`, `etiquetas_blog` y `posts`.
- **blog/menu.py:** muestra el menú y recibe entradas del usuario usando `input()`.
- **blog/operaciones.py:** permite listar, buscar por título y filtrar por tag.
- **blog/validaciones.py:** revisa si los posts tienen la estructura correcta.

## Opciones del menú

1. **Ver todos los posts:** muestra título, nombre del autor y estado.
2. **Buscar por título:** acepta coincidencias parciales, sin distinguir mayúsculas y minúsculas.
3. **Filtrar por tag:** muestra publicaciones con el tag solicitado, sin distinguir mayúsculas y minúsculas.
4. **Validar posts:** informa cuáles son válidos y cuáles contienen errores.
5. **Salir:** cierra el programa.

El post de **id 6** está incompleto a propósito: no tiene la clave `contenido`.
Esto permite comprobar la validación de la opción 4, tal como en la Entrega 4.
