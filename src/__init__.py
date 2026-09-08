"""
Paquete src - Gestor de Tareas CLI (versión sin POO)

Este paquete contiene todos los módulos necesarios para el funcionamiento
del Gestor de Tareas, una aplicación de línea de comandos que permite
gestionar tareas con persistencia en JSON.

Módulos disponibles:
    - tareas: Funciones para manejar tareas (CRUD)
    - storage: Operaciones de persistencia (guardar/cargar)
    - cli: Interfaz de usuario y funciones de interacción
    - main: Punto de entrada principal
"""

import os
import sys

__version__ = "1.0.0"
__author__ = "Tu Nombre"

if __package__ in (None, ""):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    if root_dir not in sys.path:
        sys.path.insert(0, root_dir)

try:
    if __package__:
        from .tareas import (
            crear_tarea,
            listar_tareas,
            completar_tarea,
            eliminar_tarea,
            obtener_estadisticas,
            buscar_tarea,
        )
        from .storage import guardar_tareas, cargar_tareas
    else:
        from src.tareas import (
            crear_tarea,
            listar_tareas,
            completar_tarea,
            eliminar_tarea,
            obtener_estadisticas,
            buscar_tarea,
        )
        from src.storage import guardar_tareas, cargar_tareas
except ModuleNotFoundError:
    from tareas import (
        crear_tarea,
        listar_tareas,
        completar_tarea,
        eliminar_tarea,
        obtener_estadisticas,
        buscar_tarea,
    )
    from storage import guardar_tareas, cargar_tareas

__all__ = [
    "crear_tarea",
    "listar_tareas",
    "completar_tarea",
    "eliminar_tarea",
    "obtener_estadisticas",
    "buscar_tarea",
    "guardar_tareas",
    "cargar_tareas",
]


if __name__ == "__main__":
    try:
        from src.cli import main as cli_main
    except ModuleNotFoundError:
        from cli import main as cli_main
    cli_main()