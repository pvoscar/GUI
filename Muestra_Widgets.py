from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def guardar(*args):
    pass

def cancelar(*args):
    pass

#Se crea el objeto ventana y se le agrega un título
raiz = Tk()  
raiz.title("Muestra Widgets")
raiz.resizable(False, False)
#raiz.geometry('500x410')

#Se definen las variables a utilizar
nombre = StringVar()
aPaterno = StringVar()
aMaterno = StringVar()
correo = StringVar()
movil = StringVar()

#Se crea el marco principal
marcoPrincipal = ttk.Frame(raiz)
marcoPrincipal.grid(column=0, row=0)

#Se crea el marco secundario 1 
marcoSec1 = ttk.Frame(marcoPrincipal, relief="raised", width=400, height=300)
marcoSec1.grid(column=0, row=0, columnspan=4, rowspan=5, padx=10, pady=10)

#Se agregan los widgets al marco secundario 1
#Nombre:
ttk.Label(marcoSec1, text="Nombre:", font=('bold', 14)).grid(column=0, row=0, sticky=W)
txtNombre = ttk.Entry(marcoSec1, textvariable=nombre, width=25)
txtNombre.grid(column=1, row=0, columnspan=3, sticky=E)

#Apellido Paterno
ttk.Label(marcoSec1, text="A. Paterno:", font=('bold', 14)).grid(column=0, row=1, sticky=W)
txtAPaterno = ttk.Entry(marcoSec1, textvariable=aPaterno, width=25)
txtAPaterno.grid(column=1, row=1, columnspan=3, sticky=E)

# Apellido Materno:
ttk.Label(marcoSec1, text='A. Materno:', font=('bold', 14)).grid(column=0, row=2, sticky=W)
aMaterno = ttk.Entry(marcoSec1, textvariable=aMaterno, width=25)
aMaterno.grid(column=1, row=2, columnspan=3, sticky=E)

# Correo:
ttk.Label(marcoSec1, text='Correo:', font=('bold', 14)).grid(column=0, row=3, sticky=W)
correo = ttk.Entry(marcoSec1, textvariable=correo, width=25)
correo.grid(column=1, row=3, columnspan=3, sticky=E)

# Móvil:
ttk.Label(marcoSec1, text='Móvil:', font=('bold', 14)).grid(column=0, row=4, sticky=W)
movil = ttk.Entry(marcoSec1, textvariable=movil, width=25)
movil.grid(column=1, row=4, columnspan=3, sticky=E)

for widget in marcoSec1.winfo_children():
    widget.grid(padx=10, pady=10)


#Se crea el marco secundario 2 y se posiciona dentro del marco principal
marcoSec2 = ttk.Frame(marcoPrincipal, relief="raised")
marcoSec2.grid(column=0, row=5, columnspan=4, rowspan=2, padx=10, pady=10, sticky=EW)

#Se agregan los widgets al marco secundario 2
ttk.Label(marcoSec2, text='Aficiones:').grid(column=0, row=5, columnspan=4, sticky=W)
chkAficion1 = ttk.Checkbutton(marcoSec2, text='Leer', state='!selected').grid(column=0, row=6)
chkAficion2 = ttk.Checkbutton(marcoSec2, text='Música').grid(column=1, row=6)
chkAficion3 = ttk.Checkbutton(marcoSec2, text='Videojuegos').grid(column=2, row=6, columnspan=2)

for widget in marcoSec2.winfo_children():
    widget.grid(padx=10, pady=5)

#Se agrega el botón Guardar
ttk.Button(marcoPrincipal, text="Guardar", command=guardar).grid(column=0, row=7, pady=10)
ttk.Button(marcoPrincipal, text="Cancelar", command=cancelar).grid(column=1, row=7, columnspan=2, sticky=E, pady=10)

#Se agregan los radio botones
opSelected = StringVar()

opcion = ttk.Radiobutton(marcoPrincipal, text="Estudiante", value="Estudiante", variable=opSelected, width=15)
opcion.grid(column=4, row=1, columnspan=2, sticky=S)
opcion = ttk.Radiobutton(marcoPrincipal, text="Empleado", value="Empleado", variable=opSelected, width=15)
opcion.grid(column=4, row=2, columnspan=2)
opcion = ttk.Radiobutton(marcoPrincipal, text="Desempleado", value="Desempleado", variable=opSelected, width=15)
opcion.grid(column=4, row=3, columnspan=2, sticky=N)

#Se agrega el combo
estados = StringVar()

comboEstados = ttk.Combobox(marcoPrincipal, textvariable=estados)
comboEstados.grid(column=4, row=5, columnspan=2, rowspan=2, padx=15)
comboEstados['values'] = ("Aguascalientes", "Baja California", "Baja California Sur", "Campeche", 
                          "Coahuila", "Colima", "Chiapas", "Chihuahua", "Durango", "Distrito Federal", 
                          "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "México", "Michoacán", 
                          "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", 
                          "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", 
                          "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas")

#Para ejecutar el bucle de eventos de Tkinter.
raiz.mainloop()