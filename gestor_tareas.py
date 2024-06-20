import os  # Módulo para operaciones del sistema de archivos
import json  # Módulo para trabajar con JSON
import random  # Módulo para generar números aleatorios

class GestorTareas:
    def __init__(self, directorio='tareas'):
        """ Constructor que inicializa el directorio donde se guardarán las tareas. Si el directorio no existe, lo crea."""
        self.directorio = directorio
        if not os.path.exists(directorio):
            os.makedirs(directorio)

    def _ruta_tarea(self, id_tarea):
        """ Método privado que genera la ruta del archivo donde se almacenará una tarea específica."""
        return os.path.join(self.directorio, f'tarea_{id_tarea}.json')

    def generar_id_unico(self, tareas):
        """Genera un ID único de 3 dígitos para una nueva tarea. Comprueba que el ID no exista ya en el diccionario de tareas. """
        while True:
            id_unico = random.randint(100, 999)  # Genera un número aleatorio entre 100 y 999
            if id_unico not in tareas:
                return id_unico

    def crear_tarea(self, descripcion, fecha_limite, prioridad, categoria):
        """ Crea una nueva tarea con los detalles proporcionados y la guarda en un archivo JSON."""
        tareas = self.leer_tareas()  # Lee las tareas existentes
        next_id = self.generar_id_unico(tareas)  # Genera un ID único para la nueva tarea
        tarea = {
            "id": next_id,
            "descripcion": descripcion,
            "fecha_limite": fecha_limite,
            "prioridad": prioridad,
            "categoria": categoria,
            "estado": "pendiente"
        }
        ruta = self._ruta_tarea(next_id)  # Genera la ruta del archivo para la nueva tarea
        with open(ruta, 'w') as archivo:
            json.dump(tarea, archivo)  # Guarda la tarea en un archivo JSON
        print("Tarea agregada exitosamente.")

    def leer_tareas(self):
        """Lee todas las tareas guardadas y las devuelve en un diccionario."""
        tareas = {}
        for archivo in os.listdir(self.directorio):
            if archivo.endswith('.json'):
                ruta = os.path.join(self.directorio, archivo)
                with open(ruta, 'r') as f:
                    tarea = json.load(f)  # Carga la tarea desde el archivo JSON
                    tareas[tarea["id"]] = tarea  # Añade la tarea al diccionario de tareas
        return tareas

    def actualizar_tarea(self, id_tarea, descripcion=None, fecha_limite=None, prioridad=None, categoria=None, estado=None):
        """Actualiza los detalles de una tarea existente."""
        
        ruta = self._ruta_tarea(id_tarea)  # Genera la ruta del archivo de la tarea a actualizar
        if os.path.exists(ruta):
            with open(ruta, 'r') as archivo:
                tarea = json.load(archivo)  # Carga la tarea desde el archivo JSON
            if descripcion:
                tarea["descripcion"] = descripcion
            if fecha_limite:
                tarea["fecha_limite"] = fecha_limite
            if prioridad:
                tarea["prioridad"] = prioridad
            if categoria:
                tarea["categoria"] = categoria
            if estado:
                tarea["estado"] = estado
            with open(ruta, 'w') as archivo:
                json.dump(tarea, archivo)  # Guarda los cambios en el archivo JSON
            return True
        return False

    def eliminar_tarea(self, id_tarea):
        """
        Elimina una tarea existente.
        """
        ruta = self._ruta_tarea(id_tarea)  # Genera la ruta del archivo de la tarea a eliminar
        if os.path.exists(ruta):
            os.remove(ruta)  # Elimina el archivo de la tarea
            return True
        return False
