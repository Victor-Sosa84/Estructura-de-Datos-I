import tkinter as tk
from vista import Vista
from controlador import Controlador

def main():
    root = tk.Tk()
    vista = Vista(root)
    controlador = Controlador(vista)
    vista.set_controlador(controlador)
    root.mainloop()

if __name__ == "__main__":
    main()