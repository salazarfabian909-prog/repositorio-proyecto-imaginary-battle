import tkinter as tk
from tkinter import messagebox

window1 = tk.Tk()
window1.geometry("720x720")
window1.configure(padx=0, pady=0,highlightthickness=0)

firsttext = tk.Label(window1, text="Bienvenido")
firsttext.configure(font="Arial, 20")
firsttext.pack()

firstbutton = tk.Button(window1, text="------>")
firstbutton.configure(font="Arial, 20")
firstbutton.pack()

first_si_button = tk.Button(window1, text="------>")
first_si_button.configure(font="Arial, 20")

def nombre():
    firstbutton.pack_forget()
    first_si_button.pack()
    firsttext.configure(text="Debes de escribir tu nombre de jugador a continuación")

firstbutton.config(command= nombre)

def si_response(*args):
    first_si_button.pack_forget()
    firsttext.configure(text="Escribe tu nombre de jugador para empezar")
    boxname.pack()
    savenamebutton.pack()

first_si_button.config(command= si_response)

variable1 = tk.StringVar()
def savename(*args):
    if boxname.get().strip():
        savenamebutton.config(state="normal")
    else:
        savenamebutton.config(state="disabled")

boxname = tk.Entry(window1, textvariable=variable1)
boxname.configure(font="Arial, 20")
savenamebutton = tk.Button(text="Guardar mi nombre", state="disabled")
savenamebutton.configure(font="Arial, 20")
variable1.trace_add("write",savename)

galeriaframe = tk.Frame(window1)

galeriabutton1 = tk.Button(galeriaframe, text="Ir a galeria de personajes")
def galeria1(*args):
    boxname.pack_forget()
    savenamebutton.pack_forget()
    firsttext.pack_forget()
    global playername 
    playername = boxname.get()
    texto1 = tk.Label(text=f"Tu nombre es {playername}")
    texto1.configure(font="Arial, 20")
    texto1.pack()
    galeriabutton1. configure(font= "Arial, 20")
    galeriabutton1.pack(padx=10, pady=10)
    window1.after(3000, texto1.pack_forget)
    window1.after(4000, lambda: galeriaframe.pack())

savenamebutton.config(command=galeria1)

ventanapersonajes = tk.LabelFrame(relief="flat")

def ir_a_galeria(*args):
    ventanapersonajes.pack()
    galeriabutton1.pack_forget()

galeriabutton1.config(command= ir_a_galeria)

nombres_de_personajes = ["Patrolclo", "Benzemá", "Juan", "Seis", "Veroliz", "Esteban", "Jeff", "Elena",
                          "Leylani", "Princesa", "Tomas","Pancracio", "Yomelaximohamillyilmar Cariliana",
                            "Don Krilinger", "Mateo" ]


def contadorseleccion(variable_actual, *args):
    seleccionados = [v.get() for v in vars_check].count(1)
    limite = 3
    if seleccionados > limite:
        variable_actual.set(0)
        messagebox.showwarning("Límite de selección", f"Solo puedes seleccionar hasta {limite} personajes.")
    elif seleccionados == limite:
        botoncontinue.configure(state= "normal")

vars_check = [] 
mis_personajes = []
mis_botones = [] 
for i in range(15):
    var = tk.IntVar()
    vars_check.append(var)
    lbl = tk.Label(ventanapersonajes, text=nombres_de_personajes[i], font= "Arial, 18")
    lbl.grid(row=0 if i < 7 else 2, column=i if i < 7 else i-7, padx=10, pady=10)
    btn = tk.Checkbutton(ventanapersonajes, variable=var, command=lambda v=var: contadorseleccion(v), font="Arial, 14")
    btn.grid(row=1 if i < 7 else 3, column=i if i< 7 else i-7, padx=10, pady=10)
    mis_personajes.append(lbl)
    mis_botones.append(btn)

botoncontinue = tk.Button(ventanapersonajes, text="Confirmar", font= "Arial, 18")
botoncontinue.configure(state="disabled")
botoncontinue.grid(row=5, column=4)

iraljuegobutton = tk.Button(window1, text="continuar", font= "Arial, 20")

def guardarpersonajes(*args):
    global mispersonajes
    mispersonajes = []
    for i in range(len(vars_check)):
        if vars_check[i].get() == 1:
            mispersonajes.append(nombres_de_personajes[i])
    global personajes_texto
    personajes_texto = ", ".join(mispersonajes)
    for l in mis_personajes:
        l.grid_forget()
    for b in mis_botones:
        b.grid_forget()
    lbl.grid_forget()
    btn.grid_forget()
    botoncontinue.grid_forget()
    textomio = tk.Label(ventanapersonajes, text=f"Has elegido a {personajes_texto}")
    textomio.configure(font= "Arial, 20")
    textomio.grid(row=6, column=6)
    ventanapersonajes.after(4000, textomio.grid_forget)
    ventanapersonajes.after(4000, ventanapersonajes.pack_forget)
    ventanapersonajes.after(5000, iraljuegobutton.pack)

botoncontinue.config(command=guardarpersonajes)

cuadrogris = tk.LabelFrame(window1)
cuadrogris.configure(bd=0, relief="flat")

otrocuadrogris = tk.LabelFrame(cuadrogris, font="Arial, 20")
otrocuadromas = tk.LabelFrame(otrocuadrogris, font="Arial, 15")
my_nombre_en_cuadrogris = tk.Label(otrocuadromas, font="Arial, 15")

def statsbox():
    cuadrogris.pack(fill="both", expand=True)
    iraljuegobutton.pack_forget()
    otrocuadrogris.configure(width=350, height=175, bg="light grey")
    otrocuadrogris.grid()
    otrocuadromas.grid()
    my_nombre_en_cuadrogris.grid()
    my_nombre_en_cuadrogris.config(text=f"Jugador: {playername}        Personajes: {personajes_texto}")

iraljuegobutton.config(command=statsbox)
window1.mainloop()