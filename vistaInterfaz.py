from tkinter import *
from tkinter import messagebox
import sqlite3


root = Tk()

from funcionesInterfaz import conexionBBDD, salirAplicacion, limpiarCampos, crear
from variablesCompartidas import  miId, miNombre, miApellido, miPass, miDireccion


barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)



    

#menus de arriba --------------------------------------------------X
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu =  Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="crear", command=crear)
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="Crud", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#mitad de la aplicacion (entrys)------------------------------------------X

miFrame = Frame(root)
miFrame.pack()



cuadroID = Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=5, pady=5)

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=5, pady=5)
cuadroNombre.config(fg="red", justify="right")

cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=5, pady=5)

cuadroPassword = Entry(miFrame, textvariable=miPass)
cuadroPassword.grid(row=3, column=1, padx=5, pady=5)
cuadroPassword.config(show="*")

cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=5, pady=5)


#aqui van los label ------------------------------------------x
idLabel = Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0, padx=5, pady=5, sticky="e")

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")


apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, padx=5, pady=5, sticky="e")


passLabel = Label(miFrame, text="Password:")
passLabel.grid(row=3, column=0, padx=5, pady=5, sticky="e")


direccionlabel = Label(miFrame, text="Direccion:")
direccionlabel.grid(row=4, column=0, padx=5, pady=5, sticky="e")



#aquí van los botones --------------------------------------X

frameBotones = Frame(root)
frameBotones.pack()

botonCrear = Button(frameBotones, text="Create", command=crear)
botonCrear.grid(row=1, column=0, padx=5, pady=5, sticky="e")


botonLeer = Button(frameBotones, text="read")
botonLeer.grid(row=1, column=1, padx=5, pady=5, sticky="e")


botonActualizar = Button(frameBotones, text="Update")
botonActualizar.grid(row=1, column=2, padx=5, pady=5, sticky="e")


botonBorrar = Button(frameBotones, text="Delete")
botonBorrar.grid(row=1, column=3, padx=5, pady=5, sticky="e")

root.mainloop()
