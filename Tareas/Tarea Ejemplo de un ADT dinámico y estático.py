# Ejemplo de un ADT, para un objeto Autómovil, de manera dinámica y estática

class Automovil:
    """
    Representación de un objeto Automóvil.

    Parámetros:
        marca (str): La marca del automóvil.
        modelo (str): El modelo del automóvil.
        color (str): El color del automóvil.
    """

    def __init__(self, marca=None, modelo=None, color=None):
        """
        Constructor de la clase Automovil.
        """
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__pasajeros = [None] * 4  # Espacio fijo para 4 pasajeros

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

    # -----------------------
    # Modelo ADT estático: Pasajeros
    # -----------------------
    def agregar_pasajero(self, nombre):
        """
        Agrega un pasajero en la primera posición vacía.

        Args:
            nombre (str): Nombre del pasajero.

        Returns:
            bool: True si se agregó, False si ya está lleno.
        """
        for i in range(4):
            if self.__pasajeros[i] is None:
                self.__pasajeros[i] = nombre
                return True
        return False  # No hay espacio

    def quitar_pasajero(self, nombre):
        """
        Quita un pasajero por nombre.

        Args:
            nombre (str): Nombre del pasajero a quitar.

        Returns:
            bool: True si se quitó, False si no estaba.
        """
        for i in range(4):
            if self.__pasajeros[i] == nombre:
                self.__pasajeros[i] = None
                return True
        return False

    @property
    def pasajeros(self):
        """
        Devuelve la lista de pasajeros.

        Returns:
            list: Lista de nombres de pasajeros.
        """
        return [p for p in self.__pasajeros if p is not None]

    # -----------------------
    # Método para representar el auto en texto
    # -----------------------
    def __str__(self):
        return f"{self.marca} {self.modelo}"


# -----------------------
# Modelo ADT dinámico: Fila de autos
# -----------------------
class fila_de_autos:
    def __init__(self):
        self.autos = []
    
    def agregar_auto(self, auto):
        self.autos.append(auto)
    
    def sacar_auto(self, auto):
        if auto in self.autos:
            self.autos.remove(auto)

    @property
    def lista_de_autos(self):
        # Devuelve solo el nombre (marca y modelo) de cada auto
        return [str(auto) for auto in self.autos]


# Ejemplo de uso
# Inicializar automóviles
auto_1 = Automovil("Toyota", "Starlet", "Blanco")
auto_2 = Automovil("Ford", "Fiesta", "Rojo")
auto_3 = Automovil("Chevrolet", "Spark", "Azul")

# Ejemplo de uso de ADT estático
auto_1.agregar_pasajero("Ana")
auto_1.agregar_pasajero("Luis")

print(auto_1.pasajeros)  # ['Ana', 'Luis']

auto_1.agregar_pasajero("Carlos")
auto_1.agregar_pasajero("Marta")

print(auto_1.pasajeros)  # ['Ana', 'Luis', 'Carlos', 'Marta']

auto_1.agregar_pasajero("Sofía")  # No se agrega, ya hay 4 pasajeros
auto_1.quitar_pasajero("Carlos")
auto_1.agregar_pasajero("Sofía")  # Ahora sí se agrega  

print(auto_1.pasajeros)  # ['Ana', 'Luis', 'Marta', 'Sofía']

# Ejemplo de uso de ADT dinámico    
fila = fila_de_autos()
fila.agregar_auto(auto_1)
fila.agregar_auto(auto_2)

print(fila.lista_de_autos)  # [auto_1, auto_2]

fila.sacar_auto(auto_1)

print(fila.lista_de_autos)  # [auto_2]