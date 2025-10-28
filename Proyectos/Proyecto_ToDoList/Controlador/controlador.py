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

    def agregar_tarea(self, descripcion, impacto, fecha):
        """
        Agrega una tarea al inicio de la lista.
        
        Parámetros:
            descripcion(str): Descripción de la tarea.

        Returns:
            (bool): True o False si la tarea fue añadida.
        """
        return self._lista.agregar(descripcion, impacto, fecha)

    def completar_tarea(self, descripcion):
        """
        Completa una tarea.

        Parámetros:
            descripcion(str): Descripción de la tarea.
        """
        self._lista.completar(descripcion)

    def eliminar_tarea(self, descripcion):
        """
        Elimina una tarea.

        Parámetros:
            descripcion(str): Descripción de la tarea.
        """
        self._lista.eliminar(descripcion)
