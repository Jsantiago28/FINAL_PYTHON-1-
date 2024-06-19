from gestor_tareas import GestorTareas


def mostrar_menu():
    print("\nSistema de Gestión de Tareas")
    print("1. Agregar Tarea")
    print("2. Ver Tareas")
    print("3. Actualizar Tarea")
    print("4. Eliminar Tarea")
    print("5. Salir")

def agregar_tarea(gestor):
    descripcion = input("Descripción: ")
    fecha_limite = input("Fecha Límite (YYYY-MM-DD): ")
    prioridad = input("Prioridad (baja, media, alta): ")
    categoria = input("Categoría: ")
    gestor.crear_tarea(descripcion, fecha_limite, prioridad, categoria)

def ver_tareas(gestor):
    tareas = gestor.leer_tareas()
    if not tareas:
        print("No hay tareas.")
    else:
        for id_tarea, tarea in tareas.items():
            print(f"ID: {tarea['id']}, Descripción: {tarea['descripcion']}, Fecha Límite: {tarea['fecha_limite']}, Prioridad: {tarea['prioridad']}, Categoría: {tarea['categoria']}, Estado: {tarea['estado']}")

def actualizar_tarea(gestor):
    id_tarea = int(input("ID de la tarea: "))
    descripcion = input("Nueva Descripción: ")
    fecha_limite = input("Nueva Fecha Límite (YYYY-MM-DD): ")
    prioridad = input("Nueva Prioridad (baja, media, alta): ")
    categoria = input("Nueva Categoría: ")
    estado = input("Nuevo Estado (pendiente, en progreso, completada): ")
    if gestor.actualizar_tarea(id_tarea, descripcion=descripcion, fecha_limite=fecha_limite, prioridad=prioridad, categoria=categoria, estado=estado):
        print("Tarea actualizada exitosamente.")
    else:
        print("Tarea no encontrada.")

def eliminar_tarea(gestor):
    id_tarea = int(input("ID de la tarea: "))
    if gestor.eliminar_tarea(id_tarea):
        print("Tarea eliminada exitosamente.")
    else:
        print("Tarea no encontrada.")

def main():
    gestor = GestorTareas()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
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
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
