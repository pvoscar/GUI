from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def ingresar(*args):
    banUser = True
    banPass = True
    if usuario.get() == "":
        messagebox.showinfo(message="Ingrese el usuario", title="Mensaje Info")
        banUser = False
    if contrasenya.get() == "":
        messagebox.showinfo(message="Ingrese la contraseña", title="Mensaje Info")
        banPass = False
    if banUser and banPass:
        mess = "Usuario: " + usuario.get() + "\n"
        mess += "Contraseña: " + contrasenya.get() + "\n"
        mess += "\nDatos ingresados exitosamente"
        messagebox.showinfo(message=mess, title="Mensaje Info")
    

#Se crea el objeto ventana y se le agrega un título
raiz = Tk()  
raiz.title("Inicio de Sesión")

#Se crea el marco principal y se posiciona de tal forma que abarque toda la pantalla
marcoPrincipal = ttk.Frame(raiz, padding="15 15 15 15")
marcoPrincipal.grid(column=0, row=0)

#Se definen las variables a utilizar
usuario = StringVar()
contrasenya = StringVar()

#Se agregan los cuadros de texto al marco principal
txtUsuario = ttk.Entry(marcoPrincipal, textvariable=usuario, width=20, justify="center")
txtUsuario.grid(column=1, row=0, columnspan=2)
txtContrasenya = ttk.Entry(marcoPrincipal, textvariable=contrasenya, width=20, justify="center", show="*")
txtContrasenya.grid(column=1, row=1, columnspan=2)

#Se agregan las etiquetas al marco principal
ttk.Label(marcoPrincipal, text="Usuario:").grid(column=0, row=0, sticky=W)   #objeto anónimo
ttk.Label(marcoPrincipal, text="Contraseña:").grid(column=0, row=1, sticky=W)

#Se agrega el botón al marco principal
ttk.Button(marcoPrincipal, text="Ingresar", command=ingresar, width=8).grid(column=1, row=2, columnspan=2, sticky=E)

#Se recorre todos los widgets y se agrega espacio a la izquierda, derecha, arriba y debajo del widget
for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=7, pady=7)

#Se establece el objeto que tendrá el foco y captura el enter en la pantalla raíz
txtUsuario.focus()  
raiz.bind("<Return>", ingresar)

#Para ejecutar el bucle de eventos de Tkinter.
raiz.mainloop()

