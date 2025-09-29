class PolinomioEstatico:
    def __init__(self, terminos):
        # Lista/tupla fija de términos
        self._terminos = terminos  

    # Getter
    def get_terminos(self):
        return self._terminos

    # Setter
    def set_terminos(self, nuevos_terminos):
        self._terminos = nuevos_terminos

    def evaluar(self, x):
        return sum(coef * (x ** exp) for coef, exp in self._terminos)

    def mostrar(self):
        return " + ".join(f"{coef}x^{exp}" for coef, exp in self._terminos)

pEst = PolinomioEstatico([(1,0), (2,3), (7,1), (9,2)])
print("Terminos:", pEst.get_terminos())
print("Polinomio Estatico:", pEst.mostrar())
print("Evaluado en x=2:", pEst.evaluar(2))

pEst.set_terminos([(4,6), (2,3), (7,2)])
print("------ Terminos modificados. ------")

print("Nuevo Polinomio Estatico:", pEst.mostrar())
print("Nueva evaluacion en x=2:", pEst.evaluar(2))
print("Nuevos terminos:", pEst.get_terminos())


print("------------------------------------------------")


class PolinomioDinamico:
    def __init__(self):
        self._terminos = []

    # Getter
    def get_terminos(self):
        return self._terminos

    # Setter
    def set_terminos(self, nuevos_terminos):
        self._terminos = nuevos_terminos

    def agregar_termino(self, coef, exp):
        self._terminos.append((coef, exp))

    def evaluar(self, x):
        return sum(coef * (x ** exp) for coef, exp in self._terminos)

    def mostrar(self):
        return " + ".join(f"{coef}x^{exp}" for coef, exp in self._terminos)
    
pDin = PolinomioDinamico()
pDin.agregar_termino(1,0)
pDin.agregar_termino(2,3) 
pDin.agregar_termino(7,1)
pDin.agregar_termino(9,2)

print("Terminos:", pDin.get_terminos())
print("Polinomio Dinamico:", pDin.mostrar())
print("Evaluado en x=2:", pDin.evaluar(2)) 

pDin.set_terminos([(4,6), (2,3), (7,2)])
print("------ Terminos modificados. ------")

print("Nuevo Polinomio Dinamico:", pDin.mostrar())
print("Nueva evaluacion en x=2:", pDin.evaluar(2))
print("Nuevos terminos:", pDin.get_terminos())