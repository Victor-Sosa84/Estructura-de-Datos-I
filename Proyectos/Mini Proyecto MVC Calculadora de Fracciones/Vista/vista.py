from tkinter import Frame, Label, Entry, Button

class class_Vista:
    def __init__(self, ventana, controlador):
        '''
        Clase que representa la vista principal de la aplicación
        e instanciación de componentes.
        
        Parámetros:
            ventana: La ventana principal de la aplicación (objeto Tk).
            controlador: La instancia del controlador, para manejar eventos.
        '''
        self.ventana = ventana
        self.controlador = controlador
        self.vista = self
        self.centrar_ventana()
        self.crear_componentes()
        
    def centrar_ventana(self):
        '''Centrar la ventana en la pantalla.'''
        ventana_width = 850
        ventana_height = 600
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()           
        x = (screen_width // 2) - (ventana_width // 2)
        y = (screen_height // 2) - (ventana_height // 2)
        self.ventana.geometry(f"{ventana_width}x{ventana_height}+{x}+{y}")
    
    def obtener_entrada(self, entrada=None):
        '''Obtener el texto ingresado en la entrada.'''
        if entrada == 'numerador':
            return self.numerador.get()
        elif entrada == 'denominador':
            return self.denominador.get()
        elif entrada == "entrada":
            return self.entrada.get()
        else:
            return self.resultado.get()

    def crear_componentes(self):
        '''Crear los componentes de la interfaz gráfica.'''

        fuente = "Consolas"
        letra = "#d0edfe"
        fuente_label = ("Consolas", 17)
        

        self.ventana.title("Menú Principal")
        self.ventana.config(bg="#11212d")

        Label(self.ventana, text="Calculadora de Fracciones", font=(fuente, 32, "bold italic underline"), 
            bg="#11212d", fg=letra).pack(pady=20)
        
        frame_numerador = Frame(self.ventana, bg="#11212d")
        frame_numerador.pack(pady=1)
        Label(frame_numerador, text="Numerador:", font=fuente_label,
            bg="#11212d", fg=letra).pack(side="left")
        self.numerador = Entry(frame_numerador, width=7, borderwidth=2, font=(fuente, 15), 
                            bg="#4a5c6a", fg=letra, insertbackground=letra)
        self.numerador.pack(side="left", padx=5)

        frame_denominador = Frame(self.ventana, bg="#11212d")
        frame_denominador.pack(pady=1)
        Label(frame_denominador, text="Denominador:", font=fuente_label, 
            bg="#11212d", fg=letra).pack(side="left")
        self.denominador = Entry(frame_denominador, width=7, borderwidth=2, font=(fuente, 15), 
                                bg="#4a5c6a", fg=letra, insertbackground=letra)
        self.denominador.pack(side="left", padx=5)

        frame_entrada = Frame(self.ventana, bg="#11212d")
        frame_entrada.pack(pady=1)
        Label(frame_entrada, text="Fracciones añadidas:", font=fuente_label, 
            bg="#11212d", fg=letra).pack(side="left")
        self.entrada = Entry(frame_entrada, width=28, borderwidth=2, font=(fuente, 15), 
                            bg="#4a5c6a", fg=letra, insertbackground=letra)
        self.entrada.pack(side="left", padx=5)

        frame_resultado = Frame(self.ventana, bg="#11212d")
        frame_resultado.pack(pady=1)
        Label(frame_resultado, text="Resultado:", font=fuente_label, 
            bg="#11212d", fg=letra).pack(side="left")
        self.resultado = Entry(frame_resultado, width=26, borderwidth=2, font=(fuente, 15), 
                            bg="#4a5c6a", fg=letra, insertbackground=letra)
        self.resultado.pack(side="left", padx=5, pady=20)

        frame_botones = Frame(self.ventana, bg="#11212d")
        frame_botones.pack(pady=1)

        botones = [
            ["Añadir Fracción"],
            ["+", "-", "×", "÷"],
            ["Limpiar Pantalla", "Resultado"], 
            ["Comparar Mayor a Menor", "Comparar Menor a Mayor"]
        ]

        for fila in botones:
            fila_frame = Frame(frame_botones, bg="#11212d")
            fila_frame.pack(pady=5)
            for texto in fila:
                if texto in "+-×÷":
                    boton_op = Button(fila_frame, text=texto, width=12, height=2, font=(fuente, 15, "bold"), 
                            bg="#253745", fg=letra, borderwidth=4, border=5,
                            activebackground="#4a5c6a", activeforeground=letra,
                            command=lambda t=texto: self.controlador.boton_click(t))
                    boton_op.pack(side="left", padx=5)
                else:
                    boton = Button(fila_frame, text=texto, width=22, height=2, font=(fuente, 13, "bold"), 
                            bg="#253745", fg=letra, borderwidth=4, border=5,
                            activebackground="#4a5c6a", activeforeground=letra,
                            command=lambda t=texto: self.controlador.boton_click(t))
                    boton.pack(side="left", padx=5)

    def mostrar_resultado(self, resultado_numerador, resultado_denominador, resultado_entrada, resultado):
            '''
            Mostrar resultados luego de haber presionado un botón en la interfaz.
            
            Parámetros:
                resultado_numerador (str): El texto para el numerador.
                resultado_denominador (str): El texto para el denominador.
                resultado_entrada (str): El texto para la entrada principal.
                resultado (str): El texto para el resultado.
            '''
            self.numerador.delete(0, 'end')
            self.denominador.delete(0, 'end')
            self.entrada.delete(0, 'end')
            self.resultado.delete(0, 'end')
            self.numerador.insert(0, resultado_numerador)
            self.denominador.insert(0, resultado_denominador)
            self.entrada.insert(0, resultado_entrada)
            self.resultado.insert(0, resultado)


