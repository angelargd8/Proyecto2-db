from tkinter import *
from tkinter import messagebox, ttk, PhotoImage, font
from datetime import datetime
import os
from PIL import Image, ImageTk
import requests




class Pantallas():
    def __init__(self,_cursor, _conn, _tipo):
        #bebida
        #comida
        self.cursor = _cursor
        self.conn = _conn
        self.imagenes = []
        self.itemsCocina = []
        self.displayItems= []
        self.tipo = _tipo
        self.objetos = set()


    def onClickCanvas(self,elemento,idOrden,hora, canvas):
        #entregada
        self.cursor.execute(f"update menu_orden set estatus = 'entregada' where id_elemento = '{elemento}' and id_orden = {idOrden} and hora = '{hora}'")
        self.conn.commit()
        index = self.displayItems.index(canvas)
        canvas.destroy()
        self.displayItems.pop(index)
        for i in range(index, len(self.displayItems)):
            x = self.displayItems[i].winfo_x()
            y = self.displayItems[i].winfo_y()

            if x == 10:
                x = 690
                y -= 150
            else:
                x -= 170

            self.displayItems[i].place(x=x, y=y)

    
    def showObject(self, elemento,idOrden,hora,positionx, positiony):
        canvas = Canvas(self.frameK, width=150, height=120, background="#53007f") 
        self.cursor.execute(f'select * from menu where id_elemento = {elemento}')
        resultados = self.cursor.fetchall()
        ruta = resultados[0][-1].split("/")

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
        canvas.create_text(80,110,text=resultados[0][1], fill="white")
        canvas.place(x=positionx,y=positiony)
        canvas.bind("<Button-1>", lambda event: self.onClickCanvas(elemento,idOrden, hora,canvas))
        self.displayItems.append(canvas)

    def create_canvas(self, i):
        if(len(self.displayItems)>1):
            x = self.displayItems[-1].winfo_x()
            y = self.displayItems[-1].winfo_y()
        else:
            x = -160
            y = 5

        if((x+170) > 850):
            x = 10
            y = y+150
        else:
            x += 170

        canvas = Canvas(self.frameK, width=150, height=120, background="#53007f")

        ruta = i[-1].split("/")

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
        canvas.create_text(80,110,text=i[6], fill="white")
        canvas.place(x=x,y=y)
        canvas.bind("<Button-1>", lambda event: self.onClickCanvas(i[0],i[1],i[4],canvas))
        self.frameK.update_idletasks()
        self.displayItems.append(canvas)

    def addNewElement(self, newElements):
        for i in newElements:
            self.frameK.after(100,self.create_canvas,i)
            



            

            



    def checkNewItem(self):
        
        self.cursor.execute(f'''SELECT * FROM menu_orden mo
inner join menu m on (mo.id_elemento = m.id_elemento)
WHERE estatus = 'solicitada' and tipo_elemento = '{self.tipo}' 
order by hora''')
        new_rows = self.cursor.fetchall()

        new_objetos = set(new_rows)


        if new_objetos.difference(self.objetos):
            print("Nuevo objeto detectado!")
            print("Objetos nuevos:", new_objetos.difference(self.objetos))
            self.addNewElement(list(new_objetos.difference(self.objetos)))


        if self.objetos.difference(new_objetos):
            print("Objeto eliminado!")
            print("Objetos eliminados:", self.objetos.difference(new_objetos))

        self.objetos = new_objetos


        self.frameK.after(5000,self.checkNewItem)


    def firstTimeIN(self):

        self.cursor.execute(f'''SELECT * FROM menu_orden mo
inner join menu m on (mo.id_elemento = m.id_elemento)
WHERE estatus = 'solicitada' and tipo_elemento = '{self.tipo}' 
order by hora''')
        new_rows = self.cursor.fetchall()
        self.objetos = set(new_rows)
        self.itemsCocina = list(new_rows)

        x = 10
        y = 5
        for i in self.itemsCocina:
            self.showObject(i[0],i[1],i[4], x, y)
            x=x+170
            if(x > 850):
                x= 10
                y = y+150


        self.frameK.after(5000,self.checkNewItem)


    def Cocina(self, _self, _style):
        
        self.frameK = ttk.Frame(_self, style=_style)

        try:
            self.firstTimeIN()
        except FileNotFoundError:
            print(f"El archivo  no se encontró.")
        except requests.exceptions.MissingSchema as e:
            print(f"Error al cargar el archivo: {e}")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
        
        return self.frameK



