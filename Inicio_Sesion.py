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
    
#Se crea la ventana raíz
raiz = Tk()  
raiz.title("Inicio de Sesión")

#Se definen las variables a utilizar
usuario = StringVar()
contrasenya = StringVar()

#Se crea el marco principal y se posiciona de tal forma que abarque toda la pantalla
marcoPrincipal = ttk.Frame(raiz, padding="15 15 15 15")
marcoPrincipal.grid(column=0, row=0)

#Se configura el grid
marcoPrincipal.columnconfigure(0, weight=1)
marcoPrincipal.columnconfigure(1, weight=3)

#Se agregan los widgets de usuario al marco principal
ttk.Label(marcoPrincipal, text="Usuario:").grid(column=0, row=0, sticky=E, padx=10, pady=10)
txtUsuario = ttk.Entry(marcoPrincipal, textvariable=usuario)
txtUsuario.grid(column=1, row=0, sticky=E, padx=10, pady=10)

#Se agregan los widgets de Contraseña al marco principal
ttk.Label(marcoPrincipal, text="Contraseña:").grid(column=0, row=1, sticky=E, padx=10, pady=10)
txtContrasenya = ttk.Entry(marcoPrincipal, textvariable=contrasenya, show="*")
txtContrasenya.grid(column=1, row=1, sticky=E, padx=10, pady=10)

#Se agrega el botón Ingresar al marco principal
ttk.Button(marcoPrincipal, text="Ingresar", command=ingresar).grid(column=1, row=3, sticky=E, padx=10, pady=10)

#Se establece el objeto que tendrá el foco y captura el enter en la pantalla raíz
txtUsuario.focus()  
raiz.bind("<Return>", ingresar)

#Para ejecutar el bucle de eventos de Tkinter.
raiz.mainloop()

