from Modelo.modelo import ListaEnlazada

class Controlador:
    def __init__(self):
        """
        Método constructor. Inicializa la lista enlazada.
        """
        self._lista = ListaEnlazada()

    def mostrar_tareas(self):
        """
        Muestra la lista de tareas.

        Returns:
            Obtiene la lista de tareas desde el modelo.
        """
        return self._lista.mostrar()

    def agregar_tarea_inicio(self, descripcion):
        """
        Agrega una tarea al inicio de la lista.

        Returns:
            (bool): Devuelve True o False si la tarea fue añadida al inicio.
        """
        return self._lista.agregar_inicio(descripcion)

    def agregar_tarea_final(self, descripcion):
        """
        Agrega una tarea al final de la lista.

        Returns:
            (bool): Devuelve True o False si la tarea fue añadida al final.
        """
        return self._lista.agregar_final(descripcion)

    def completar_tarea(self, descripcion):
        """
        Completa una tarea.
        """
        self._lista.completar(descripcion)

    def eliminar_tarea(self, descripcion):
        """
        Elimina una tarea.
        """
        self._lista.eliminar(descripcion)
