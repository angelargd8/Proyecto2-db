#librerias
from conexion import conexiones
import psycopg2
import io
import os
from tkinter import *
from tkinter import messagebox, ttk, PhotoImage, font
#conexion
conexion = conexiones()
#uso de cursor
cursor= conexion.cursor()

#clase
class Forma(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("901x563")#
        self.config(bg="#3c096c")
        self.base_font = font.Font(family="Helvetica", size=30, weight="normal", slant="roman")
        self.custom_font = self.base_font.copy();self.custom_font2 = self.base_font.copy()
        self.custom_font.configure(size=30, weight="bold") #underline=1
        self.custom_font2.configure(size=15, weight="bold") #underline=1
        self.l1= Label(self, text="Login", font=self.custom_font, bg="#3c096c", fg="white").place(x=395, y=100)
        self.l2= Label(self, text="ingrese su usuario:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=365, y=200)
        self.e1= Entry(width=35); self.e1.place(x=355,y=230)
        self.l3= Label(self, text="ingrese su contraseña:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=350, y=270)
        self.e2= Entry(width=35); self.e2.place(x=355,y=300)
        self.btn1= Button(text="ingresar", font=("Arial", 15),fg="white" ,width=19, bg="#7b2cbf").place(x=355,y=340) #height=3,
        


    def Login(self):
        pass

    
    def MenuPrincipal(self):
        pass

#cerrar conexion y cursor
cursor.close()
conexion.close()

v=Forma()
v.mainloop()