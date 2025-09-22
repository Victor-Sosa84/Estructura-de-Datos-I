import tkinter as tk
from Modelo.modelo import class_Modelo
from Vista.vista import class_Vista
from Controlador.controlador import class_Controlador      

def main():
    '''Función principal para iniciar la aplicación.'''
    
    ''' Crear la ventana principal.'''
    ventana = tk.Tk()

    ''' Crear instancias de las clases Modelo, Vista y Controlador '''
    modelo = class_Modelo()
    vista = class_Vista(ventana, None)  
    controlador = class_Controlador(modelo, vista)
    vista.controlador = controlador

    ''' Iniciar el bucle principal de la interfaz gráfica '''
    ventana.mainloop()


if __name__ == "__main__":
    ''' Ejecutar la función principal '''
    main()