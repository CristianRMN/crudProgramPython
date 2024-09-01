import sqlite3
from tkinter import messagebox
from tkinter import *
import sys
from variablesCompartidas import miId, miNombre, miApellido, miPass, miDireccion

def conexionBBDD():
    miConexion = sqlite3.connect("usuariosBase")
    miCursor = miConexion.cursor()

    #creamos las tablas
    try:
        miCursor.execute('''create table datos_usuarios(
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     nombre_usuario VARCHAR(50),
                     apellido VARCHAR(50),
                     password VARCHAR(50),
                     direccion VARCHAR (50)
                    )
                     ''')
    
        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except:
        messagebox.showwarning("!Atención", "La BBDD ya existe")

def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor == "yes":
        sys.exit(0)


def limpiarCampos():
    miNombre.set("")
    miId.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")


def crear():
    miConexion = sqlite3.connect("usuariosBase")
    miCursor = miConexion.cursor()

    miCursor.execute("insert into datos_usuarios values(null, '" + miNombre.get() + 
                     "','" + miApellido.get()+ "','" + miPass.get() + "','" + 
                     miDireccion.get() + "')")
    
    miConexion.commit()

    messagebox.showinfo("BBDD", "registro insertado con éxito")

def leer():
    miConexion = sqlite3.connect("usuariosBase")
    miCursor = miConexion.cursor()

    miCursor.execute("select * from datos_usuarios where id =" + miId.get())

    elUsuario = miCursor.fetchall()

    for i in elUsuario:
        miId.set(i[0])
        miNombre.set(i[1])
        miApellido.set(i[2])
        miPass.set(i[3])
        miDireccion.set(i[4])
    
    miConexion.commit()

def actualizar():
    miConexion = sqlite3.connect("usuariosBase")
    miCursor = miConexion.cursor()

    miCursor.execute("update datos_usuarios set nombre_usuario = '" + miNombre.get() + 
                     "', apellido='" + miApellido.get() + 
                     "', password='" + miPass.get() + 
                     "', direccion='" + miDireccion.get() + "' where ID=" + miId.get())
    
    miConexion.commit()

    messagebox.showinfo("BBDD", "registro actualizado con éxito")


def eliminar():
    miConexion = sqlite3.connect("usuariosBase")
    miCursor = miConexion.cursor()

    miCursor.execute("delete from datos_usuarios where id=" + miId.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "registro borrado con éxito")


def ayuda():
    messagebox.showinfo("Licencia", "Programa crud hecho en visual studio code")

def acerca():
    messagebox.showinfo("preguntas", "IDE: Visual code" + "\n" + "Base de datos: Sqlite")

#consulta parametrizada
#datos = miNombre.get(),miApellido.get(),miPass.get(),miDireccion.get()
#miCursor.execute("insert into datos_usuarios values(NULL, ?, ?, ?, ?)", (datos))


        
    
    