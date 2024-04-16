import psycopg2
from tkinter import *
from tkinter import messagebox
from conexion import conexiones
import traceback
from datetime import datetime

conexion = conexiones()
cursor= conexion.cursor()


def capacidadPersonas(mesa):
    try:
        resultado = cursor.execute("SELECT capacidad FROM mesas WHERE id_mesa = %s",(mesa,))
        resultado = cursor.fetchone()
        return resultado[0]
    except Exception as e:
        print("Ocurrió un error:", e)
        print(traceback.format_exc())
        return False
    
def insertarMesaJunta(mesaJunta, mesa):
    try:
        cursor.execute("UPDATE mesas SET mesas_juntas = %s WHERE id_mesa = %s", (mesaJunta, mesa,))
        conexion.commit()
        return True
    except Exception as e:
        print("Ocurrió un error:", e)
        print(traceback.format_exc())
        return False

# print(capacidadPersonas(12))
def queryInsertar(id_mesero, mesa, cant_personas):
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
        return True
    except Exception as e:
        print("Ocurrió un error:", e)
        print(traceback.format_exc())
        return False
    
def cambiarEstadoMesa(mesa, estado):
    try:
        cursor.execute("UPDATE mesas SET habilitada = %s WHERE id_mesa = %s", (estado, mesa,))
        conexion.commit()
        return True
    except Exception as e:
        print("Ocurrió un error:", e)
        print(traceback.format_exc())
        return False

def crearPedido(id_mesero, mesa, cant_personas,mesasJuntas=False,mesaJunta = None):
    try:
        if mesa == "" or id_mesero == "" or id_mesero == "":
            messagebox.showerror("error","rellene todos los campos")
            return False
        else:
            if mesasJuntas:
                if cant_personas>capacidadPersonas(mesa)+capacidadPersonas(mesaJunta):
                    messagebox.showerror("error","La cantidad de personas excede la capacidad de las mesas")
                    return False
                else:
                    queryInsertar(id_mesero, mesa, cant_personas)
                    cambiarEstadoMesa(mesaJunta, '0')
                    insertarMesaJunta(mesaJunta, mesa)
                    return True
            else:
                if cant_personas>capacidadPersonas(mesa):
                    messagebox.showerror("error","La cantidad de personas excede la capacidad de la mesa")
                    return False
                else:
                    queryInsertar(id_mesero, mesa, cant_personas)
                    return True
    except Exception as msg:
        messagebox.showerror("Error", "No se pudo ingresar, ingrese bien los datos"+str(msg))
        return False
# crearPedido(1005, 2, 4,True,3)
    
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
        print(resultado, orden)
        return resultado[0]
    except Exception as msg:
        messagebox.showerror("Error", "No se pudo realizar consulta")
        return False
    
def encontrarMesa(matriz, numero):
    for fila_index, fila in enumerate(matriz):
        for columna_index, valor in enumerate(fila):
            if valor == numero:
                return fila_index , columna_index 
            
def encontrarMesa2(matriz, numero):
    for fila_index, fila in enumerate(matriz):
        for columna_index, valor in enumerate(fila):
            if valor == numero:
                return  columna_index 

def cerrarCuenta(orden):
    try:
        resultado = cursor.execute("select o.id_orden, o.id_mesa, o.id_mesero, o.cant_personas, m.mesas_juntas from orden as o join mesas as m on(o.id_mesa = m.id_mesa) where estado_orden = 'abierto' and id_orden = %s",(orden,))
        resultado = cursor.fetchone()
        print(resultado)
        if(resultado[4] != None):
            cursor.execute("UPDATE mesas SET habilitada = '1' WHERE id_mesa = %s", (resultado[4],))
            conexion.commit()
            cursor.execute("UPDATE mesas SET mesas_juntas = NULL WHERE id_mesa = %s", (resultado[1],))
            conexion.commit()
        cursor.execute("UPDATE mesas SET habilitada = '1' WHERE id_mesa = %s", (resultado[1],))
        conexion.commit()
        cursor.execute("UPDATE orden SET estado_orden = 'cerrado' WHERE id_orden = %s", (orden,))
        conexion.commit()
        salida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute("UPDATE orden SET orden_salida = %s WHERE id_orden = %s", (salida,orden,))
        conexion.commit()
        return True
    except Exception as msg:
        messagebox.showerror("Error", "No se pudo realizar consulta")
        return False

