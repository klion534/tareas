"""
Módulo para el manejo de tareas (versión sin POO).
Las tareas se representan como diccionarios.
"""

from datetime import datetime
from typing import List, Dict, Optional


def crear_tarea(titulo: str, descripcion: str = "") -> Dict:
    """
    Crea una nueva tarea como diccionario.
    
    Args:
        titulo (str): Título de la tarea (obligatorio)
        descripcion (str): Descripción de la tarea (opcional)
    
    Returns:
        Dict: Diccionario con los datos de la tarea
    """
    return {
        "titulo": titulo,
        "descripcion": descripcion,
        "completada": False,
        "fecha_creacion": datetime.now().isoformat()
    }


def listar_tareas(tareas: List[Dict]) -> None:
    """
    Muestra todas las tareas en formato legible.
    
    Args:
        tareas (List[Dict]): Lista de tareas
    """
    if not tareas:
        print("\n📭 No hay tareas en la lista.")
        return
    
    print("\n" + "=" * 40)
    print("        LISTA DE TAREAS")
    print("=" * 40)
    
    for i, tarea in enumerate(tareas, 1):
        estado = "✅" if tarea["completada"] else "⬜"
        print(f"{i}. {estado} {tarea['titulo']}")
        
        if tarea["descripcion"]:
            print(f"   📝 {tarea['descripcion']}")
        
        # Mostrar solo la fecha (sin hora)
        fecha = tarea["fecha_creacion"].split("T")[0]
        print(f"   📅 Creada: {fecha}")
        print()


def completar_tarea(tareas: List[Dict], indice: int) -> bool:
    """
    Marca una tarea como completada.
    
    Args:
        tareas (List[Dict]): Lista de tareas
        indice (int): Índice de la tarea (0-based)
    
    Returns:
        bool: True si se completó, False si el índice es inválido
    """
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        return True
    return False


def eliminar_tarea(tareas: List[Dict], indice: int) -> bool:
    """
    Elimina una tarea de la lista.
    
    Args:
        tareas (List[Dict]): Lista de tareas
        indice (int): Índice de la tarea (0-based)
    
    Returns:
        bool: True si se eliminó, False si el índice es inválido
    """
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        return True
    return False


def obtener_estadisticas(tareas: List[Dict]) -> Dict:
    """
    Calcula estadísticas de las tareas.
    
    Args:
        tareas (List[Dict]): Lista de tareas
    
    Returns:
        Dict: Diccionario con total, completadas y pendientes
    """
    total = len(tareas)
    completadas = sum(1 for t in tareas if t["completada"])
    pendientes = total - completadas
    porcentaje = (completadas / total * 100) if total > 0 else 0
    
    return {
        "total": total,
        "completadas": completadas,
        "pendientes": pendientes,
        "porcentaje": porcentaje
    }


def buscar_tarea(tareas: List[Dict], texto: str) -> List[Dict]:
    """
    Busca tareas que contengan el texto en el título o descripción.
    
    Args:
        tareas (List[Dict]): Lista de tareas
        texto (str): Texto a buscar
    
    Returns:
        List[Dict]: Lista de tareas que coinciden con la búsqueda
    """
    texto = texto.lower()
    resultados = []
    
    for tarea in tareas:
        if texto in tarea["titulo"].lower() or texto in tarea["descripcion"].lower():
            resultados.append(tarea)
    
    return resultados