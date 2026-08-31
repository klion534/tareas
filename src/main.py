"""
Punto de entrada principal del Gestor de Tareas CLI (versión sin POO).
Orquesta la aplicación y maneja el flujo principal del programa.
"""

import sys
from src.storage import guardar_tareas, cargar_tareas
from src.tareas import completar_tarea, eliminar_tarea
from src.cli import (
    mostrar_menu,
    obtener_opcion,
    agregar_tarea_interactiva,
    listar_tareas,
    mostrar_estadisticas,
    buscar_tarea_interactiva,
    obtener_indice,
    confirmar_salida
)


def main():
    """
    Función principal que ejecuta el Gestor de Tareas.
    """
    print("\n" + "🚀" * 20)
    print("    GESTOR DE TAREAS - Iniciando...")
    print("🚀" * 20)
    
    # Cargar tareas existentes
    tareas = cargar_tareas()
    print(f"📂 Cargadas {len(tareas)} tareas desde el archivo.")
    
    # Bucle principal
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
            else:
                print("⏹️ Continuando con la aplicación...")
                continue
        
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            print("🔄 El programa continuará ejecutándose.")


if __name__ == "__main__":
    main()