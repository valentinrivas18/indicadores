import tkinter as tk
from tkinter import messagebox
from VentanaPrincipal import VentanaPrincipal
from PIL import Image, ImageTk
import mysql.connector

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("INDICA - Inicio de Sesion")
        self.root.geometry("400x400")
        self.root.configure(background='#D476F9')
        self.colorlb="#D476F9"
        self.coloruniversal="#ff8000"
        self.root.iconbitmap("imagenes/icono/icon.ico")

        # imagen del pcba
        self.imagen = Image.open("imagenes/pcba.jpg")
        self.tamano_imagen_deseado = (180, 300)
        self.imagen_redimensionada = self.imagen.resize(self.tamano_imagen_deseado)
        self.tkimagen = ImageTk.PhotoImage(self.imagen_redimensionada)

        #Creando Frame Izquierdo para la Imagen
        self.frame = tk.Frame(root, bg="white",width=200, padx=0, pady=0)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        # Mostrar la imagen en un Label del Frame
        self.label = tk.Label(self.frame, image=self.tkimagen, background="#ffffff")
        self.label.pack()
        self.label.place(x=0,y=30)

        # Creando Frame Derecho para el Formulario
        self.frameder = tk.Frame(root, bg=self.colorlb,width=200, padx=30, pady=10)
        self.frameder.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)
        
        # Todo esto debe ir dentro del frame llamado "frameder"
        

        # Label del Usuario
        self.username_label = tk.Label(self.frameder, text="Usuario:",font=("Arial","12","bold"), background=self.colorlb)
        self.username_label.pack(anchor=tk.CENTER,pady=10)
        self.username_label.place(relx=0.5, rely=0, anchor=tk.CENTER, y=60)

        # text box para ingresar usuario
        self.username_entry = tk.Entry(self.frameder, font=("Arial",12))
        self.username_entry.pack(anchor=tk.CENTER, pady=10)
        self.username_entry.place(relx=0.5, rely=0, anchor=tk.CENTER, y=100)

        # label de contraseña
        self.password_label = tk.Label(self.frameder, text="Contraseña:", font=("Arial",12,"bold"), background=self.colorlb)
        self.password_label.pack(pady=10)
        self.password_label.place(relx=0.5, rely=0, anchor=tk.CENTER, y=140)

        # label de usuarios

        self.password_entry = tk.Entry(self.frameder, show="*",font=("Arial",12))
        self.password_entry.pack(pady=20)
        self.password_entry.place(relx=0.5, rely=0, anchor=tk.CENTER, y=180)


        self.login_button = tk.Button(self.frameder, text="Iniciar Sesión", width=10, height=1,
                                font=("Arial", 12,"bold"),background=self.coloruniversal, fg="white",command=self.login)
        self.login_button.pack(pady=10)
        self.login_button.place(relx=0.5, rely=0, anchor=tk.CENTER, y=230)

        

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()


        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="valentin",
                database="indic",
                port="3307" 
            )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM administrador WHERE usuario = %s AND contrasena = %s", (username, password))
            credencial = cursor.fetchone()
            # Aquí deberías agregar la lógica de autenticación, por ejemplo, comparando con una base de datos
            if credencial:
                messagebox.showinfo("Inicio de Sesión", "Iniciaste sesión correctamente, bienvenido " + username)
                self.root.destroy()
                ventana = tk.Tk()
                app = VentanaPrincipal(ventana)
                ventana.mainloop()
            else:
                messagebox.showerror("Error", "Credenciales incorrectas")
                
        except mysql.connector.Error as err:
            messagebox.showerror("Error", "Credenciales incorrectas")

if __name__ == "__main__":
    root = tk.Tk()
    login = LoginWindow(root)
    root.mainloop()