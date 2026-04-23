import tkinter as tk
from tkinter import messagebox

window1 = tk.Tk()
window1.geometry("1080x1080")
window1.configure(padx=0, pady=0,highlightthickness=0) #el hight... hace que el grosor no resalte si está en cero

firsttext = tk.Label(window1, text="Bienvenido")
firsttext.configure(font="Arial, 20")
firsttext.pack()

firstbutton = tk.Button(window1, text="------>")
firstbutton.configure(font="Arial, 20")
firstbutton.pack()

aboutbutton = tk.Button(text="Acerca de", font="Arial,20")
aboutbutton.pack()

global labelinfo
labelinfo = tk.LabelFrame(window1)

global labelinfoclosebutton
labelinfoclosebutton = tk.Button(labelinfo, text= "Cerrar", font="Arial, 20")

def informacion(*args):
    firstbutton.pack_forget()
    firsttext.pack_forget()
    aboutbutton.pack_forget()

    labelinfo.pack()
    labelinfolabel = tk.Label(labelinfo, font= "Arial,20", text="Este juego es trabajo del proyecto imaginary battles, en este juego te adentraras en un " \
    "mundo dondee existen criaturas llamadas hollos, a quienes debes derrotar para terminar la historia")
    labelinfolabel.grid()

    labelinfoclosebutton.grid()
aboutbutton.configure(command= informacion)

def closeinformacion():
    labelinfo.pack_forget()
    firsttext.pack()
    firstbutton.pack()
    aboutbutton.pack()
labelinfoclosebutton.config(command=closeinformacion)


    


first_si_button = tk.Button(window1, text="------>")
first_si_button.configure(font="Arial, 20")

def nombre():
    aboutbutton.pack_forget()
    firstbutton.pack_forget()
    first_si_button.pack()
    firsttext.configure(text="Debes de escribir tu nombre de jugador a continuación")

firstbutton.config(command= nombre)
#las lineas anteriores te levan a el cuadro de texto, es una bienvenida
#la siguiente función muestra el cuadro para que el jugador ingrese su nombre

def si_response(*args):
    first_si_button.pack_forget()
    firsttext.configure(text="Escribe tu nombre de jugador para empezar")
    boxname.pack()
    savenamebutton.pack()

first_si_button.config(command= si_response)


#la siguiente funcion, variable1, hace que el boton de guardar numbre no se habilite hasta
#que el usuario haya ingresado algo, sino, el boton no se habilitará
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

#la siguiente funcion guarda el nombre del jugador, seguido de eso, muestra un mensaje de confirmacion
#al estilo de "tu nombre es ...", para despues desaparecer y mostrar un boton que te llevará a la
#galeria de personajes
galeriaframe = tk.Frame(window1)

galeriabutton1 = tk.Button(galeriaframe, text="Ir a galeria de personajes")
def galeria1(*args):
    boxname.pack_forget()
    savenamebutton.pack_forget()
    firsttext.pack_forget()
    #lo de arriba esconde el cuadro de texto y su respectivo botón
    global playername 
    playername = boxname.get()
    #guarda el nombre del jugador
    texto1 = tk.Label(text=f"Tu nombre es {playername}")
    texto1.configure(font="Arial, 20")
    texto1.pack()
    #muestra un cuadro que dice el nombre del jugador

    galeriabutton1. configure(font= "Arial, 20")
    galeriabutton1.pack(padx=10, pady=10)
    window1.after(3000, texto1.pack_forget)
    window1.after(4000, lambda: galeriaframe.pack())
    #muestra el texto del nombre por tres segundos y al cuarto muestra el boton de la galería

savenamebutton.config(command=galeria1)



ventanapersonajes = tk.LabelFrame(relief="flat")

def ir_a_galeria(*args):
    ventanapersonajes.pack()
    galeriabutton1.pack_forget()

galeriabutton1.config(command= ir_a_galeria)

nombres_de_personajes = ["Patrolclo", "Benzemá", "Juan", "Seis", "Veroliz", "Esteban", "Jeff", "Elena", "Leylani", "Princesa", "Tomas",
                          "Pancracio", "Yomelaximohamillyilmar Cariliana", "Don Krilinger", "Mateo" ]


def contadorseleccion(variable_actual, *args): #este codigo fue sugerido por gemini
    seleccionados = [v.get() for v in vars_check].count(1) #seleccionados obtiene el resultado de lo que se marcó en la lista de
    limite = 3 #vars_check, luego de eso, count(1) cuenta la cantidad de cosas marcadas en el vars_check
    if seleccionados > limite: #si el valor de seleccionados es mayor a cero, saltará un mensaje que dice que solo
        variable_actual.set(0) # se puede seleccionar hasta el limite (3), y que el jugador ha llegado a ese limite
        messagebox.showwarning("Límite de selección", f"Solo puedes seleccionar hasta {limite} personajes.")
    elif seleccionados == limite:
        botoncontinue.configure(state= "normal")

vars_check = [] #aqui se guarda la información los estados de seleccion de cada personaje
mis_personajes = []
mis_botones = [] #crea dos listas
for i in range(15):
    var = tk.IntVar()
    vars_check.append(var) #mete el "sensor" var, crado anteriormente a vars_check, para observar en tiempo 
    lbl = tk.Label(ventanapersonajes, text=nombres_de_personajes[i], font= "Arial, 18") #real lo marcado
    lbl.grid(row=0 if i < 7 else 2, column=i if i < 7 else i-7, padx=10, pady=10) # en la parte de arriba se crea un label, que crea la etiqueda de los 7 personajes en total
    btn = tk.Checkbutton(ventanapersonajes, variable=var, command=lambda v=var: contadorseleccion(v), font="Arial, 14")  #lambda hace que
    btn.grid(row=1 if i < 7 else 3, column=i if i< 7 else i-7, padx=10, pady=10) #la función no se ejecute inmediatamente al detectar "()" en el comando
    mis_personajes.append(lbl)
    mis_botones.append(btn)   #nombra a btn y lbl como parte de las respectivas listas en esta linea y la anterior
# las filas llegan hasta 7 pernajes para que no se salga de la pantalla, al llegar, bajan de fila y se reorganizan
# hasta aqui se agrego el codigo sugerido por gemini

botoncontinue = tk.Button(ventanapersonajes, text="Confirmar", font= "Arial, 18")
botoncontinue.configure(state="disabled")
botoncontinue.grid(row=5, column=4)

iraljuegobutton = tk.Button(window1, text="continuar", font= "Arial, 20")

def guardarpersonajes(*args):
    global mispersonajes
    mispersonajes = []
    for i in range(len(vars_check)):
        if vars_check[i].get() == 1: #si el espacio del checkbutton = 1, se guarda, osea, si está marcado
            mispersonajes.append(nombres_de_personajes[i])
    # Esta linea lee lo marcado para guardarlo para despues, y ser usado como
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
cuadrogris.configure(bd=0, relief="flat") #relief controla el efecto de sombra, flat hace que no tenga efectos de sombra
cuadrogris.propagate(False)
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