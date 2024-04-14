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
        login_resultado1, rol = iniciarSesion(self.codigo, self.contraseña)
        if login_resultado1== True:
            self.destroy()
            print(rol)
            ventana= MenuPrincipal(rol)

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
        self.e2= Entry(width=35, show="*"); self.e2.place(x=355,y=300)
        self.l3= Label(self, text="ingrese su clasificacion:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=350, y=340)
        self.e2= Entry(width=35); self.e2.place(x=355,y=370)
        self.btn1= Button(self, text="registrarse", font=("Arial", 15),fg="white" ,width=19, bg="#9d4edd", command=lambda:self.Menu()).place(x=355,y=410) 
        self.mainloop()

    

    def Menu(self):
        self.destroy()
        ventana= MenuPrincipal()

class MenuPrincipal(Tk):
    def __init__(self, rol):
        Tk.__init__(self)
        self.title("Menu Principal")
        self.geometry("901x563")
        self.config(bg="#3c096c")
        self.base_font = font.Font(family="Helvetica", size=30, weight="normal", slant="roman")
        self.custom_font = self.base_font.copy();self.custom_font2 = self.base_font.copy()
        self.custom_font.configure(size=30, weight="bold") #underline=1
        self.custom_font2.configure(size=15, weight="bold") #underline=1

        self.l1= Label(self, text="Restaurante chilerisimo 🤑", font=self.custom_font, bg="#3c096c", fg="white").place(x=20, y=20)
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

        self.notebook.add(self.tab1, text="Pedido")
        self.notebook.add(self.tab2, text="Bar")
        self.notebook.add(self.tab3, text="Cocina")

        self.mostrar_objetos(rol)

    def crear_tab1(self):
        # ----- tab 1 -------
        self.l1= Label(self.tab1, text="Mesas", font=self.custom_font, bg="#3c096c", fg="white").place(x=20, y=20)
        Button(self.tab1, text="Deshabilitar mesa").place(x=250, y=30)
        for i in range(7):
            Label(self.tab1, text="Mesa "+str(i+1)).place(x=20, y=100+(i*30))
        
        self.ordenes = []
        for i in range(7):
            bt1 = Button(self.tab1, text="Agregar Orden "+str(i+1), width=15, background="#3c096c", fg= "white", command=lambda i=i:self.crear_orden(i))
            bt1.place(x=100, y=95+(i*30))
            self.ordenes.append(bt1)

        # ordenes[0].config(command=lambda:self.crear_orden(), text=" Orden 1")
    

    def mostrar_objetos(self, rol):
        if rol == "mesero":
            pass
        elif rol == "cocinero":
            pass
        elif rol == "admin" or rol == "administrador":
            self.crear_tab1()
        elif rol == "gerente":
            pass
        elif rol == "recepcionista":
            pass
        elif rol == "personal":
            pass


    def crear_orden(self,i): # cuando ingresa un cliente al restaurante se le crea la cuenta
        self.ordenes[i].config(text="Orden "+str(i+1), command=lambda i=i:self.modificar_orden(i))
        self.vent = Toplevel()
        self.vent.title("Crear orden")
        self.vent.geometry("500x400")
        # informacion de orden 

        Label(self.vent, text="No. Mesa").place(x=50, y=20)
        Label(self.vent,width=10, text = str(i+1)).place(x=150, y=20)
        Label(self.vent, text="No. Orden").place(x=50, y=50)
        self.text1 = Entry(self.vent,width=10)
        self.text1.place(x=150, y=50)
        Label(self.vent, text="Mesero").place(x=50, y=80)
        self.text2 = Entry(self.vent,width=10)
        self.text2.place(x=150, y=80)
        Label(self.vent, text="Hora").place(x=50, y=110)
        hora = datetime.now().strftime("%H:%M:%S")
        Label(self.vent,width=10, text = hora).place(x=140, y=110)
        Label(self.vent, text="Orden").place(x=50, y=140)
        self.text3 = Text(self.vent,width=30, height=10)
        self.text3.place(x=150, y=140)
        Button(self.vent, text="Añadir a la orden", command=lambda i=self.text1.get():self.añadir_pedido(self.text1.get())).place(x=200, y=320)


    def añadir_pedido(self, i): # se añade un pedido a la cuenta
        # print(i)        
        pass

    def modificar_orden(self,i): # cuando se quiere tomar la orden de un cliente, agregar comidas y bebidas
        # se debe de validar que la cuenta este abierta 
        self.vent = Toplevel()
        self.vent.title("Modificar orden")
        self.vent.geometry("500x400")
        # informacion de orden 

        Label(self.vent, text="No. Mesa").place(x=50, y=20)
        Label(self.vent,width=10, text = str(i+1)).place(x=150, y=20)
        Label(self.vent, text="No. Orden").place(x=50, y=50)
        self.text1 = Text(self.vent,width=10, height=1)
        self.text1.place(x=150, y=50)
        Label(self.vent, text="Mesero").place(x=50, y=80)
        self.text2 = Text(self.vent,width=10, height=1)
        self.text2.place(x=150, y=80)
        Label(self.vent, text="Hora").place(x=50, y=110)
        hora = datetime.now().strftime("%H:%M:%S")
        Label(self.vent,width=10, text = hora).place(x=140, y=110)
        Label(self.vent, text="Orden").place(x=50, y=140)
        self.text3 = Text(self.vent,width=30, height=10)
        self.text3.place(x=150, y=140)

        Button(self.vent, text="Añadir pedido", command=lambda:self.añadir_pedido()).place(x=200, y=350)
        Button(self.vent, text="Cerrar cuenta", command=lambda:self.cerrar_pedido()).place(x=350, y=20)


    def cerrar_pedido(self): # se cierra la cuenta y se genera factura, ya no se pueden hacer modificaciones
        # se modifica la cuenta a cerrada
        pass
        
        self.mainloop()




#cerrar conexion y cursor
cursor.close()
conexion.close()

v=Forma()
v.mainloop()