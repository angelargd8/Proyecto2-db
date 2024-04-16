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
import pedidos
#-----------------------------------------------------------------
from ImpresionFactura import impresionFactura
#-----------------------------------------------------------------
#conexion
conexion = conexiones()
#uso de cursor
cursor= conexion.cursor()

Cocina = Pantallas(cursor, conexion, 'comida')
Bar = Pantallas(cursor, conexion,'bebida')

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
        #-----------------------------------------------------------------


        self.notebook.add(self.tab1, text="Pedido")
        self.notebook.add(Bar.Cocina(self.notebook,'TFrame.TFrame.TFrame'), text="Bar")
        self.notebook.add(Cocina.Cocina(self.notebook,'TFrame.TFrame.TFrame'), text="Cocina")
        #-----------------------------------------------------------------
        self.notebook.add(self.tab4, text="Impresion factura")
    
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
        elif rol == "gerente":
            self.salir()
        elif rol == "recepcionista":
            self.salir()
        elif rol == "personal":
            self.salir()
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
        self.areas = ["Patio","Salon 1","Salon 2","Pergola"] # se puede sacar del query de la base de datos

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

        self.mesas = []
        cont = 1
        self.ordenes = [] # lista de botones de ordenes
        
        for j in range(len(self.cantMesas)):
            Label(self.pantallas[j], text=self.areas[j], font=self.custom_font, bg="#3c096c", fg="white").place(x=30, y=10)
            Label(self.pantallas[j], text="Capacidad", font=self.custom_font2, bg="#3c096c", fg="white").place(x=220, y=45)
            self.ordenesS1 = []
            numeros = []
            
            for i in range(self.cantMesas[j]):
                numeros.append(cont)
                cont += 1
                Label(self.pantallas[j], text="Mesa "+str(i+1)).place(x=20, y=80+(i*30))
                
            for i in range(self.cantMesas[j]):
                bt1 = Button(self.pantallas[j], text="Agregar Orden ", width=15, background="#3c096c", fg= "white", command=lambda j=j,i=i:self.llamar_boton(j,i))
                bt1.place(x=100, y=75+(i*30))
                self.ordenesS1.append(bt1)

            self.mesas.append(numeros)
            self.ordenes.append(self.ordenesS1)
        print(self.mesas)
        for j in range(len(self.cantMesas)):
            for i in range(self.cantMesas[j]):
                Label(self.pantallas[j], text=pedidos.capacidadPersonas(self.mesas[j][i])).place(x=270, y=80+(i*30))

        self.actualizar_ordenes()
        self.No_orden_query = pedidos.obtenerOrden() # query que obtiene el numero de orden actual
        
        # print(self.ordenesactuales) // este es la lista de ordenes actuales, hay que actualizarla con la info de la base de datos 
        
       
    def actualizar_ordenes(self): # actualizar con lo que ya esta en la base de datos
        ordenes = pedidos.ordenesActuales()
        print(ordenes , "ordenes")
        for a in range(len(ordenes)):
            mesa = ordenes[a][1]
            j,i = pedidos.encontrarMesa(self.mesas, mesa)
            self.ordenes[j][i].config(text="Orden "+str(ordenes[a][0]))
            self.ordenesactuales[j][i] = ordenes[a][0]
            print(ordenes[a][0], "orden")
        print(self.ordenesactuales)


    def llamar_boton(self, j, i): # valida si la orden ya esta creada o hay que crearla 
        if self.ordenes[j][i].cget("text") == "Agregar Orden ":
            self.pestaña_orden(j,i,1)# se le pasa 1 cuando se acaba de crear, de lo contrario no se le pasa nada
        elif self.ordenes[j][i].cget("text") == "No disponible":
            messagebox.showinfo("Info", "Mesa no disponible")
        else:
            self.pestaña_orden(j,i)
    
    
    def crear_orden(self,j,i,mesasJuntas=False,mesaJunta = None,a=None): # cuando ingresa un cliente al restaurante se le crea la cuenta
        print(j,i)
        # crear nueva cuenta 
        # informacion de orden 
        mesero = self.MeseroEntry.get()
        mesa = self.mesas[j][i]
        personas = self.Cantidad_personas.get()
        print("mesero: ",mesero,", mesa: ", mesa,", personas: ", personas)

        if (pedidos.crearPedido(int(mesero), int(mesa), int(personas),mesasJuntas,mesaJunta) ):
            self.No_orden_query = pedidos.obtenerOrden() 
            self.ordenesactuales[j][i] = self.No_orden_query
            print(self.ordenesactuales)
            self.ordenes[j][i].config(text="Orden "+str(self.No_orden_query)) # se remplaza por el query
            
            if (mesasJuntas):
                
                self.ordenes[j][pedidos.encontrarMesa2(self.mesas, int(mesaJunta))].config(text="No disponible")
            # query para crear la orden
            self.vent.destroy()
        else:
            messagebox.showerror("Error", "No se pudo crear pedido")

   
    def pestaña_orden(self,j,i, NoOrden=0): # i es el numero de mesa / si no se le pasa el numero, la cuenta ya existe
        self.vent = Toplevel()
        Label(self.vent, text="No. Mesa").place(x=50, y=20)
        Label(self.vent,width=10, text = str(i+1)).place(x=150, y=20)
        Label(self.vent, text="No. Orden").place(x=50, y=50)

        temp = self.No_orden_query + 1  # por si decide cancelar la orden 
        Label(self.vent, width=10,text=str(temp)).place(x=150, y=50)

        Label(self.vent, text="Mesero").place(x=50, y=80)
        self.MeseroEntry = Entry(self.vent,width=10)
        self.MeseroEntry.place(x=150, y=80)
        Label(self.vent, text="No. Personas").place(x=50, y=110)
        self.Cantidad_personas = Entry(self.vent,width=10)
        self.Cantidad_personas.place(x=150, y=110)

        
        if NoOrden == 1: # primera vez que se crea 
            self.vent.title("Crear orden")
            self.vent.geometry("500x300")
            Button(self.vent, text="Guardar Orden", command=lambda  j=j,i=i:self.crear_orden(j,i)).place(x=100, y=220)
            Button(self.vent, text="Cancelar", command=lambda  j=j,i=i,ventana = self.vent:self.cerrar_pedido(j,i,self.vent)).place(x=350, y=220)
            if self.mesas[j][i] in pedidos.mesasMover():
                Button(self.vent, text="Juntar mesa", command=lambda  j=j,i=i:self.mover_mesa(j,i)).place(x=200, y=220)
        else:
            self.vent.geometry("500x400")
            self.vent.title("Modificar orden")
            Label(self.vent, text="Ordenes").place(x=50, y=140)
            self.text3 = Text(self.vent,width=30, height=10)
            self.text3.place(x=150, y=140)
            orden = self.ordenesactuales[j][i]
            Label(self.vent, width=10,text=str(orden)).place(x=150, y=50)
            # print(orden)
            self.text3.insert(INSERT, pedidos.listadoOrden(orden))
            self.text3.config(state = DISABLED)
            info = pedidos.ordenEspecifica(orden)
            print(info)
            self.MeseroEntry.insert(0, info[2])
            self.Cantidad_personas.insert(0, info[3])
            self.MeseroEntry.config(state=DISABLED)
            self.Cantidad_personas.config(state=DISABLED)
            Button(self.vent, text="Añadir a la orden", command=lambda  j=j,i=i:self.añadir_pedido(j,i)).place(x=150, y=320)
            Button(self.vent, text="Cerrar cuenta", command=lambda  j=j,i=i,ventana = self.vent:self.cerrar_pedido(j,i,self.vent)).place(x=400, y=50)

    def mover_mesa(self,j,i):
        self.l = Toplevel()
        self.l.title("Juntar mesa")
        self.l.geometry("500x200")
        Label(self.l, text="Mesas disponibles").place(x=50, y=20)
        print(pedidos.mesasDispo(j+1,self.mesas[j][i]),j+1)
        self.comboBox = ttk.Combobox(self.l, values = pedidos.mesasDispo(j+1,self.mesas[j][i]))
        self.comboBox.place(x=200, y=20)
        self.comboBox.bind("<<ComboboxSelected>>", self.on_select)
        self.mesa2 = ''
        
              
        Button(self.l, text="Juntar",command=lambda j=j, i=i, mesasJuntas=True, mesaJunta=self.mesa2:self.crear_orden(j,i,True,self.mesa2)).place(x=200, y=100)

    
    def on_select(self,event):
        self.mesa2 = self.comboBox.get()
        print("Seleccionado:", self.mesa2)
        


    def añadir_pedido(self,j,i): # se añade un pedido a la cuenta
        self.add = Toplevel()
        self.add.title("crear")    
        self.add.geometry("600x150")
        self.add["bg"] = "blueviolet"

        self.comida = Button(self.add, text="COMIDA", height=5, width=10, command=lambda j=j,i=i: self.showElement('comida',j,i));self.comida.place(x=200,y=5)
        self.bebidas = Button(self.add, text="BEBIDAS",height=5, width=10, command=lambda j=j,i=i: self.showElement('bebida',j,i));self.bebidas.place(x=350,y=5)

    def showElement(self,tipo,j,i):
        self.comida.destroy()
        self.bebidas.destroy()
        self.add.geometry("700x400")

        cursor.execute(f"select * from menu where tipo_elemento = '{tipo}'")
        resultados = cursor.fetchall()
        
        index = 0
        x=10
        y= 5
        for r in resultados:
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
            canvas.create_text(80,110,text=r[1], fill="white")
            canvas.create_text(80,130,text=f"Precio: {r[4]}", fill="White")
            canvas.place(x=x,y=y)
            print(r[0])
            canvas.bind("<Button-1>", lambda event, r = r: self.apacharMenu(r[0],j,i))
            x+=170
            if(x > 600):
                x = 10
                y +=170
            index+=1


    def apacharMenu(self, idElemento,j,i):
        # print(f"Elemento Apachado: {idElemento}")
        # print(f"Orden {self.ordenesactuales[j][i]}")
        pedidos.añadirPedido(idElemento, self.ordenesactuales[j][i])
        self.text3.delete(1.0, END)
        self.text3.insert(INSERT, pedidos.listadoOrden(self.ordenesactuales[j][i]))
   
    def factura(self,j,i):
        self.l = Toplevel()
        self.l.title("Datos Factura")
        self.l.geometry("500x200")
        
        Label(self.l, text="Ingrese el nit").place(x=50, y=50)
        self.nit = Entry(self.l,width=10)
        self.nit.place(x=200, y=50)
        Label(self.l, text="Ingrese el nombre").place(x=50, y=80)
        self.nombre = Entry(self.l,width=10)
        self.nombre.place(x=200, y=80)
        Label(self.l, text="Ingrese la direccion").place(x=50, y=110)
        self.direccion = Entry(self.l,width=10)
        self.direccion.place(x=200, y=110)
        orden = self.ordenesactuales[j][i]
        self.ordenesactuales[j][i] = 0 # borra la orden de la mesa
    

        Button(self.l, text="Generar Factura",command=lambda orden = orden, v= self.l:self.encuesta(orden,self.l)).place(x=200, y=140)


    def encuesta(self, orden,v):
        pedidos.insertarFactura(orden, self.nit.get(),self.nombre.get(), self.direccion.get())
        v.destroy()
        self.l = Toplevel()
        self.l.title("Encuesta")
        self.l.geometry("500x200")
        
        Label(self.l, text="Ingrese a su mesero").place(x=50, y=50)
        self.mesero = Entry(self.l,width=10)
        self.mesero.place(x=200, y=50)
        
        Label(self.l, text="1 - 5 amabilidad").place(x=50, y=80)
        self.amabilidad = Entry(self.l,width=10)
        self.amabilidad.place(x=200, y=80)
        Label(self.l, text="1 - 5 exactitud").place(x=50, y=110)
        self.ex = Entry(self.l,width=10)
        self.ex.place(x=200, y=110)
        Button(self.l, text="Enviar",command=lambda:self.enviar()).place(x=200, y=140)
        
    def enviar(self):
        mesero = self.mesero.get()
        amabilidad = self.amabilidad.get()
        ex = self.ex.get()
        print("h0aaa ",mesero, amabilidad, ex)
        pedidos.insertarEncuesta(mesero, amabilidad, ex)




    def cerrar_pedido(self,j,i, ventana): # se cierra la cuenta y se genera factura, ya no se pueden hacer modificaciones
        # se modifica la cuenta a cerrada
        pedidos.cerrarCuenta(self.ordenesactuales[j][i])
        self.ordenes[j][i].config(text="Agregar Orden ")
        ventana.destroy()
        self.factura(j,i)
        
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