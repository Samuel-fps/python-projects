# BookStore Manager

Este proyecto es una aplicación de gestión de libros desarrollada en Python. Utiliza una interfaz gráfica construida con Tkinter para permitir a los usuarios gestionar una colección de libros. Los datos de los libros se almacenan en una base de datos SQLite, que se crea automáticamente al ejecutar la aplicación.

## Características

- **Interfaz gráfica**: Fácil de usar para gestionar libros.
- **Funcionalidades**: Permite agregar, editar, eliminar y visualizar detalles de los libros.
- **Base de datos SQLite**: Guarda los datos localmente en un archivo de base de datos.

## Requisitos

- Python 3.12 o superior
- Tkinter (generalmente viene preinstalado con Python)
- PyInstaller (para generar el ejecutable)

## Uso

Para ejecutar la aplicación desde el entorno de desarrollo:

```bash
    python app.py
```

## Generar ejecutable

  1. Instala PyInstaller si aún no lo tienes:

        ```bash
            pip install pyinstaller
        ```

  2. Genera el ejecutable con el siguiente comando, asegurándote de añadir la
     ruta a libpython3.12.so si es necesario:

        ```bash
            pyinstaller --console --add-binary "/ruta/a/libpython3.12.so:." app.py
        ```

  3. El ejecutable se creará en el directorio dist/app. Puedes ejecutar la
   aplicación generada con:

        ```bash
            ./dist/app/app
        ```
