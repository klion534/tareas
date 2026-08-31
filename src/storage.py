"""
Módulo de persistencia para el Gestor de Tareas (versión sin POO).
Maneja la lectura y escritura de datos en archivos JSON.
"""

import json
import os
from typing import List, Dict, Optional

# Constantes
ARCHIVO_DATOS = "tareas.json"
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_COMPLETA = os.path.join(os.path.dirname(DIRECTORIO_ACTUAL), ARCHIVO_DATOS)


def guardar_tareas(tareas: List[Dict], ruta: Optional[str] = None) -> bool:
    """
    Guarda la lista de tareas en un archivo JSON.
    
    Args:
        tareas (List[Dict]): Lista de tareas (diccionarios)
        ruta (str, optional): Ruta del archivo
    
    Returns:
        bool: True si se guardó correctamente, False en caso contrario
    """
    if ruta is None:
        ruta = RUTA_COMPLETA
    
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(tareas, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ Error al guardar las tareas: {e}")
        return False


def cargar_tareas(ruta: Optional[str] = None) -> List[Dict]:
    """
    Carga la lista de tareas desde un archivo JSON.
    
    Args:
        ruta (str, optional): Ruta del archivo
    
    Returns:
        List[Dict]: Lista de tareas cargadas. Si hay error, retorna lista vacía.
    """
    if ruta is None:
        ruta = RUTA_COMPLETA
    
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        print("⚠️ El archivo de datos está corrupto. Se iniciará con una lista vacía.")
        return []
    
    except Exception as e:
        print(f"❌ Error al cargar las tareas: {e}")
        return []


def existe_archivo(ruta: Optional[str] = None) -> bool:
    """Verifica si el archivo de datos existe."""
    if ruta is None:
        ruta = RUTA_COMPLETA
    return os.path.exists(ruta)