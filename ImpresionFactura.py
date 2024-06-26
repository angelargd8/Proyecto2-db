import psycopg2
from tkinter import *
from tkinter import messagebox
from conexion import conexiones
import traceback
#parte que va en main.py, pero para que no se tilinee, lo pondré aqui
"""
self.crear_tab4()
self.tab4=ttk.Frame(self.notebook,style='TFrame.TFrame')
        self.notebook.add(self.tab4, text="Impresion factura")

    def crear_tab4(self):
        self.l1= Label(self.tab4, text="Impresion de factura", font=self.custom_font, bg="#3c096c", fg="white").place(x=20, y=20)
        Button(self.tab4, text="Imprimir factura", font=("Arial", 9),fg="white" ,width=19, bg="#9d4edd", command=lambda:self.imprimir_factura()).place(x=430,y=30) 
        self.base_font = font.Font(family="Helvetica", size=30, weight="normal", slant="roman")
        self.custom_font3 = self.base_font.copy()
        self.custom_font3.configure(size=10, weight="bold") #underline=1
        self.l5= Label(self.tab4, text="ingrese el id de la orden:", font=self.custom_font3, bg="#3c096c", fg="white").place(x=20, y=100)
        self.e5= Entry(self.tab4,width=35); self.e5.place(x=20,y=130)
        
        
"""

conexion = conexiones()
cursor= conexion.cursor()

def impresionFactura(id_orden):
    conexion = conexiones()
    cursor= conexion.cursor()
    print(id_orden)
    cursor.execute("SELECT * FROM orden WHERE id_orden=%s",(id_orden,))
    orden=cursor.fetchone()
    print(orden)

    """
    id_orden       INTEGER NOT NULL,
    id_mesa        INTEGER NOT NULL,
    total_orden    NUMERIC,
    estado_orden   VARCHAR(10) NOT NULL,
    propina        NUMERIC,
    id_mesero      INTEGER NOT NULL,
    nit            VARCHAR(50),
    nombre_nit     VARCHAR(50),
    direccion      VARCHAR(20),
    orden_llegada  TIMESTAMP NOT NULL, 
    orden_salida   TIMESTAMP,
    cant_personas  INTEGER NOT NULL
    """
    
    if orden is not None:
        estado=orden[3]
        #print(orden)
        print(estado)
        if estado == 'cerrado' or estado == 'cerrada':
            print("Estado de la orden: ", estado)
            #datos del cliente
            nit = orden[6]
            nombre_nit = orden[7]
            direccion = orden[8]        
            print(nit, nombre_nit, direccion)
            #formas de pago
            try:
                cursor.execute('''SELECT orden.id_orden, pago.tipo_pago FROM orden 
                                    INNER JOIN orden_pago ON orden.id_orden = orden_pago.id_orden 
                                    INNER JOIN pago ON orden_pago.id_pago = pago.id_pago WHERE orden.id_orden = %s
                                    ''', (id_orden,))
                pago= cursor.fetchone()
                tipo_pago = pago[1]
                print(tipo_pago)
            except Exception as e:
                print("Ocurrió un error, falta poner el metodo de pago:", e)
                print(traceback.format_exc())
                                
                        
            #total de la orden y que pidio
            cursor.execute('''SELECT o.id_orden, o.total_orden, m.nombre_elemento, m.precio
                            FROM orden o
                            JOIN menu_orden mo ON o.id_orden = mo.id_orden
                            JOIN menu m ON mo.id_elemento = m.id_elemento
                            WHERE o.id_orden = %s''', (id_orden,))
            resultados = cursor.fetchall()

            total_orden= resultados[0][1]
           
            print("total_orden")
            print(total_orden)
    
            return True, nit, nombre_nit, direccion, tipo_pago, total_orden, resultados

        else:
            messagebox.showerror("Error", "No se puede imprimir la orden porque sigue abierta")
    else:
            messagebox.showerror("Error", "No se puede imprimir la orden porque no existe la orden")

#para probar la funcion xd
#impresionFactura(4)