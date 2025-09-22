import math
import re
from fractions import Fraction

class class_Modelo:
    def __init__(self):
        '''
        Clase que representa el modelo de la aplicación.
        Maneja la lógica y los datos de la aplicación.
        '''
        self.fracciones = []
    
    def limpiar_entrada(self):
        '''
        Borra todo.
        
        Returns:
            str: Una cadena vacía.
        '''
        return ""
    
    def evaluar(self, texto):
        '''
        Evalúa la expresión en la entrada.
        
        Parámetros:
            texto (str): El texto en la entrada.
            
        Returns:
            (str): El resultado de las operaciones en la entrada.
        '''
        texto = texto.replace("÷", "/").replace("×", "*")
    
        fracciones = re.findall(r"\((\d+)/(\d+)\)", texto)
    
        for num, den in fracciones:
            fr = f"Fraction({num},{den})"
            texto = texto.replace(f"({num}/{den})", fr)
    
        return eval(texto, {"Fraction": Fraction}, {})
    
    def añadir_fraccion(self, texto_entrada, num, den):
        '''
        Añade una fracción a la entrada.
        
        Parámetros:
            texto_entrada (str): La entrada actual como cadena.
            fraccion (tuple): Una tupla que representa la fracción (numerador, denominador).

        Returns:
            str: La nueva entrada con la fracción añadida.
        '''
        self.fracciones.append(Fraction(num, den))
        return "".join([texto_entrada, f"({num}/{den})"]) 

    def comparar_mayor_a_menor(self):
        '''
        Compara y ordena la lista de las fracciones añadidas a la lista
        desde la entrada.

        Returns:
            (str): La cadena con las fracciones ordenadas de mayor a menor.
        '''
        fracs = sorted(self.fracciones, reverse=True)
        return ", ".join(str(fr) for fr in fracs)

    def comparar_menor_a_mayor(self):
        '''
        Compara y ordena la lista de las fracciones añadidas a la lista
        desde la entrada.

        Returns:
            (str): La cadena con las fracciones ordenadas de menor a mayor.
        '''
        fracs = sorted(self.fracciones)
        return ", ".join(str(fr) for fr in fracs)

