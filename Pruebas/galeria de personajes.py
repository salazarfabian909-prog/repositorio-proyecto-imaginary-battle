import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("galeria de perosnajes")
ventana.geometry("720x1080")


def contadorseleccion(variable_actual): #este codigo fue sugerido por gemini
    seleccionados = [v.get() for v in vars_check].count(1) #seleccionados obtiene el resultado de lo que se marcó en la lista de
    limite = 3 #vars_check, luego de eso, count(1) cuenta la cantidad de cosas marcadas en el vars_check
    if seleccionados > limite: #si el valor de seleccionados es mayor a cero, saltará un mensaje que dice que solo
        variable_actual.set(0) # se puede seleccionar hasta el limite (3), y que el jugador ha llegado a ese limite
        messagebox.showwarning("Límite de selección", f"Solo puedes seleccionar hasta {limite} personajes.")

vars_check = [] #aqui se guarda la información los estados de seleccion de cada personaje
for i in range(15):
    var = tk.IntVar()
    vars_check.append(var) #mete el "sensor" var, crado anteriormente a vars_check, para observar en tiempo 
    lbl = tk.Label(ventana, text=f"personaje {i+1}") #real lo marcado
    lbl.grid(row=0 if i < 7 else 2, column=i if i < 7 else i-7, padx=10, pady=10) # en la parte de arriba se crea un label, que crea la etiqueda de los 7 personajes en total
    btn = tk.Checkbutton(ventana, text=f"Seleccionar {i+1}", variable=var, command=lambda v=var: contadorseleccion(v)) #lambda hace que
    btn.grid(row=1 if i < 7 else 3, column=i if i< 7 else i-7, padx=10, pady=10) #la función no se ejecute inmediatamente al detectar "()" en el comando
# las filas llegan hasta 7 pernajes para que no se salga de la pantalla, al llegar, bajan de fila y se reorganizan
# hasta aqui se agrego el codigo sugerido por gemini
ventana.mainloop()