from tkinter import *
from tkinter import messagebox, ttk, PhotoImage, font
from datetime import datetime
import os
from tkcalendar import Calendar

class Reporte():
    def __init__(self,_conn,_cursor, _query,_text,_result, _flag = True):
        self.cursor = _cursor
        self.conn = _conn
        self.query = _query
        self.oldQuery = _query
        self.fecha1 = ""
        self.fecha2 = ""
        self.text = _text
        self.extraText = _result
        self.flag = _flag


    def calendar(self, entry, fecha):
        def changeDate():
            entry.config(state="normal")
            fecha.set(cal.selection_get())
            entry.config(state="disabled")
            top.destroy()

        
        top = Toplevel(self.frame)
        cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1", year=2024, month=4, day=11)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="OK", command=changeDate).pack()

    def generateResult(self):
        if((self.fecha1.get() == "" or self.fecha2.get() =="") and self.flag == True):
            messagebox.showerror("Error","Ingrese las dos fechas primero")
        else:
            if(self.flag):
                tempQuery = self.query.split("'fecha_inicio' AND 'fecha_fin'")
                print(tempQuery)

                self.query = tempQuery[0]+f"'{self.fecha1.get()}' AND '{self.fecha2.get()}' "+tempQuery[1]
                print(self.query)
                self.cursor.execute(self.query)
                result = self.cursor.fetchall()
                print(result)

                if(result == []):
                    self.result.delete("1.0", END)
                    self.result.insert(END, "No hay informacion sobre ese rango de fechas")
                else:
                    self.textResult = f"{self.extraText}\n"
                    for i in result:
                        self.textResult += f"{i[0]}: {i[1]}\n"
                        
                    self.result.delete("1.0", END)
                    self.result.insert(END, self.textResult)

                self.query = self.oldQuery
            else:
                self.cursor.execute(self.query)
                result = self.cursor.fetchall()

                if(result == []):
                    self.result.delete("1.0", END)
                    self.result.insert(END, "No hay informacion sobre ese rango de fechas")
                else:
                    self.textResult = f"{self.extraText}\n"
                    for i in result:
                        self.textResult += f"{i[0]}: {i[1]}, {i[2]}, {i[3]}\n"

                    self.result.delete("1.0", END)
                    self.result.insert(END, self.textResult)



    def reporte(self,_self,_style):
        self.frame = ttk.Frame(_self,style=_style)
        self.fecha1 = StringVar()
        self.fecha2 = StringVar()

        Label(self.frame,text=self.text,font="Arial 20").place(x=5,y=5)
        x=250
        y=70

        if(self.flag):
            self.c1 = Entry(self.frame, textvariable=self.fecha1, state=DISABLED);self.c1.place(x=75,y=110)
            self.c2 = Entry(self.frame, textvariable=self.fecha2, state=DISABLED);self.c2.place(x=275,y=110)

            Button(self.frame,text="Fecha 1", font="Arial 12", command=lambda:self.calendar(self.c1,self.fecha1)).place(x=100,y=70)
            Button(self.frame,text="Fecha 2", font="Arial 12", command=lambda:self.calendar(self.c2,self.fecha2)).place(x=300,y=70)
            x=500
            y=70

        Button(self.frame,text="Generar Reporte", font="Arial 12",background="red", command=self.generateResult).place(x=x,y=y)


        self.result = Text(self.frame, height=9,width=85)
        self.result.place(x=5,y=140)



       

        

        return self.frame

        