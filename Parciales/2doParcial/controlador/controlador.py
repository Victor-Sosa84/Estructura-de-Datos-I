class Controlador:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo

    def obt_exp(self, exp):
        self.modelo.limpiar()
        self.modelo.obt_exp(exp)

    def prefija(self):
        if self.modelo.pila_num and self.modelo.pila_op:
            return self.modelo.prefija()
        else: return "No hay Expresión"
    
    def evaluar(self):
        if self.modelo.pila_num and self.modelo.pila_op:
            return self.modelo.evaluar()
        else: return "No hay Expresión"