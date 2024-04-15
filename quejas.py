import psycopg2
from tkinter import *
from tkinter import messagebox
from conexion import conexiones
import traceback

conexion = conexiones()
cursor= conexion.cursor()


def InsertarQueja(id_personal, motivo, fecha, hora,clasificacion, id_elemento):
    try: 
        cursor.execute("SELECT COUNT(*) FROM QUEJAS")
        resultado = cursor.fetchone()
        id_queja = resultado[0]
        id_queja += 1
        id_queja = str(id_queja)

        cursor.execute("SELECT id_personal from PERSONAL WHERE id_personal=%s", (id_personal,))
        resultado = cursor.fetchall()
        if resultado!=None:
            try:
                cursor.execute("insert into quejas (id_personal, motivo, id_queja,fecha, hora, clasificacion, id_elemento) values (%s,%s,%s,%s,%s,%s,%s)", (id_personal, motivo,id_queja, fecha, hora, clasificacion, id_elemento))
                conexion.commit()
                messagebox.showinfo("Atencion!", f"Queja registrada y el codigo de la queja es: {id_queja}")
                return True
            except Exception as e:
                print("Ocurrió un error:", e)
                print(traceback.format_exc())
                return False
        else:
            messagebox.showerror("Error", "el personal ingresado no existe")
    except Exception as msg:
        messagebox.showerror("Error","ingrese bien los datos")


    