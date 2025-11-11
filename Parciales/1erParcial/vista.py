from tkinter import Frame, Button, Canvas, Label

class Vista:
    def __init__(self, root):
        self.root = root
        self.controlador = None
        self.figura_actual = "Circulo"
        self.color_actual = "Rojo"
        self.iniciar()
        self.componentes()

    def set_controlador(self, controlador):
        self.controlador = controlador

    def iniciar(self):
        self.root.title("Lista Circular de Figuras")
        self.root.geometry("550x400")

    def componentes(self):
        frame = Frame(self.root)
        frame.pack(pady=10)

        Button(frame, text="<", font="normal 20 bold", command=self.atras).pack(side="left", padx=10)
        Button(frame, text=">", font="normal 20 bold", command=self.adelante).pack(side="left", padx=10)

        self.canvas = Canvas(self.root, width=300, height=200, bg="white")
        self.canvas.pack(pady=20)

        self.color_label = Label(self.root, text="Color: Rojo", font="normal 16 bold")
        self.color_label.pack()

        self.info_label = Label(
            self.root,
            text="Figuras: [Círculo, Triángulo, Rectángulo]\nColores: [Rojo, Verde, Azul]",
            font="normal 12"
        )
        self.info_label.pack(anchor="ne", padx=10, pady=5)

        self.dibujar_figura(self.figura_actual, self.color_actual)

    def _map_color(self, color_es):
        colores = {"Rojo": "red", "Verde": "green", "Azul": "blue"}
        return colores.get(color_es, "black")

    def dibujar_figura(self, figura, color_es):
        self.canvas.delete("all")
        color = self._map_color(color_es)

        if figura == "Circulo":
            self.canvas.create_oval(80, 40, 220, 180, fill=color, outline="")
        elif figura == "Triangulo":
            self.canvas.create_polygon(150, 40, 80, 180, 220, 180, fill=color, outline="")
        elif figura == "Rectangulo":
            self.canvas.create_rectangle(80, 60, 220, 160, fill=color, outline="")

        self.canvas.create_text(150, 190, text=f"{figura} {color_es}", font=("Arial", 14, "bold"))
        self.color_label.config(text=f"Color: {color_es}")
        self.figura_actual = figura
        self.color_actual = color_es

    def adelante(self):
        if self.controlador:
            figura, color = self.controlador.adelante(self.figura_actual)
            self.dibujar_figura(figura, color)

    def atras(self):
        if self.controlador:
            figura, color = self.controlador.atras(self.figura_actual)
            self.dibujar_figura(figura, color)