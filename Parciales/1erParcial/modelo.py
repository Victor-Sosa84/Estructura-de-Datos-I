class Nodo:
    def __init__(self, figura, siguiente=None):
        self.figura = figura
        self.siguiente = siguiente


class ListaCircular:
    def __init__(self):
        # Crear los 3 nodos
        n1 = Nodo("Circulo")
        n2 = Nodo("Triangulo")
        n3 = Nodo("Rectangulo")

        # Enlazar en forma circular
        n1.siguiente = n2
        n2.siguiente = n3
        n3.siguiente = n1

        self.head = n1

        # Colores asociados
        self.colores = ["Rojo", "Verde", "Azul"]
        self.color_index = 0

    def adelante(self, figura_actual):
        actual = self.head
        while actual.figura != figura_actual:
            actual = actual.siguiente

        # Si pasamos del Rectángulo al Círculo -> rotar colores
        if actual.figura == "Rectangulo":
            self.recorrer_colores()

        self.head = actual.siguiente
        return self.head.figura

    def atras(self, figura_actual):
        actual = self.head
        while actual.siguiente.figura != figura_actual:
            actual = actual.siguiente

        # Si retrocedemos del Círculo al Rectángulo -> rotar colores también
        if figura_actual == "Circulo":
            self.recorrer_colores()

        self.head = actual
        return self.head.figura

    def recorrer_colores(self):
        """Rota los colores hacia la derecha (Rojo→Verde→Azul→Rojo...)"""
        self.colores = [self.colores[-1]] + self.colores[:-1]

    def obtener_color(self, figura):
        """Devuelve el color actual asociado a una figura."""
        if figura == "Circulo":
            return self.colores[0]
        elif figura == "Triangulo":
            return self.colores[1]
        elif figura == "Rectangulo":
            return self.colores[2]




