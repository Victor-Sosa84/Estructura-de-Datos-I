class Nodo:
    def __init__(self, descripcion, estado="Por hacer", siguiente=None, impacto=None, fecha=None):
        """
        Constructor de la clase.

        Parámetros:
            descripcion(str): descripcion de la tarea.
            estado(str): el estado de la tarea.
            siguiente(Nodo): puntero al siguiente nodo en la lista.
            impacto(str): nivel de impacto de la tarea.
            fecha(str): fecha límite para completar la tarea.
        """
        self._descripcion = descripcion
        self._estado = estado
        self._siguiente = siguiente
        self._impacto = impacto
        self._fecha = fecha

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

        Parámetros:
            nueva_descripcion(str): la nueva descripcion de la tarea.
        """
        self._descripcion = nueva_descripcion

    def cambiar_estado(self, nuevo_estado):
        """
        Cambia el estado de una tarea.

        Parámetros:
            nuevo_estado(str): el nuevo estado de la tarea.
        """
        self._estado = nuevo_estado

    def obtener_impacto(self):
        """
        Obtiene el nivel de impacto de la tarea.
        """
        return self._impacto

    def obtener_fecha(self):
        """
        Obtiene la fecha límite de una tarea.
        """
        return self._fecha

class ListaEnlazada:
    def __init__(self):
        """
        Constructor de la clase.
        """
        self._cabeza = None

    def verificar_tarea(self, descripcion):
        """
        Verifica si la tarea ya está en la lista.

        Parámetros:
            descripcion(str): descripcion de la tarea que se va a verificar.

        Returns:
            (bool): True o False si la tarea ya existía.
        """
        actual = self._cabeza
        while actual:
            if actual.obtener_descripcion() == descripcion:
                return True
            actual = actual._siguiente
        return False

    def agregar(self, descripcion, impacto, fecha):
        """
        Agrega una tarea al inicio de la lista.

        Parámetros:
            descripcion(str): Descripción de la tarea que se va a agregar.
        
        Returns:
            (bool): True o False si fue añadida o no.
        """
        if not self.verificar_tarea(descripcion):
            nuevo_nodo = Nodo(descripcion, "Por hacer", self._cabeza, impacto, fecha)
            self._cabeza = nuevo_nodo
            return True
        else:
            return False

    def mostrar(self):
        """
        Muestra la lista de tareas completa.

        Returns:
            tareas (dict): Un diccionario con la lista de tareas.
        """
        self.ordenar_por_impacto()
        tareas = []
        actual = self._cabeza
        while actual:
            tareas.append(
                {
                    "descripcion" : actual.obtener_descripcion(),
                    "estado" : actual.obtener_estado(),
                    "impacto": actual.obtener_impacto(),
                    "fecha": actual.obtener_fecha()
                }
            )
            actual = actual._siguiente
        return tareas

    def completar(self, descripcion):
        """
        Busca y completa una tarea de la lista.

        Parámetros:
            descripcion(str): descripcion de la tarea que se va a completar.
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

        Parámetros:
            descripcion(str): descripcion de la tarea que se va a eliminar.
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
        
    def intercambiar(self, nodo1, nodo2):
        nodo1._descripcion, nodo2._descripcion = nodo2._descripcion, nodo1._descripcion
        nodo1._estado, nodo2._estado = nodo2._estado, nodo1._estado
        nodo1._impacto, nodo2._impacto = nodo2._impacto, nodo1._impacto
        nodo1._fecha, nodo2._fecha = nodo2._fecha, nodo1._fecha
    
    def ordenar_por_impacto(self):
        """
        Ordena la lista de tareas por su impacto (alto, medio, bajo o ninguno).
        """
        if not self._cabeza or not self._cabeza._siguiente:
            return

        niveles = {"Alto": 4, "Medio": 3, "Bajo": 2}        
        cambio = True

        while cambio:
            cambio = False
            actual = self._cabeza
            
            while actual._siguiente:
                siguiente = actual._siguiente
                if niveles.get(actual.obtener_impacto(), 1) < niveles.get(siguiente.obtener_impacto(), 1):
                    self.intercambiar(actual, siguiente)
                    cambio = True
                actual = actual._siguiente