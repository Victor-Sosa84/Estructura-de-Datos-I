from tkinter import Button, Frame, Label, Entry

class Vista:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.entry_exp = ""
        self.label_calc = ""
        self.label_resp = ""
        self.centrar()
        self.componentes()

    def centrar(self):
        rw = 350
        rh = 300
        scw = self.root.winfo_screenwidth()
        sch = self.root.winfo_screenheight()           
        x = (scw // 2) - (rw // 2)
        y = (sch // 2) - (rh // 2)
        self.root.geometry(f"{rw}x{rh}+{x}+{y}")
    
    def press(self):
        exp = self.entry_exp.get()
        self.controlador.obt_exp(exp)
        self.label_calc.config(text=self.controlador.prefija())
        self.label_resp.config(text=self.controlador.evaluar())

    def componentes(self):
        frame_exp = Frame(self.root)
        frame_exp.pack(pady=10)

        Label(frame_exp, text="Expresión: ").pack(side="left")
        self.entry_exp = Entry(frame_exp)
        self.entry_exp.pack(side="left")


        frame_calc = Frame(self.root)
        frame_calc.pack(pady=10)

        btn_calc = Button(frame_calc,text="Calcular Expresión Prefija", command=self.press)
        btn_calc.pack(side="left", padx=10)
        self.label_calc = Label(frame_calc, text="")
        self.label_calc.pack(side="left")


        frame_resp = Frame(self.root)
        frame_resp.pack()

        Label(frame_resp, text="Respuesta Calculada: ").pack(side="left")
        self.label_resp = Label(frame_resp, text="")
        self.label_resp.pack(side="left")