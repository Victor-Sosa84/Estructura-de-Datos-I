class Nodo:
    def __init__(self, descripcion, estado="Pendiente", siguiente=None):
        """
        Constructor de la clase.
        """
        self._descripcion = descripcion
        self._estado = estado
        self._siguiente = siguiente

    def obtener_descripcion(self):
        """
        Obtiene la descripción de una tarea.

        Returns:
            La descripción de la tarea.
        """
        return self._descripcion
    
    def obtener_estado(self):
        """
        Obtiene el estado de una tarea.

        Returns:
            El estado de la tarea.
        """
        return self._estado

    def cambiar_descripcion(self, nueva_descripcion):
        """
        Cambia la descripción de una tarea.
        """
        self._descripcion = nueva_descripcion

    def cambiar_estado(self, nuevo_estado):
        """
        Cambia el estado de una tarea.
        """
        self._estado = nuevo_estado

class ListaEnlazada:
    def __init__(self):
        """
        Constructor de la clase.
        """
        self._cabeza = None

    def verificar_tarea(self, descripcion):
        """
        Verifica si la tarea ya está en la lista.
        """
        actual = self._cabeza
        while actual:
            if actual.obtener_descripcion() == descripcion:
                return True
            actual = actual._siguiente
        return False

    def agregar_inicio(self, descripcion):
        """
        Agrega una tarea al inicio de la lista.
        
        Returns:
            (bool): True o False si fue añadida o no.
        """
        if not self.verificar_tarea(descripcion):
            nuevo_nodo = Nodo(descripcion, "Pendiente", self._cabeza)
            self._cabeza = nuevo_nodo
            return True
        else:
            return False

    def agregar_final(self, descripcion):
        """
        Agrega una tarea al final de la lista.
        
        Returns:
            (bool): True o False si fue añadida o no.
        """
        if not self.verificar_tarea(descripcion):
            nuevo_nodo = Nodo(descripcion)
            if not self._cabeza:
                self._cabeza = nuevo_nodo
                return
            ultimo_nodo = self._cabeza
            while ultimo_nodo._siguiente:
                ultimo_nodo = ultimo_nodo._siguiente
            ultimo_nodo._siguiente = nuevo_nodo
            return True
        else:
            return False

    def mostrar(self):
        """
        Muestra la lista de tareas completa.

        Returns:
            tareas (dict): Un diccionario con la lista de tareas.
        """
        tareas = []
        actual = self._cabeza
        while actual:
            tareas.append(
                {
                    "descripcion" : actual.obtener_descripcion(),
                    "estado" : actual.obtener_estado()
                }
            )
            actual = actual._siguiente
        return tareas

    def completar(self, descripcion):
        """
        Busca y completa una tarea de la lista.
        """
        actual = self._cabeza
        while actual:
            if actual.obtener_descripcion() == descripcion:
                actual.cambiar_estado("Completado")
                break
            actual = actual._siguiente

    def eliminar(self, descripcion):
        """
        Busca y elimina una tarea de la lista.
        """
        actual = self._cabeza
        if actual and actual.obtener_descripcion() == descripcion:
            self._cabeza = actual._siguiente
            actual = None
            return
        
        anterior = None
        while actual and actual.obtener_descripcion() != descripcion:
            anterior = actual
            actual = actual._siguiente

        if not actual:
            return
        
        anterior._siguiente = actual._siguiente
        actual = None