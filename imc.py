import tkinter as tk

from tkinter import ttk
from tkinter.constants import LEFT, RIGHT

def show_entry_fields():
    imc = 0
    try: 
        weight = float(eWeight.get())
        height = float(eHeight.get())
        imc = weight / (height*height)
        print(imc) 
    except Exception as ex:
        print(ex) 
    print("Peso: %s\nAltura: %s" % (eWeight.get(), eHeight.get()))
    
    # https://brasilescola.uol.com.br/saude-na-escola/Indice-massa-corporea-imc.htm
    situation = ""
    if imc < 18.5:
        situation = "subpeso"
    elif imc < 25:
        situation = "normal"
    elif imc < 30: 
        situation = "pré-obeso"
    elif imc < 35: 
        situation = "obeso I"
    elif imc < 40: 
        situation = "obeso II"
    else: 
        situation = "obeso III"
    varSituation.set('Situação: '+situation)  
    varImc.set(imc)  

master = tk.Tk()

frm = ttk.Frame(master, padding=6)
frm.grid() 

varImc = tk.StringVar() 
varImc.set("0.0")  

varSituation  = tk.StringVar() 
varSituation.set('Situação: ???')

eResult = tk.Entry(frm, width=34,justify=tk.RIGHT, textvariable=varImc)  
eResult.grid(row=1, columnspan=2,pady=3)
 
labelSituation = tk.Label(frm, textvariable=varSituation)
labelSituation.grid(row=2, columnspan=2, pady=3)

tk.Label(frm, text="Peso:").grid(row=3, sticky=tk.W)
tk.Label(frm, text="Altura:").grid(row=4, sticky=tk.W)

eWeight = tk.Entry(frm, width=15)
eHeight = tk.Entry(frm, width=15) 

eWeight.grid(row=3, column=1,pady=3)
eHeight.grid(row=4, column=1,pady=3)

tk.Button(frm, width=25, text='Calcular', command=show_entry_fields).grid(row=5, columnspan=2, pady=4)
tk.Button(frm, width=25, text='Sair', command=master.quit).grid(row=6, columnspan=2, pady=4)                                

master.mainloop()