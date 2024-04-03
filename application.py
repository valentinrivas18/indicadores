import tkinter as tk
from VentanaInsercion import VentanaInsercion
from VentanaConsulta import VentanaConsulta

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")
        
        self.button_insercion = tk.Button(self.root, text="Abrir Ventana de Inserción", command=self.abrir_ventana_insercion)
        self.button_insercion.pack()

        self.button_consulta = tk.Button(self.root, text="Abrir Ventana de Consulta", command=self.abrir_ventana_consulta)
        self.button_consulta.pack()

    def abrir_ventana_insercion(self):
        self.ventana_insercion = tk.Toplevel(self.root)
        self.app_insercion = VentanaInsercion(self.ventana_insercion)

    def abrir_ventana_consulta(self):
        self.ventana_consulta = tk.Toplevel(self.root)
        self.app_consulta = VentanaConsulta(self.ventana_consulta)

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()