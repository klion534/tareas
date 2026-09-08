"""
Módulo de interfaz de línea de comandos para el Gestor de Tareas (versión sin POO).
Contiene todas las funciones de interacción con el usuario.
"""

import sys
from typing import List, Dict

try:
    from src.tareas import (
        crear_tarea,
        listar_tareas,
        completar_tarea,
        eliminar_tarea,
        obtener_estadisticas,
        buscar_tarea
    )
    from src.storage import guardar_tareas, cargar_tareas
except ModuleNotFoundError:
    from tareas import (
        crear_tarea,
        listar_tareas,
        completar_tarea,
        eliminar_tarea,
        obtener_estadisticas,
        buscar_tarea
    )
    from storage import guardar_tareas, cargar_tareas


def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("\n" + "=" * 40)
    print("        GESTOR DE TAREAS - CLI")
    print("=" * 40)
    print("1. 📋 Ver todas las tareas")
    print("2. ➕ Agregar nueva tarea")
    print("3. ✅ Marcar tarea como completada")
    print("4. 🗑️ Eliminar tarea")
    print("5. 🔍 Buscar tarea")
    print("6. 📊 Ver estadísticas")
    print("7. 💾 Guardar y Salir")
    print("-" * 40)


def obtener_opcion() -> int:
    """
    Solicita y valida la opción del usuario.
    
    Returns:
        int: Opción seleccionada, o -1 si hay error
    """
    try:
        opcion = int(input("Selecciona una opción: "))
        return opcion
    except ValueError:
        print("❌ Error: Debes ingresar un número.")
        return -1


def obtener_indice(tareas: List[Dict], accion: str) -> int:
    """
    Solicita un índice válido para operar sobre una tarea.
    
    Args:
        tareas (List[Dict]): Lista de tareas
        accion (str): Acción a realizar (ej: "completar", "eliminar")
    
    Returns:
        int: Índice válido, o -1 si hay error o cancelación
    """
    if not tareas:
        print("📭 No hay tareas para " + accion + ".")
        return -1
    
    listar_tareas(tareas)
    
    try:
        indice = int(input(f"\nNúmero de tarea a {accion}: ")) - 1
        if 0 <= indice < len(tareas):
            return indice
        else:
            print("❌ Número de tarea inválido.")
            return -1
    except ValueError:
        print("❌ Debes ingresar un número válido.")
        return -1


def agregar_tarea_interactiva(tareas: List[Dict]):
    """
    Solicita datos al usuario y agrega una nueva tarea.
    
    Args:
        tareas (List[Dict]): Lista de tareas donde agregar
    """
    print("\n" + "=" * 40)
    print("        AGREGAR NUEVA TAREA")
    print("=" * 40)
    
    titulo = input("Título de la tarea: ").strip()
    if not titulo:
        print("❌ El título no puede estar vacío.")
        return
    
    descripcion = input("Descripción (opcional): ").strip()
    
    nueva_tarea = crear_tarea(titulo, descripcion)
    tareas.append(nueva_tarea)
    
    print(f"✅ Tarea '{titulo}' agregada exitosamente.")


def mostrar_estadisticas(tareas: List[Dict]):
    """
    Muestra estadísticas de las tareas.
    
    Args:
        tareas (List[Dict]): Lista de tareas
    """
    stats = obtener_estadisticas(tareas)
    
    print("\n" + "=" * 40)
    print("        ESTADÍSTICAS")
    print("=" * 40)
    print(f"📊 Total de tareas: {stats['total']}")
    print(f"✅ Completadas: {stats['completadas']} ({stats['porcentaje']:.1f}%)")
    print(f"⬜ Pendientes: {stats['pendientes']}")


def buscar_tarea_interactiva(tareas: List[Dict]):
    """
    Busca tareas por título o descripción.
    
    Args:
        tareas (List[Dict]): Lista de tareas
    """
    texto = input("\n🔍 Texto a buscar: ").strip()
    if not texto:
        print("❌ Debes ingresar un texto para buscar.")
        return
    
    resultados = buscar_tarea(tareas, texto)
    
    if resultados:
        print(f"\n✅ Se encontraron {len(resultados)} tarea(s):")
        listar_tareas(resultados)
    else:
        print("📭 No se encontraron tareas que coincidan con la búsqueda.")


def confirmar_salida() -> bool:
    """
    Solicita confirmación antes de salir.
    
    Returns:
        bool: True si se confirma la salida, False en caso contrario
    """
    respuesta = input("\n¿Estás seguro de que quieres salir? (s/n): ").lower()
    return respuesta in ['s', 'si', 'sí', 'y', 'yes']


def main():
    """Ejecuta el flujo principal del menú del CLI."""
    print("\n" + "🚀" * 20)
    print("    GESTOR DE TAREAS - Iniciando...")
    print("🚀" * 20)

    tareas = cargar_tareas()
    print(f"📂 Cargadas {len(tareas)} tareas desde el archivo.")

    while True:
        try:
            mostrar_menu()
            opcion = obtener_opcion()

            if opcion == 1:
                listar_tareas(tareas)
            elif opcion == 2:
                agregar_tarea_interactiva(tareas)
            elif opcion == 3:
                indice = obtener_indice(tareas, "completar")
                if indice != -1:
                    if completar_tarea(tareas, indice):
                        print(f"✅ Tarea '{tareas[indice]['titulo']}' marcada como completada.")
                    else:
                        print("❌ Error al completar la tarea.")
            elif opcion == 4:
                indice = obtener_indice(tareas, "eliminar")
                if indice != -1:
                    titulo = tareas[indice]['titulo']
                    if eliminar_tarea(tareas, indice):
                        print(f"🗑️ Tarea '{titulo}' eliminada.")
                    else:
                        print("❌ Error al eliminar la tarea.")
            elif opcion == 5:
                buscar_tarea_interactiva(tareas)
            elif opcion == 6:
                mostrar_estadisticas(tareas)
            elif opcion == 7:
                if guardar_tareas(tareas):
                    print("💾 Tareas guardadas correctamente.")
                else:
                    print("⚠️ No se pudieron guardar las tareas.")
                print("\n👋 ¡Hasta luego!")
                sys.exit(0)
            else:
                print("⚠️ Opción no válida. Por favor, selecciona una opción del 1 al 7.")

        except KeyboardInterrupt:
            print("\n\n⚠️ Interrupción detectada. ¿Deseas guardar antes de salir?")
            if confirmar_salida():
                if guardar_tareas(tareas):
                    print("💾 Tareas guardadas correctamente.")
                print("👋 ¡Hasta luego!")
                sys.exit(0)
            print("⏹️ Continuando con la aplicación...")
            continue
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            print("🔄 El programa continuará ejecutándose.")


if __name__ == "__main__":
    main()