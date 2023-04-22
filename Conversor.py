from tkinter import *
from tkinter import ttk

def calcular(*args):
    #metros.set(pies.get())
    try:
        resultado = float(pies.get()) * 0.3048
        metros.set(resultado)
    except ValueError:
        pass

raiz = Tk()  #Es un objeto ventana
raiz.title("Pies a metros")

marcoPrincipal = ttk.Frame(raiz, padding="15 15 15 15")
marcoPrincipal.grid(column=0, row=0)

pies = StringVar()
metros = StringVar()

txtPies = ttk.Entry(marcoPrincipal, textvariable=pies, width=7, justify="center")
txtPies.grid(column=1, row=0)

ttk.Label(marcoPrincipal, text="pies").grid(column=2, row=0, sticky=W)   #objeto anónimo
ttk.Label(marcoPrincipal, text="Son equivalentes a:").grid(column=0, row=1)
ttk.Label(marcoPrincipal, textvariable=metros).grid(column=1, row=1)
ttk.Label(marcoPrincipal, text="metros").grid(column=2, row=1, sticky=W)

ttk.Button(marcoPrincipal, text="Calcular", command=calcular, width=8).grid(column=2, row=2)

for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=5, pady=5)

txtPies.focus()  #Establece el objeto que tendrá el foco
raiz.bind("<Return>", calcular)  #Captura el enter en la pantalla raíz

raiz.mainloop()