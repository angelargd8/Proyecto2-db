import psycopg2
from tkinter import *
from tkinter import messagebox
from conexion import conexiones
#from main import Forma

#parte que va en main.py, pero para que no se tilinee, lo pondré aqui
"""
        self.l2= Label(self, text="ingrese su codigo:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=365, y=200)
        
def Login(self):
        #validacion del usuario y contraseña
        self.codigo = str(self.e1.get())
        self.contraseña = str(self.e2.get())
        login = iniciarSesion(self.codigo, self.contraseña)
        if login == True:
            self.destroy()
            ventana= MenuPrincipal()


"""

#instanciar clase
#forma = Forma()
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
                categoria = result[4]
                messagebox.showinfo("Bienvenido!", f"Bienvenido {nombre}")
                return True, categoria

    except Exception as msg:
        messagebox.showerror("Error", "No se pudo ingresar, ingrese bien los datos")