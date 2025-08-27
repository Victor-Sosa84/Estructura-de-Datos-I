# Ejemplo de un ADT, para un objeto Autómovil, de manera dinámica y estática

class Automovil:
    """
    Representación de un objeto Automóvil.

    Parámetros:
        marca (str): La marca del automóvil.
        modelo (str): El modelo del automóvil.
        color (str): El color del automóvil.
    """

    def __init__(self, marca, modelo, color):
        """
        Constructor de la clase Automovil.
        """
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color

    # -----------------------
    # Propiedad: marca
    # -----------------------
    @property
    def marca(self):
        """
        Obtiene la marca del automóvil.

        Returns:
            str: Marca del automóvil.
        """
        return self.__marca

    @marca.setter
    def marca(self, valor):
        """
        Cambia la marca del automóvil.

        Args:
            valor (str): Nueva marca del automóvil.
        """
        self.__marca = valor

    # -----------------------
    # Propiedad: modelo
    # -----------------------
    @property
    def modelo(self):
        """
        Obtiene el modelo del automóvil.

        Returns:
            str: Modelo del automóvil.
        """
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        """
        Cambia el modelo del automóvil.

        Args:
            valor (str): Nuevo modelo del automóvil.
        """
        self.__modelo = valor

    # -----------------------
    # Propiedad: color
    # -----------------------
    @property
    def color(self):
        """
        Obtiene el color del automóvil.

        Returns:
            str: Color del automóvil.
        """
        return self.__color

    @color.setter
    def color(self, valor):
        """
        Cambia el color del automóvil.

        Args:
            valor (str): Nuevo color del automóvil.
        """
        self.__color = valor

