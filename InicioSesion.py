import psycopg2
from tkinter import *
from tkinter import messagebox
from conexion import conexiones

conexion = conexiones()
cursor= conexion.cursor()

def iniciarSesion(id, contraseña):
    try:
        if id == "" or contraseña == "":
            messagebox.showerror("error","rellene todos los campos")
            return False, 'None'
        else:
            cursor.execute("select * from personal where id_personal = %s and password = %s", (id, contraseña))
            result = cursor.fetchone()
            if result == None and result== "" :
                messagebox.showerror("error","usuario o contraseña incorrectos")
                return False, 'None' 
            else:
                nombre = result[1]
                categoria = result[3]
                messagebox.showinfo("Bienvenido!", f"Bienvenido {nombre}")
                return True, categoria

    except Exception as msg:
        messagebox.showerror("Error", "No se pudo ingresar, ingrese bien los datos")