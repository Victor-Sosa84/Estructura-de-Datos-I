from Modelo.modelo import ListaEnlazada

class Controlador:
    def __init__(self):
        self._lista = ListaEnlazada()

    def mostrar_tareas(self):
        return self._lista.mostrar()

    def agregar_tarea_inicio(self, descripcion):
        return self._lista.agregar_inicio(descripcion)

    def agregar_tarea_final(self, descripcion):
        return self._lista.agregar_final(descripcion)

    def completar_tarea(self, descripcion):
        self._lista.completar(descripcion)

    def eliminar_tarea(self, descripcion):
        self._lista.eliminar(descripcion)
