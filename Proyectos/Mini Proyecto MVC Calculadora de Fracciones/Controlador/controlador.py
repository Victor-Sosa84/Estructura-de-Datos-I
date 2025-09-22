class class_Controlador:
    def __init__(self, modelo, vista):
        '''
        Clase que representa el controlador de la aplicación.
        
        Parámetros:
            modelo: La instancia del modelo, para manejar la lógica.
            vista: La instancia de la vista, para actualizar la interfaz de usuario.
        '''
        self.modelo = modelo
        self.vista = vista
    
    def boton_click(self, texto):
        '''
        Maneja el evento de clic en los botones, y actualiza en la vista.
        
        Parámetros:
            texto: El texto del botón que fue presionado.
        '''
        if texto == "Añadir Fracción":
            num = int(self.vista.obtener_entrada("numerador"))
            den = int(self.vista.obtener_entrada("denominador"))
            result_num = self.modelo.limpiar_entrada()
            result_den = self.modelo.limpiar_entrada()
            entrada = self.vista.obtener_entrada("entrada")
            result_entrada = self.modelo.añadir_fraccion(entrada, num, den)
            result = self.vista.obtener_entrada()
        
        elif texto == "Limpiar Pantalla":
            result_num = self.modelo.limpiar_entrada()
            result_den = self.modelo.limpiar_entrada()
            result_entrada = self.modelo.limpiar_entrada()
            result = self.modelo.limpiar_entrada()

        elif texto == "Resultado":
            result_num = self.vista.obtener_entrada("numerador")
            result_den = self.vista.obtener_entrada("denominador")
            entrada = self.vista.obtener_entrada("entrada")
            result_entrada = entrada
            result = self.modelo.evaluar(entrada)

        elif texto == "Comparar Mayor a Menor":
            result_num = self.vista.obtener_entrada("numerador")
            result_den = self.vista.obtener_entrada("denominador")
            entrada = self.vista.obtener_entrada("entrada")
            result_entrada = entrada
            result = self.modelo.comparar_mayor_a_menor()

        elif texto == "Comparar Menor a Mayor":
            result_num = self.vista.obtener_entrada("numerador")
            result_den = self.vista.obtener_entrada("denominador")
            entrada = self.vista.obtener_entrada("entrada")
            result_entrada = entrada
            result = self.modelo.comparar_menor_a_mayor()

        else:
            result_den = self.vista.obtener_entrada("denominador")
            result_num = self.vista.obtener_entrada("numerador")
            result_entrada = self.vista.obtener_entrada("entrada") + texto
            result = self.vista.obtener_entrada()

        self.vista.mostrar_resultado(result_num, result_den, result_entrada, result)