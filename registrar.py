import psycopg2
from tkinter import *
from tkinter import messagebox
from conexion import conexiones
import traceback

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

def registrar( nombre, contraseña, clasificacion):
    
    try:
        if nombre == "" or contraseña == "" or clasificacion == "":
            messagebox.showerror("error","rellene todos los campos")
        else:
            clasificacion = clasificacion.lower()
            if clasificacion == "admin" or clasificacion == "mesero" or clasificacion == "cocinero" or clasificacion == "gerente"  or clasificacion == "recepcionista"  or clasificacion == "administrador"  or clasificacion == "personal" or clasificacion == "mesera" or clasificacion == "cocinera":
                resultado = cursor.execute("SELECT COUNT(*) FROM PERSONAL")
                resultado = cursor.fetchone()
                id_personal = resultado[0]
                id_personal += 10000
                id_personal = str(id_personal)
                try:
                    cursor.execute("insert into personal (id_personal, nombre_personal, password, clasificacion) values (%s,%s,%s,%s)", (id_personal, nombre, contraseña, clasificacion))
                    conexion.commit()
                    messagebox.showinfo("Atencion!", f"personal registrado y su codigo(id) es: {id_personal}")
                    return True
                except Exception as e:
                    print("Ocurrió un error:", e)
                    print(traceback.format_exc())
            else:
                messagebox.showerror("error","la clasificacion es incorrecta")
                

    except Exception as msg:
        messagebox.showerror("Error", "No se pudo ingresar, ingrese bien los datos")
    
    
