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
from Pantalla import Pantallas
from PIL import Image, ImageTk
#-----------------------------------------------------------------
from ImpresionFactura import impresionFactura
#-----------------------------------------------------------------
from Reporte1y2 import Reporte
#conexion
conexion = conexiones()
#uso de cursor
cursor= conexion.cursor()

Cocina = Pantallas(cursor, conexion, 'comida')
Bar = Pantallas(cursor, conexion,'bebida')
Reporte1 = Reporte(conexion,cursor,'''SELECT nombre_elemento, COUNT(*) AS numero_pedidos
FROM menu_orden mo
inner join menu m on (mo.id_elemento = m.id_elemento)
WHERE date(hora) BETWEEN 'fecha_inicio' AND 'fecha_fin'
AND estatus = 'entregada'
GROUP BY nombre_elemento
ORDER BY numero_pedidos DESC;''', "Platos mas pedidos en un rango de fechas")

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
        #-----------------------------------------------------------------
        self.custom_font3 = self.base_font.copy()
        self.custom_font3.configure(size=10, weight="bold") #underline=1
        #-----------------------------------------------------------------
        self.l1= Label(self, text="Login", font=self.custom_font, bg="#3c096c", fg="white").place(x=395, y=100)
        self.l2= Label(self, text="ingrese su codigo:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=365, y=200)
        self.e1= Entry(width=35); self.e1.place(x=355,y=230)
        self.l3= Label(self, text="ingrese su contraseña:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=350, y=270)
        self.e2= Entry(width=35, show="*"); self.e2.place(x=355,y=300)
        self.btn1= Button(text="ingresar", font=("Arial", 15),fg="white" ,width=19, bg="#7b2cbf", command=lambda:self.Login()).place(x=355,y=340) #height=3,
        self.mainloop()


    def Login(self):
        #validacion del usuario y contraseña
        self.codigo = str(self.e1.get())
        self.contraseña = str(self.e2.get())
        login_resultado1, rol = iniciarSesion(self.codigo, self.contraseña)
        if login_resultado1== True:
            self.destroy()
            ventana= MenuPrincipal(rol)
        else:
            messagebox.showerror("Error", "No se pudo ingresar, ingrese bien los datos")

    


class Registrarse(Tk):
    def __init__(self,rol):
        Tk.__init__(self)
        self.title("Registro")
        self.geometry("901x563")
        self.config(bg="#3c096c")
        self.base_font = font.Font(family="Helvetica", size=30, weight="normal", slant="roman")
        self.custom_font = self.base_font.copy();self.custom_font2 = self.base_font.copy()
        self.custom_font.configure(size=30, weight="bold") #underline=1
        self.custom_font2.configure(size=15, weight="bold") #underline=1
        self.l1= Label(self, text="Registro", font=self.custom_font, bg="#3c096c", fg="white").place(x=375, y=100)
        self.l2= Label(self, text="ingrese el nombre:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=365, y=200)
        self.e1= Entry(width=35); self.e1.place(x=355,y=230)
        self.l3= Label(self, text="ingrese la contraseña:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=350, y=270)
        self.e2= Entry(width=35, show="*"); self.e2.place(x=355,y=300)
        self.l3= Label(self, text="ingrese la clasificacion:", font=self.custom_font2, bg="#3c096c", fg="white").place(x=350, y=340)
        self.e3= Entry(width=35); self.e3.place(x=355,y=370)
        self.l4= Label(self, text="ingrese el id del area (solo si es mesero):", font=self.custom_font2, bg="#3c096c", fg="white").place(x=290, y=410)
        self.e4= Entry(width=35); self.e4.place(x=355,y=440)
        self.btn1= Button(self, text="registrarse", font=("Arial", 15),fg="white" ,width=19, bg="#9d4edd", command=lambda:self.registro(rol)).place(x=355,y=480) 
        self.mainloop()


    def registro(self, rol):
        self.nombre =self.e1.get()
        self.contraseña = self.e2.get()
        self.clasificacion = self.e3.get()
        self.id_area = self.e4.get()
        resultado = registrar(self.nombre, self.contraseña, self.clasificacion,self.id_area)
        if resultado == True:
            self.destroy()
            ventana= MenuPrincipal(rol)
        else:
            messagebox.showerror("Error", "No se pudo registrar")


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

        self.l1= Label(self, text="Restaurante chilerisimo", font=self.custom_font, bg="#3c096c", fg="white").place(x=20, y=20)
        self.style= ttk.Style()
        self.style.configure('TFrame', background="#5a189a", foreground="#5a189a" )

        self.imagenes = []

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
        #-----------------------------------------------------------------
        self.tab4=ttk.Frame(self.notebook,style='TFrame.TFrame')
        self.tab5= ttk.Frame(self.notebook,style='TFrame.TFrame')
        #-----------------------------------------------------------------


        self.notebook.add(self.tab1, text="Pedido")
        self.notebook.add(Bar.Cocina(self.notebook,'TFrame.TFrame.TFrame'), text="Bar")
        self.notebook.add(Cocina.Cocina(self.notebook,'TFrame.TFrame.TFrame'), text="Cocina")
        #-----------------------------------------------------------------
        self.notebook.add(self.tab4, text="Impresion factura")
        self.notebook.add(self.tab5, text="Reportes")
    
        self.mostrar_objetos(rol)



    def mostrar_objetos(self, rol):
        if rol == "mesero" or rol == "mesera":
            self.salir()
        elif rol == "cocinero" or rol == "cocinera":
            self.salir()
        elif rol == "admin" or rol == "administrador":
            self.crear_tab1()
            self.registrar_miembros(rol)
            self.salir()
            self.crear_tab4()
            self.crear_tab5()
        elif rol == "gerente":
            self.salir()
        elif rol == "recepcionista":
            self.salir()
        elif rol == "personal":
            self.salir()

    def crear_tab5(self):
        self.l1= Label(self.tab5, text="Reportes", font=self.custom_font, bg="#3c096c", fg="white").place(x=20, y=20)
        Button(self.tab5, text="1", font=("Arial", 9),fg="white" ,width=10, bg="#9d4edd", command=lambda:self.a()).place(x=20,y=85) 
        Button(self.tab5, text="2", font=("Arial", 9),fg="white" ,width=10, bg="#9d4edd", command=lambda:self.b()).place(x=120,y=85) 
        Button(self.tab5, text="3", font=("Arial", 9),fg="white" ,width=10, bg="#9d4edd", command=lambda:self.c()).place(x=220,y=85) 
        Button(self.tab5, text="4", font=("Arial", 9),fg="white" ,width=10, bg="#9d4edd", command=lambda:self.d()).place(x=320,y=85) 
        Button(self.tab5, text="5", font=("Arial", 9),fg="white" ,width=10, bg="#9d4edd", command=lambda:self.e()).place(x=420,y=85) 
        
        self.notebook3 = ttk.Notebook(self.tab5)
        self.notebook3.pack(fill="both", expand="yes")
        self.notebook3.config(width="700", height="300")
        self.notebook3.place(x=20,y=120)

        self.reportes = ["Reporte 1","Reporte 2","Reporte 3 ","Reporte 4", "Reporte 5"] # se puede sacar del query de la base de datos

        # agregar las pestañas de los salones
        self.pantallas2 = []
        for i in range(5):
            if i == 0:
                self.pantallas2.append(Reporte1.reporte(self.notebook3,'TFrame.TFrame.TFrame'))
            else:
                self.pantallas2.append(ttk.Frame(self.notebook3,style='TFrame.TFrame.TFrame'))
            self.notebook3.add(self.pantallas2[i], text=self.reportes[i])

        self.base_font = font.Font(family="Helvetica", size=30, weight="normal", slant="roman")
        self.custom_font3 = self.base_font.copy()
        self.custom_font3.configure(size=10, weight="bold") 


    def a(self):
        Label(self.pantallas2[0], text="los platos más pedidos:", font=self.custom_font3, bg="#3c096c", fg="white").place(x=20, y=20)
        Label(self.pantallas2[0], text="Ingrese la primera fecha:", font=self.custom_font3, bg="#3c096c", fg="white").place(x=20, y=20)
        Label(self.pantallas2[0], text="Ingrese la primera fecha:", font=self.custom_font3, bg="#3c096c", fg="white").place(x=20, y=20)
    def b(self):
        Label(self.pantallas2[1], text="Horario en el que se ingresan más pedidos:", font=self.custom_font3, bg="#3c096c", fg="white").place(x=20, y=20)
    def c(self):
        Label(self.pantallas2[2], text="Promedio de tiempo en que se tardan los clientes en comer:", font=self.custom_font3, bg="#3c096c", fg="white").place(x=20, y=20)
    def d(self):
        Label(self.pantallas2[3], text="Reporte de las quejas agrupadas por persona:", font=self.custom_font3, bg="#3c096c", fg="white").place(x=20, y=20)
    def e(self):
        Label(self.pantallas2[4], text="Reporte de las quejas agrupadas por plato:", font=self.custom_font3, bg="#3c096c", fg="white").place(x=20, y=20)

#-----------------------------------------------------------------
    def crear_tab4(self):
        self.l1= Label(self.tab4, text="Impresion de factura", font=self.custom_font, bg="#3c096c", fg="white").place(x=20, y=20)
        Button(self.tab4, text="Imprimir factura", font=("Arial", 9),fg="white" ,width=19, bg="#9d4edd", command=lambda:self.imprimir_factura()).place(x=480,y=85) 
        self.base_font = font.Font(family="Helvetica", size=30, weight="normal", slant="roman")
        self.custom_font3 = self.base_font.copy()
        self.custom_font3.configure(size=10, weight="bold") #underline=1
        self.l5= Label(self.tab4, text="Ingrese el id de la orden:", font=self.custom_font3, bg="#3c096c", fg="white").place(x=20, y=90)
        self.e5= Entry(self.tab4,width=35); self.e5.place(x=200,y=90)

        
    def imprimir_factura(self):
        self.id_orden = self.e5.get()
        resultado_impresion = impresionFactura(self.id_orden)
        if resultado_impresion[0] == True:
            self.l6= Label(self.tab4, text="Factura:", font=self.custom_font3, bg="#3c096c", fg="white").place(x=20, y=120)
            self.area_texto= Text(self.tab4, height=19, width=85,font=("Helvetica", 11))
            self.area_texto.place(x=90, y=120)
            self.nit = resultado_impresion[1]
            self.nombre_nit = resultado_impresion[2]
            self.direccion = resultado_impresion[3]
            self.tipo_pago = resultado_impresion[4]
            self.area_texto.insert(INSERT, "Nit de la orden   : %s \n" % (self.nit))
            self.area_texto.insert(INSERT, "Nombre del cliente: %s \n" % (self.nombre_nit))
            self.area_texto.insert(INSERT, "Direccion         : %s \n" % (self.direccion))
            self.area_texto.insert(INSERT, "Tipo de pago      : %s \n" % (self.tipo_pago))

            
        else:
            messagebox.showerror("Error", "No se pudo registrar")

    def salir(self):
        Button(self, text="Cerrar sesión", font=("Arial", 15),fg="white" ,width=12, bg="#240046", command=lambda:self.cerrarSesion()).place(x=640,y=20) 

    def cerrarSesion(self):
        self.destroy()
        ventana = Forma()
#-----------------------------------------------------------------



    def crear_tab1(self):

        # ----- tab 1 -------
        Label(self.tab1, text="Areas", font=self.custom_font, bg="#3c096c", fg="white").place(x=30, y=20)
        # pestañas para los salones 
        self.notebook2 = ttk.Notebook(self.tab1)
        self.notebook2.pack(fill="both", expand="yes")
        self.notebook2.config(width="700", height="300")
        self.notebook2.place(x=20,y=80)

    
        
        self.pantallas = []
        self.cantMesas = [4,4,5,4] # se puede sacar del query de la base de datos
        self.areas = ["Salon 1","Salon 2","Pergola","Terraza"] # se puede sacar del query de la base de datos

        # agregar las pestañas de los salones
        for i in range(len(self.cantMesas)):
            self.pantallas.append(ttk.Frame(self.notebook2,style='TFrame.TFrame.TFrame'))
            self.notebook2.add(self.pantallas[i], text=self.areas[i])

        self.ordenesactuales = []
        for j in range(len(self.cantMesas)):
            self.ordeness = []
            for i in range(self.cantMesas[j]):
                self.ordeness.append(0)
            self.ordenesactuales.append(self.ordeness)


        self.ordenes = []
        
        for j in range(len(self.cantMesas)):
            Label(self.pantallas[j], text=self.areas[j], font=self.custom_font, bg="#3c096c", fg="white").place(x=30, y=10)
            self.ordenesS1 = []
            for i in range(self.cantMesas[j]):
                Label(self.pantallas[j], text="Mesa "+str(i+1)).place(x=20, y=80+(i*30))
                
            for i in range(self.cantMesas[j]):
                bt1 = Button(self.pantallas[j], text="Agregar Orden ", width=15, background="#3c096c", fg= "white", command=lambda j=j,i=i:self.crear_orden(j,i))
                bt1.place(x=100, y=75+(i*30))
                self.ordenesS1.append(bt1)

                
            self.ordenes.append(self.ordenesS1)
        # al crear una nueva cuenta se remplaza 
        self.No_orden_query = 0 # borrar al tener el query 
        print(self.ordenesactuales)
        
    
    
    def crear_orden(self,j,i): # cuando ingresa un cliente al restaurante se le crea la cuenta
        print(j,i)
        # crear nueva cuenta 
        # query para obtener el numero de orden con count*
        self.No_orden_query += 1
        self.ordenesactuales[j][i] = self.No_orden_query
        print(self.ordenesactuales)

        self.ordenes[j][i].config(text="Orden "+str(self.No_orden_query)) # se remplaza por el query
        self.vent = Toplevel()
        self.vent.title("Crear orden")
        self.vent.geometry("500x400")
        # informacion de orden 
        self.pestaña_orden(j,i,1)
        # query para crear la orden

        # se le pasa 1 cuando se acaba de crear, de lo contrario no se le pasa nada
   
    def pestaña_orden(self,j,i, NoOrden=0): # i es el numero de mesa / si no se le pasa el numero, la cuenta ya existe
        Label(self.vent, text="No. Mesa").place(x=50, y=20)
        Label(self.vent,width=10, text = str(i+1)).place(x=150, y=20)
        Label(self.vent, text="No. Orden").place(x=50, y=50)
        Label(self.vent, width=10,text=str(self.No_orden_query)).place(x=150, y=50)
        no_orden = self.No_orden_query

        Label(self.vent, text="Mesero").place(x=50, y=80)
        self.text2 = Entry(self.vent,width=10)
        self.text2.place(x=150, y=80)
      
        Label(self.vent, text="Orden").place(x=50, y=110)
        self.text3 = Text(self.vent,width=30, height=10)
        self.text3.place(x=150, y=110)
        # Button(self.vent, text="Añadir a la orden", command=lambda i=self.text1.get():self.añadir_pedido(self.text1.get())).place(x=150, y=320)
        Button(self.vent, text="Guardar Orden", command=lambda No_orden=no_orden:self.guardar_pedido(no_orden)).place(x=300, y=320)
        Button(self.vent, text="Cerrar cuenta", command=lambda  j=j,i=i,ventana = self.vent:self.cerrar_pedido(j,i,self.vent)).place(x=400, y=50)

    def añadir_pedido(self, i): # se añade un pedido a la cuenta
        self.add = Toplevel()
        self.add.title("crear")    
        self.add.geometry("600x150")
        self.add["bg"] = "blueviolet"

        self.comida = Button(self.add, text="COMIDA", height=5, width=10, command=lambda: self.showElement('comida'));self.comida.place(x=200,y=5)
        self.bebidas = Button(self.add, text="BEBIDAS",height=5, width=10, command=lambda: self.showElement('bebida'));self.bebidas.place(x=350,y=5)

    def showElement(self,tipo):
        self.comida.destroy()
        self.bebidas.destroy()
        self.add.geometry("700x400")

        cursor.execute(f"select * from menu where tipo_elemento = '{tipo}'")
        resultados = cursor.fetchall()
        
        index = 0
        x=10
        y= 5
        for i in resultados:
            canvas = Canvas(self.add, width=150, height=150, background="#53007f")
        
            ruta = resultados[index][-1].split("/")

            ruta_actual = os.path.dirname(os.path.abspath(__file__))
            ruta_img = os.path.join(ruta_actual, 'img')

            archivo_buscar = ruta[1]
            ruta_archivo = os.path.join(ruta_img, archivo_buscar)

            img_data = Image.open(ruta_archivo)

            nuevo_tamanio=(100,100)
            img_data = img_data.resize(nuevo_tamanio)
            tk_img = ImageTk.PhotoImage(img_data)
            self.imagenes.append(tk_img)

            canvas.create_image(20,0, anchor=NW,image=self.imagenes[-1])
            canvas.create_text(80,110,text=i[1], fill="white")
            canvas.create_text(80,130,text=f"Precio: {i[4]}", fill="White")
            canvas.place(x=x,y=y)
            print(i[0])
            canvas.bind("<Button-1>", lambda event, i = i: self.apacharMenu(i[0]))
            x+=170
            if(x > 600):
                x = 10
                y +=170
            index+=1


    def apacharMenu(self, idElemento):
        print(f"Elemento Apachado: {idElemento}")

    def guardar_pedido(self,No_orden): # se guarda la cuenta
        self.vent = Toplevel()
        self.vent.title("Crear orden")
        self.vent.geometry("500x400")
        # informacion de orden 
        # self.pestaña_orden(i)
        # query para actualizar la orden

    def modificar_orden(self,i): # cuando se quiere tomar la orden de un cliente, agregar comidas y bebidas
        # se debe de validar que la cuenta este abierta 
        self.vent = Toplevel()
        self.vent.title("Modificar orden")
        self.vent.geometry("500x400")
        # informacion de orden 

       
    def cerrar_pedido(self,j,i, ventana): # se cierra la cuenta y se genera factura, ya no se pueden hacer modificaciones
        # se modifica la cuenta a cerrada
        self.ordenesactuales[j][i] = 0 # borra la orden de la mesa
        self.ordenes[j][i].config(text="Agregar Orden ")
        ventana.destroy()
        
    
        
        self.mainloop()

#--------------registro-------------
    def registrar_miembros(self,rol):
        self.btn2= Button(text="registrar", font=("Arial", 15),fg="white" ,width=10, bg="#9d4edd", command=lambda:self.Registrarse(rol)).place(x=510,y=20) 


    def Registrarse(self,rol):
        self.destroy()
        ventana= Registrarse(rol)





#cerrar conexion y cursor

v=Forma()
v.mainloop()

cursor.close()
conexion.close()