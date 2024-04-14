#librerias
from conexion import conexiones
import psycopg2
import io
import os
from tkinter import *
from tkinter import messagebox, ttk, PhotoImage, font
from datetime import datetime
from registrar import registrar
from InicioSesion import iniciarSesion
#conexion
conexion = conexiones()
#uso de cursor
cursor= conexion.cursor()

#clase
class Forma(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Login")
        self.geometry("901x563")
        self.config(bg="#3c096c")
        self.base_font = font.Font(family="Helvetica", size=30, weight="normal", slant="roman")
        self.custom_font = self.base_font.copy();self.custom_font2 = self.base_font.copy()
        self.custom_font.configure(size=30, weight="bold") #underline=1
        self.custom_font2.configure(size=15, weight="bold") #underline=1
        self.l1= Label(self, text="Login", font=self.custom_font, bg="#3c096c", fg="white").place(x=395, y=100)
        self.l2= Label(self, text="ingrese su codigo:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=365, y=200)
        self.e1= Entry(width=35); self.e1.place(x=355,y=230)
        self.l3= Label(self, text="ingrese su contraseña:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=350, y=270)
        self.e2= Entry(width=35, show="*"); self.e2.place(x=355,y=300)
        self.btn1= Button(text="ingresar", font=("Arial", 15),fg="white" ,width=19, bg="#7b2cbf", command=lambda:self.Login()).place(x=355,y=340) #height=3,
        self.btn2= Button(text="registrarse", font=("Arial", 15),fg="white" ,width=19, bg="#9d4edd", command=lambda:self.Registrarse()).place(x=355,y=390) #height=3,
        self.mainloop()


    def Login(self):
        #validacion del usuario y contraseña
        self.codigo = str(self.e1.get())
        self.contraseña = str(self.e2.get())
        login = iniciarSesion(self.codigo, self.contraseña)
        if login == True:
            self.destroy()
            ventana= MenuPrincipal()
            

    def Registrarse(self):
        self.destroy()
        ventana= Registrarse()


class Registrarse(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Registro")
        self.geometry("901x563")
        self.config(bg="#3c096c")
        self.base_font = font.Font(family="Helvetica", size=30, weight="normal", slant="roman")
        self.custom_font = self.base_font.copy();self.custom_font2 = self.base_font.copy()
        self.custom_font.configure(size=30, weight="bold") #underline=1
        self.custom_font2.configure(size=15, weight="bold") #underline=1
        self.l1= Label(self, text="Registro", font=self.custom_font, bg="#3c096c", fg="white").place(x=375, y=100)
        self.l2= Label(self, text="ingrese su nombre:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=365, y=200)
        self.e1= Entry(width=35); self.e1.place(x=355,y=230)
        self.l3= Label(self, text="ingrese su contraseña:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=350, y=270)
        self.e2= Entry(width=35,show="*"); self.e2.place(x=355,y=300)
        self.l3= Label(self, text="ingrese su clasificacion:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=350, y=340)
        self.e3= Entry(width=35); self.e3.place(x=355,y=370)
        self.btn1= Button(self, text="registrarse", font=("Arial", 15),fg="white" ,width=19, bg="#9d4edd", command=lambda:self.registro()).place(x=355,y=410) 
        self.mainloop()

    def registro(self):
        self.nombre =self.e1.get()
        self.contraseña = self.e2.get()
        self.clasificacion = self.e3.get()
        registrar(self.nombre, self.contraseña, self.clasificacion)


    def Menu(self):
        self.destroy()
        ventana= MenuPrincipal()

class MenuPrincipal(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Menu Principal")
        self.geometry("901x563")
        self.config(bg="#3c096c")
        self.base_font = font.Font(family="Helvetica", size=30, weight="normal", slant="roman")
        self.custom_font = self.base_font.copy();self.custom_font2 = self.base_font.copy()
        self.custom_font.configure(size=30, weight="bold") #underline=1
        self.custom_font2.configure(size=15, weight="bold") #underline=1

        self.l1= Label(self, text="Restaurante chilerisimo", font=self.custom_font, bg="#3c096c", fg="white").place(x=20, y=20)
        self.style= ttk.Style()
        self.style.configure('TFrame', background="#5a189a", foreground="#5a189a" )

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand="yes")
        self.notebook.config(width="850", height="450")
        self.notebook.place(x=20,y=80)

        self.style.configure('TFrame.TFrame', background="#3c096c", foreground="#5a189a" )
        self.tab1=ttk.Frame(self.notebook, style='TFrame.TFrame')
        #self.tab1.configure('TFrame', background="#5a189a")
        self.tab2=ttk.Frame(self.notebook)
        self.style.configure('TFrame.TFrame.TFrame', background="#9d4edd", foreground="#5a189a" )
        self.tab3=ttk.Frame(self.notebook,style='TFrame.TFrame.TFrame')

        self.notebook.add(self.tab1, text="Inicio")
        self.notebook.add(self.tab2, text="areas")
        self.notebook.add(self.tab3, text="idk")
        
        
        #self.style.theme_use(self, bg="#5a189a")

        #self.l2= Label(self, text="ingrese su nombre:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=365, y=200)
        #self.e1= Entry(width=35); self.e1.place(x=355,y=230)
        #self.l3= Label(self, text="ingrese su contraseña:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=350, y=270)
        #self.e2= Entry(width=35); self.e2.place(x=355,y=300)
        #self.l3= Label(self, text="ingrese su clasificacion:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=350, y=340)
        #self.e2= Entry(width=35); self.e2.place(x=355,y=370)
        #self.btn1= Button(text="registrarse", font=("Arial", 15),fg="white" ,width=19, bg="#9d4edd").place(x=355,y=410) 
        self.mainloop()




#cerrar conexion y cursor

conexion.close()

v=Forma()
v.mainloop()