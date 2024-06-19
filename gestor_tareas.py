import os
import json

class GestorTareas:
    def __init__(self, directorio='tareas'):
        self.directorio = directorio
        if not os.path.exists(directorio):
            os.makedirs(directorio)
    
    def _ruta_tarea(self, id_tarea):
        return os.path.join(self.directorio, f'tarea_{id_tarea}.json')
    
    def crear_tarea(self, descripcion, fecha_limite, prioridad, categoria):
        tareas = self.leer_tareas()
        next_id = max(tareas.keys(), default=0) + 1
        tarea = {
            "id": next_id,
            "descripcion": descripcion,
            "fecha_limite": fecha_limite,
            "prioridad": prioridad,
            "categoria": categoria,
            "estado": "pendiente"
        }
        ruta = self._ruta_tarea(next_id)
        with open(ruta, 'w') as archivo:
            json.dump(tarea, archivo)
        print("Tarea agregada exitosamente.")
    
    def leer_tareas(self):
        tareas = {}
        for archivo in os.listdir(self.directorio):
            if archivo.endswith('.json'):
                ruta = os.path.join(self.directorio, archivo)
                with open(ruta, 'r') as f:
                    tarea = json.load(f)
                    tareas[tarea["id"]] = tarea
        return tareas
    
    def actualizar_tarea(self, id_tarea, descripcion=None, fecha_limite=None, prioridad=None, categoria=None, estado=None):
        ruta = self._ruta_tarea(id_tarea)
        if os.path.exists(ruta):
            with open(ruta, 'r') as archivo:
                tarea = json.load(archivo)
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
                json.dump(tarea, archivo)
            return True
        return False

    def eliminar_tarea(self, id_tarea):
        ruta = self._ruta_tarea(id_tarea)
        if os.path.exists(ruta):
            os.remove(ruta)
            return True
        return False