def añadirPedido(id_elemento, id_orden):
    try:
        if id_elemento == "" or id_orden == "":
            messagebox.showerror("error","Rellene todos los campos")
        else:
            llegada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("insert into menu_orden (id_elemento, id_orden, cantidad,estatus,hora) values (%s,%s,1,'solicitada',%s)", (id_elemento, id_orden, llegada))
            conexion.commit()
            return True
    except Exception as msg:
        messagebox.showerror("Error", "No se pudo ingresar, ingrese bien los datos")
        print(traceback.format_exc())
        return False
    
def listadoOrden(id_orden):
        
    try:
        solicitadas = cursor.execute("select  m.nombre_elemento,count(*) from menu as m join menu_orden as mo on (m.id_elemento = mo.id_elemento) where mo.estatus = 'solicitada' and mo.id_orden = %s group by m.nombre_elemento",(id_orden,))
        solicitadas = cursor.fetchall()
        entregadas = cursor.execute("select  m.nombre_elemento,count(*) from menu as m join menu_orden as mo on (m.id_elemento = mo.id_elemento) where mo.estatus = 'entregada' and mo.id_orden = %s group by m.nombre_elemento",(id_orden,))
        entregadas = cursor.fetchall()
        print(solicitadas)
        print(entregadas)
        resultado = ""
        resultado = f"\n--- Solicitadas ----\n"
        if solicitadas == None:
            resultado += "No hay ordenes solicitadas\n"
        else:
            for i in solicitadas:
                resultado += f"{i[0]}: {i[1]}\n"
            resultado += "\n--- Entregadas ----\n"
        if entregadas == None:
            resultado += "No hay ordenes entregadas\n"
        else:
            for i in entregadas:
                resultado += f"{i[0]}: {i[1]}\n"
        return resultado
    except Exception as msg:
        messagebox.showerror("Error", "No se pudo realizar consulta")
        return False
    
def mesasMover():
    try:
        sql = "select id_mesa from mesas where movibilidad = '1'"
        resultado = cursor.execute(sql,)
        resultado = cursor.fetchall()
        resultado = [fila[0] for fila in resultado]
        return resultado
    except Exception as msg:
        messagebox.showerror("Error", "No se pudo realizar consulta")
        return False

def mesasDispo(area,m1):
    try:
        resultado = cursor.execute("select ma.id_mesa from mesas_areas as ma join mesas as m on (ma.id_mesa = m.id_mesa) where ma.id_area = %s and m.movibilidad ='1' and m.habilitada = '1' and m.id_mesa != %s",(area,m1,))
        resultado = cursor.fetchall()
        resultado = [fila[0] for fila in resultado]
        return resultado
    except Exception as msg:
        messagebox.showerror("Error", "No se pudo realizar consulta")
        return False
    

def insertarFactura(id_orden,nit,nombre,direccion):
    try:
       
        cursor.execute("UPDATE orden set total_orden = (SELECT SUM(m.precio) AS total FROM menu AS m JOIN menu_orden AS mo ON m.id_elemento = mo.id_elemento JOIN orden AS o ON o.id_orden = mo.id_orden WHERE o.id_orden = %s), propina = (SELECT  SUM(m.precio) * 0.10 AS propina FROM menu AS m JOIN menu_orden AS mo ON m.id_elemento = mo.id_elemento JOIN orden AS o ON o.id_orden = mo.id_orden WHERE o.id_orden = %s), nit = %s, nombre_nit = %s, direccion = %s where id_orden = %s",((id_orden),id_orden,nit,nombre,direccion,id_orden,))
        conexion.commit()
        print("Factura creada", id_orden)
        return True
    except Exception as msg:
        messagebox.showerror("Error", "No se pudo realizar consulta")
        return False


def insertarEncuesta(id_personal, amabilidad, exactitud):
    try:
        print("encuesta     ",id_personal, amabilidad, exactitud    )
        resultado = cursor.execute("select count(*) from encuesta")
        resultado = cursor.fetchone()
        print(resultado)
        id_encuesta = resultado[0] + 1
        hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("insert into encuesta (id_personal, amabilidad, exactitud, encuesta_id, fecha) values (%s,%s,%s,%s, %s)",(id_personal, amabilidad, exactitud, id_encuesta, hora))
        conexion.commit()
        print("Encuesta creada")
        return True
    except Exception as msg:
        messagebox.showerror("Error", "No se pudo realizar consulta")
        print(msg)
        return False

def obtenerMesasJuntas():
    try:
        resultado = cursor.execute("select mesas_juntas from mesas where mesas_juntas is not null")
        resultado = cursor.fetchall()
        resultado = [fila[0] for fila in resultado]
        return resultado
    except Exception as msg:
        messagebox.showerror("Error", "No se pudo realizar consulta")
        return False
    
print(obtenerMesasJuntas())