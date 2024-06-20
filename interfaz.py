from gestor_tareas import GestorTareas  # Importa la clase GestorTareas desde el módulo gestor_tareas

def mostrar_menu():
    """
    Muestra el menú principal del sistema de gestión de tareas.
    """
    print("\nSistema de Gestión de Tareas")
    print("1. Agregar Tarea")
    print("2. Ver Tareas")
    print("3. Actualizar Tarea")
    print("4. Eliminar Tarea")
    print("5. Salir")

def agregar_tarea(gestor):
    """
    Solicita los detalles de una nueva tarea al usuario y la agrega usando el gestor de tareas.
    """
    descripcion = input("Descripción: ")
    fecha_limite = input("Fecha Límite (YYYY-MM-DD): ")
    prioridad = input("Prioridad (baja, media, alta): ")
    categoria = input("Categoría: ")
    gestor.crear_tarea(descripcion, fecha_limite, prioridad, categoria)  # Llama al método crear_tarea del gestor

def ver_tareas(gestor):
    """
    Muestra todas las tareas existentes.
    Permite al usuario volver al menú principal o salir del programa.
    """
    tareas = gestor.leer_tareas()  # Llama al método leer_tareas del gestor para obtener las tareas
    if not tareas:  # Verifica si no hay tareas
        print("No hay tareas.")
    else:  # Si hay tareas, las imprime
        for id_tarea, tarea in tareas.items():
            print(f"ID: {tarea['id']}, Descripción: {tarea['descripcion']}, Fecha Límite: {tarea['fecha_limite']}, Prioridad: {tarea['prioridad']}, Categoría: {tarea['categoria']}, Estado: {tarea['estado']}")
    
    # Opciones para volver al menú principal o salir del programa
    print("\n1. Volver al menú principal")
    print("2. Salir del programa")
    opcion = input("Seleccione una opción: ")
    if opcion == "2":
        print("Saliendo del programa.")
        exit()  # Sale del programa

def actualizar_tarea(gestor):
    """Actualiza una tarea existente solicitando los nuevos detalles al usuario.
    Si no hay tareas, sugiere agregar una tarea primero.
    Permite al usuario volver al menú principal o salir del programa."""
    tareas = gestor.leer_tareas()  # Llama al método leer_tareas del gestor para obtener las tareas
    if not tareas:  # Verifica si no hay tareas
        print("No hay tareas. Agregue una tarea primero.")
        return

    id_tarea = int(input("ID de la tarea: "))  # Solicita el ID de la tarea a actualizar
    if id_tarea not in tareas:  # Verifica si el ID no se encuentra en las tareas
        print("ID no encontrado.")
        return

    # Solicita los nuevos detalles de la tarea
    descripcion = input("Nueva Descripción: ")
    fecha_limite = input("Nueva Fecha Límite (YYYY-MM-DD): ")
    prioridad = input("Nueva Prioridad (baja, media, alta): ")
    categoria = input("Nueva Categoría: ")
    estado = input("Nuevo Estado (pendiente, en progreso, completada): ")
    
    # Llama al método actualizar_tarea del gestor con los nuevos detalles
    if gestor.actualizar_tarea(id_tarea, descripcion=descripcion, fecha_limite=fecha_limite, prioridad=prioridad, categoria=categoria, estado=estado):
        print("Tarea actualizada exitosamente.")
    else:
        print("Tarea no encontrada.")

    # Opciones para volver al menú principal o salir del programa
    print("\n1. Volver al menú principal")
    print("2. Salir del programa")
    opcion = input("Seleccione una opción: ")
    if opcion == "2":
        print("Saliendo del programa.")
        exit()  # Sale del programa

def eliminar_tarea(gestor):
    """Elimina una tarea existente solicitando su ID al usuario."""
    id_tarea = int(input("ID de la tarea: "))  # Solicita el ID de la tarea a eliminar
    if gestor.eliminar_tarea(id_tarea):  # Llama al método eliminar_tarea del gestor
        print("Tarea eliminada exitosamente.")
    else:
        print("Tarea no encontrada.")

def main():
    """Función principal que ejecuta el programa y muestra el menú principal en un bucle."""
    gestor = GestorTareas()  # Crea una instancia del gestor de tareas
    while True:
        mostrar_menu()  # Muestra el menú principal
        opcion = input("Seleccione una opción: ")  # Solicita al usuario que seleccione una opción
        if opcion == "1":
            agregar_tarea(gestor)
        elif opcion == "2":
            ver_tareas(gestor)
        elif opcion == "3":
            actualizar_tarea(gestor)
        elif opcion == "4":
            eliminar_tarea(gestor)
        elif opcion == "5":
            print("Saliendo del sistema de gestión de tareas.")
            break  # Sale del bucle y del programa
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()  # Llama a la función principal si el archivo se ejecuta como un script
