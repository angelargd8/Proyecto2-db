import psycopg2
from tkinter import *
from tkinter import messagebox
from conexion import conexiones
import traceback
from datetime import datetime

conexion = conexiones()
cursor= conexion.cursor()



        
def crearPedido(id_mesero, mesa, cant_personas):
    try:
        if mesa == "" or id_mesero == "" or id_mesero == "":
            messagebox.showerror("error","rellene todos los campos")
        else:
            resultado = cursor.execute("SELECT COUNT(*) FROM orden")
            resultado = cursor.fetchone()
            id_pedido = resultado[0] + 1
            print(id_pedido)
            llegada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                cursor.execute("insert into orden (id_orden, id_mesero, estado_orden, id_mesa, orden_llegada, cant_personas) values (%s,%s,%s,%s,%s,%s)", (id_pedido, id_mesero, "abierto", mesa, llegada, cant_personas))
                conexion.commit()
                cursor.execute("UPDATE mesas SET habilitada = '0' WHERE id_mesa = %s", (mesa,))
                conexion.commit()
                messagebox.showinfo("Atencion!", f"Orden creada y su codigo(id) es: {id_pedido}")
                return id_pedido
            except Exception as e:
                print("Ocurrió un error:", e)
                print(traceback.format_exc())
    except Exception as msg:
        messagebox.showerror("Error", "No se pudo ingresar, ingrese bien los datos")
        return False
    
def obtenerOrden():
    try:
        resultado = cursor.execute("SELECT COUNT(*) FROM orden")
        resultado = cursor.fetchone()
        id_pedido = resultado[0] 
        return id_pedido
    except Exception as e:
        print("Ocurrió un error:", e)
        print(traceback.format_exc())

def ordenesActuales():
    sql = "select id_orden, id_mesa, id_mesero, cant_personas from orden where estado_orden = 'abierto'"
    try:
            resultado = cursor.execute(sql)
            resultado = cursor.fetchall()
            print(resultado)
            return resultado
    except Exception as msg:
        messagebox.showerror("Error", "No se pudo realizar consulta")
        return False
    
def ordenEspecifica(orden):
    try:
            resultado = cursor.execute("select id_orden, id_mesa, id_mesero, cant_personas from orden where estado_orden = 'abierto' and id_orden = %s",(orden,))
            resultado = cursor.fetchall()
            print(resultado)
            return resultado[0]
    except Exception as msg:
        messagebox.showerror("Error", "No se pudo realizar consulta")
        return False
    
def encontrarMesa(matriz, numero):
    for fila_index, fila in enumerate(matriz):
        for columna_index, valor in enumerate(fila):
            if valor == numero:
                return fila_index , columna_index 

def cerrarCuenta():
    pass

def añadirPedido():
    pass
