from datetime import datetime

class Tarea:
    def __init__(self, descripcion, fecha_limite, prioridad, categoria):
        self.id = int(datetime.timestamp(datetime.now()))
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
        self.categoria = categoria
        self.estado = "pendiente"
