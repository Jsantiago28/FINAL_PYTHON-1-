def agregar_tarea(gestor):
    """Solicita los detalles de una nueva tarea al usuario y la agrega usando el gestor de tareas. """
    descripcion = input("Descripción: ")
    fecha_limite = input("Fecha Límite (YYYY-MM-DD): ")
    prioridad = input("Prioridad (baja, media, alta): ")
    categoria = input("Categoría: ")
    gestor.crear_tarea(descripcion, fecha_limite, prioridad, categoria)  # Llama al método crear_tarea del gestor
