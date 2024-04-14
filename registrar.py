import psycopg2
from tkinter import *
from tkinter import messagebox
from conexion import conexiones

#lo que hay que editar del esquema
"""
ALTER TABLE IF EXISTS public.personal
    ADD COLUMN password varchar(250);

ALTER TABLE IF EXISTS public.personal
    ADD COLUMN clasificacion varchar(250);
"""
#parte que va en main.py, pero para que no se tilinee, lo pondré aqui
"""
        self.e3= Entry(width=35); self.e3.place(x=355,y=370)
        self.btn1= Button(self, text="registrarse", font=("Arial", 15),fg="white" ,width=19, bg="#9d4edd", command=lambda:self.registro()).place(x=355,y=410) 
       
    def registro(self):
        self.nombre =self.e1.get()
        self.contraseña = self.e2.get()
        self.clasificacion = self.e3.get()
        registrar(self.nombre, self.contraseña, self.clasificacion)

"""

conexion = conexiones()
cursor= conexion.cursor()
id_personal = 10000 
encuesta = "null"
id_queja = "null"

def registrar( nombre, contraseña, clasificacion):
    
    try:
        if nombre == "" or contraseña == "" or clasificacion == "":
            messagebox.showerror("error","rellene todos los campos")
        else:
            clasificacion = clasificacion.lower()
            if clasificacion != "admin" and clasificacion != "mesero" and clasificacion != "cocinero" and clasificacion != "gerente"  and clasificacion != "recepcionista"  and clasificacion != "administrador"  and clasificacion != "personal":
                messagebox.showerror("error","la clasificacion es incorrecta")
            else:
                id_personal += 1 
                cursor.execute("insert into personal (id_personal, nombre_personal, contraseña, clasificacion) values (%s, %s, %s, %s)", (id_personal,nombre, contraseña, clasificacion))
                conexion.commit()
                messagebox.showinfo("Atencion!","personal registrado")

    except Exception as msg:
        messagebox.showerror("error",msg)
    
    
