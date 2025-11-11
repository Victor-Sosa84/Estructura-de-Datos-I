import tkinter as tk
from vista.vista import Vista
from controlador.controlador import Controlador
from modelo.modelo import Modelo

def main():
    root = tk.Tk()
    
    modelo = Modelo()
    vista = Vista(root, None)
    controlador = Controlador(Vista, modelo)
    vista.controlador = controlador
    
    root.mainloop()

if __name__ == "__main__":
    main()