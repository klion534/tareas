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

__version__ = "1.0.0"
__author__ = "Tu Nombre"

# Exportar elementos principales
from src.tareas import crear_tarea, listar_tareas, completar_tarea, eliminar_tarea
from src.storage import guardar_tareas, cargar_tareas

__all__ = [
    "crear_tarea",
    "listar_tareas",
    "completar_tarea",
    "eliminar_tarea",
    "guardar_tareas",
    "cargar_tareas"
]