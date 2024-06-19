from interfaz import mostrar_menu, agregar_tarea, ver_tareas, actualizar_tarea, eliminar_tarea
from gestor_tareas import GestorTareas

def main():
    archivo_tareas = 'tareas.json'
    gestor = GestorTareas(archivo_tareas)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_tarea(gestor)
        elif opcion == '2':
            ver_tareas(gestor)
        elif opcion == '3':
            actualizar_tarea(gestor)
        elif opcion == '4':
            eliminar_tarea(gestor)
        elif opcion == '5':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
