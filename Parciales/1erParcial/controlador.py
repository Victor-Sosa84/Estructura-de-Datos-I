from modelo import ListaCircular

class Controlador:
    def __init__(self, vista):
        self.ListaC = ListaCircular()
        self.vista = vista

    def adelante(self, figura):
        nueva_figura = self.ListaC.adelante(figura)
        nuevo_color = self.ListaC.obtener_color(nueva_figura)
        return nueva_figura, nuevo_color

    def atras(self, figura):
        nueva_figura = self.ListaC.atras(figura)
        nuevo_color = self.ListaC.obtener_color(nueva_figura)
        return nueva_figura, nuevo_color