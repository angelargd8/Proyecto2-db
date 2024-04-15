import psycopg2
from tkinter import *
from tkinter import messagebox
from conexion import conexiones
import traceback

conexion = conexiones()
cursor= conexion.cursor()

def registrar( nombre, contraseña, clasificacion, id_area):
    
    try:
        if nombre == "" or contraseña == "" or clasificacion == "":
            messagebox.showerror("error","rellene todos los campos")
        else:
            clasificacion = clasificacion.lower()
            #baristay sin genero
            if clasificacion == "admin" or clasificacion == "mesero" or clasificacion == "cocinero" or clasificacion == "gerente"  or clasificacion == "recepcionista"  or clasificacion == "administrador"  or clasificacion == "personal":
                resultado = cursor.execute("SELECT COUNT(*) FROM PERSONAL")
                resultado = cursor.fetchone()
                id_personal = resultado[0]
                id_personal += 1000
                id_personal = str(id_personal)
                

                try:
                    cursor.execute("insert into personal (id_personal, nombre_personal, password, clasificacion) values (%s,%s,%s,%s)", (id_personal, nombre, contraseña, clasificacion))
                    conexion.commit()
                    messagebox.showinfo("Atencion!", f"personal registrado y su codigo(id) es: {id_personal}")
                    if clasificacion == "mesero" and id_area != "":
                        try:
                            id_mesero = id_personal
                            id_personal1= id_personal
                            tipo = "Meseros"
                            cursor.execute("insert into meseros (id_personal, id_area, id_mesero, tipo) values (%s,%s,%s,%s)", (id_personal1, id_area, id_mesero, tipo))
                            conexion.commit()
                            messagebox.showinfo("Atencion!", f"mesero registrado y su codigo(id) es: {id_mesero}")
                        except Exception as e:
                            print("Ocurrió un error:", e)
                            print(traceback.format_exc())
                    else:
                        pass
                    return True
                




                except Exception as e:
                    print("Ocurrió un error:", e)
                    print(traceback.format_exc())
            else:
                messagebox.showerror("error","la clasificacion es incorrecta")
                

    except Exception as msg:
        messagebox.showerror("Error", "No se pudo ingresar, ingrese bien los datos")
    
    
