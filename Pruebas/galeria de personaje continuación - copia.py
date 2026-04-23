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
mis_personajes = []
mis_botones = [] #crea dos listas
for i in range(15):
    var = tk.IntVar()
    vars_check.append(var) #mete el "sensor" var, crado anteriormente a vars_check, para observar en tiempo 
    lbl = tk.Label(ventana, text=f"personaje {i+1}") #real lo marcado
    lbl.grid(row=0 if i < 7 else 2, column=i if i < 7 else i-7, padx=10, pady=10) # en la parte de arriba se crea un label, que crea la etiqueda de los 7 personajes en total
    btn = tk.Checkbutton(ventana, text=f"Seleccionar {i+1}", variable=var, command=lambda v=var: contadorseleccion(v)) #lambda hace que
    btn.grid(row=1 if i < 7 else 3, column=i if i< 7 else i-7, padx=10, pady=10) #la función no se ejecute inmediatamente al detectar "()" en el comando
    mis_personajes.append(lbl)
    mis_botones.append(btn)   #nombra a btn y lbl como parte de las respectivas listas en esta linea y la anterior
# las filas llegan hasta 7 pernajes para que no se salga de la pantalla, al llegar, bajan de fila y se reorganizan
# hasta aqui se agrego el codigo sugerido por gemini

botoncontinue = tk.Button(ventana, text="Confirmar")
botoncontinue.grid(row=5, column=5)

def guardarpersonajes(*args):
    mispersonajes = []
    for i in range(len(vars_check)):
        if vars_check[i].get() == 1:
            mispersonajes.append(f"Personajes {i+1}")

    for l in mis_personajes:
        l.grid_forget()
    for b in mis_botones:
        b.grid_forget()
    
    lbl.grid_forget()
    btn.grid_forget()
    botoncontinue.grid_forget()

    textomio = tk.Label(ventana, text=f"Has elegido a {mispersonajes}")
    textomio.grid(row=6, column=6)

botoncontinue.config(command=guardarpersonajes)
ventana.mainloop()