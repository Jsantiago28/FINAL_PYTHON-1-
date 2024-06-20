from gestor_tareas import GestorTareas  #Importa la clase GestorTareas del modulo gestor_tareas

def mostrar_menu():
   
    #Muestra el manu principal del sistema de gestión de tareas
   
    print("\nSistema de Gestión de Tareas")
    print("1. Agregar Tarea")
    print("2. Ver Tareas")
    print("3. Actualizar Tarea")
    print("4. Eliminar Tarea")
    print("5. Filtrar Tareas por Prioridad")
    print("6. Filtrar Tareas por Categoria")
    print("7. Salir")

#agrega una tarea al sistema
def agregar_tarea(gestor):
    """Solicita los detalles de una nueva taera al usuario y la agrega usando el gestor de tareas."""
    descripcion = input("Descripcion: ")
    fecha_limite = input("Fecha Limite (DD/MM/YYYY): ")
    prioridad = input("Prioridad (baja, media, alta): ")
    categoria = input("Categoría: ")
    gestor.crear_tarea(descripcion, fecha_limite, prioridad, categoria)

def ver_tareas(gestor):
    """Muestra todas las tareas existentes. Permite al usuario volver al menú principal o salir del programa."""
    tareas = gestor.leer_tareas()
    if not tareas:
        print("No hay tareas.")
    else:
        for id_tarea, tarea in tareas.items():
            print(f"ID: {tarea['id']}, Descripcion: {tarea['descripcion']}, Fecha Limite: {tarea['fecha_limite']}, Prioridad: {tarea['prioridad']}, Categoría: {tarea['categoria']}, Estado: {tarea['estado']}")
    print("\n1. Volver al menu principal")
    print("2. Salir del programa")
    opcion = input("Seleccione una opcion: ")
    if opcion == "2":
        print("Saliendo del programa.")
        exit()

def actualizar_tarea(gestor):
    """Actualiza una tarea existente solicitando el ID al usuario y si no hay tareas, pide agregar una tarea primero."""
   
    tareas = gestor.leer_tareas()
    if not tareas:
        print("No hay tareas. Agregue una tarea primero.")
        return

    id_tarea = int(input("Ingrese el ID de la tarea: "))
    if id_tarea not in tareas:
        print("El ID ingresado no fue encontrado.")
        return

    descripcion = input("Nueva descripcion, si desea dejarlo igual presione Enter:: ")
    fecha_limite = input("Nueva fecha limite (DD/MM/YYYY), Si desea dejarlo igual presione Enter:: ")
    prioridad = input("Nueva prioridad (baja, media, alta), si desea dejarlo igual presione Enter: ")
    categoria = input("Nueva categoría, si desea dejarla igual presione Enter:: ")
    estado = input("Nuevo estado (pendiente, en progreso, completada), si desea dejarlo igual presione Enter:: ")
   
    if gestor.actualizar_tarea(id_tarea, descripcion=descripcion, fecha_limite=fecha_limite, prioridad=prioridad, categoria=categoria, estado=estado):
        print("Tarea actualizada exitosamente.")
    else:
        print("Tarea no encontrada.")

    print("\n1. Volver al menu principal")
    print("2. Salir del programa")
    opcion = input("Seleccione una opción: ")
    if opcion == "2":
        print("Saliendo del programa.")
        exit()

def eliminar_tarea(gestor):
    #Elimina una tarea existente solicitando su ID al usuario.
   
    id_tarea = int(input("Ingrese el ID de la tarea: "))
    if gestor.eliminar_tarea(id_tarea):
        print("Tarea eliminada exitosamente.")
    else:
        print("Tarea no encontrada.")

def filtrar_prioridad(gestor):
    """Filtra las tareas por prioridad solicitando al usuario la prioridad deseada."""
    prioridad = input("Ingrese la prioridad por la que desea filtrar (baja, media, alta): ").lower()
    tareas = gestor.leer_prioridad(prioridad)
    if not tareas:
        print(f"No hay tareas con la prioridad {prioridad}.")
    else:
        for tarea in tareas:
            print(f"ID: {tarea['id']}, Descripcion: {tarea['descripcion']}, Fecha Limite: {tarea['fecha_limite']}, Prioridad: {tarea['prioridad']}, Categoría: {tarea['categoria']}, Estado: {tarea['estado']}")

def filtrar_categoria(gestor):
    """Filtra las tareas por categoria solicitando al usuario la categoría deseada."""
    categoria = input("Ingrese la categoria para filtrar: ").lower()
    tareas = gestor.leer_categoria(categoria)
    if not tareas:
        print(f"No hay tareas en la categoria {categoria}.")
    else:
        for tarea in tareas:
            print(f"ID: {tarea['id']}, Descripcion: {tarea['descripcion']}, Fecha Limite: {tarea['fecha_limite']}, Prioridad: {tarea['prioridad']}, Categoria: {tarea['categoria']}, Estado: {tarea['estado']}")

def main():
    """Función principal que ejecuta el programa y muestra el menú principal en un ciclo While."""
   
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
            filtrar_prioridad(gestor)
        elif opcion == "6":
            filtrar_categoria(gestor)
        elif opcion == "7":
            print("Saliendo del sistema de gestión de tareas.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()