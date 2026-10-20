# Gestor de tareas CLI

Aplicación de consola en Python para practicar operaciones CRUD, modularización y persistencia local de datos.

> Este repositorio es un fork de [carlosfadul/tareas](https://github.com/carlosfadul/tareas). El historial de commits muestra los cambios realizados en este fork; el código original conserva su atribución correspondiente.

## Funciones

- Crear tareas con título y descripción.
- Listar, buscar, completar y eliminar tareas.
- Consultar estadísticas de tareas completadas y pendientes.
- Guardar y cargar datos localmente en `tareas.json`.

## Requisitos

- Python 3.8 o superior.
- No requiere paquetes externos.

## Ejecutar

Desde la raíz del repositorio:

```bash
python src/main.py
```

La aplicación también incluye la interfaz CLI ejecutable desde:

```bash
python src/cli.py
```

Los datos se guardan localmente en `tareas.json`, que está excluido de Git para evitar subir información de uso local.

## Pruebas

```bash
python -m unittest discover -s tests -v
```

## Tecnologías y conceptos

Python, módulos, listas y diccionarios, funciones, manejo de archivos JSON, validación de entradas y pruebas con `unittest`.

## Estado

Proyecto de aprendizaje. La aplicación funciona desde la terminal y guarda datos en un archivo local; no utiliza base de datos ni interfaz gráfica.
