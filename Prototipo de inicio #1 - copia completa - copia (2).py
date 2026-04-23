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
    global labelinfolabel
    labelinfolabel = tk.Label(labelinfo, font= "Arial,20", text="Este juego es trabajo del proyecto imaginary battles, en este juego te adentraras en un " \
    "mundo dondee existen criaturas llamadas hollos, a quienes debes derrotar para terminar la historia")
    labelinfolabel.grid()
    labelinfoclosebutton.grid()
aboutbutton.configure(command= informacion)

def closeinformacion():
    labelinfolabel.grid_forget()
    labelinfo.pack_forget()
    labelinfoclosebutton.grid_forget()
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

infopersonajes= tk.Button(window1, text= "Información de personajes", font="Arial, 20")

def ir_a_galeria(*args):
    ventanapersonajes.pack()
    infopersonajes.place(relx=0.1, rely= 0.9)
    galeriabutton1.pack_forget()
galeriabutton1.config(command= ir_a_galeria)

nombres_de_personajes = ["Patrolclo", "Benzemá", "Juan", "Seis", "Veroliz", "Esteban", "Jeff", "Elena", "Leylani", "Princesa", "Tomas",
                          "Pancracio", "Yomelaximohamillyilmar Cariliana", "Don Krilinger", "Mateo" ]

stats_personajes = {
    "Patrolclo": {"vida": 100, "atq": 20, "defe": 15},
    "Benzemá": {"vida": 120, "atq": 15, "defe": 25},
    "Juan": {"vida": 90, "atq": 25, "defe": 10},
    "Seis": {"vida": 110, "atq": 18, "defe": 18},
    "Veroliz": {"vida": 85, "atq": 30, "defe": 5},
    "Esteban": {"vida": 150, "atq": 10, "defe": 30},
    "Jeff": {"vida": 100, "atq": 22, "defe": 12},
    "Elena": {"vida": 95, "atq": 28, "defe": 8},
    "Leylani": {"vida": 105, "atq": 20, "defe": 20},
    "Pancracio": {"vida": 130, "atq": 12, "defe": 22},
    "Yomelaximohamillyilmar Cariliana": {"vida": 200, "atq": 5, "defe": 40},
    "Don Krilinger": {"vida": 80, "atq": 35, "defe": 5},
    "Mateo": {"vida": 115, "atq": 17, "defe": 20}}
global ventana_info_personajes

ventana_info_personajes = tk.LabelFrame(window1)

close_info_personajes_button = tk.Button(ventana_info_personajes, text="Cerrar")

infolabelpersonajes = "" #codigo creado por gemini

for nombre, stats in stats_personajes.items():
    infolabelpersonajes += f"{nombre}: Vida: {stats['vida']}, Atq: {stats['atq']}, Defe: {stats['defe']}\n"

label_lista = tk.Label(ventana_info_personajes, text=infolabelpersonajes, justify="left", font=("Arial", 10))
 #aqui termina

def mostrar_info_personajes(*args):
    infopersonajes.place_forget()
    ventanapersonajes.pack_forget()
    close_info_personajes_button.pack()
    label_lista.pack(padx=10, pady=10)
    ventana_info_personajes.pack(fill="both", expand=True)
    infolabelpersonajes.pack()
infopersonajes.config(command=mostrar_info_personajes)

def close_info_perosnajes():
    label_lista.pack_forget()
    close_info_personajes_button.pack_forget()
    ventana_info_personajes.pack_forget()
    ventanapersonajes.pack()
    infopersonajes.place(relx=0.1, rely=0.9)
close_info_personajes_button.config(command=close_info_perosnajes)


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
    infopersonajes.place_forget()


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

cuadromapa = tk.LabelFrame(cuadrogris)
cuadromapa.configure(bg="gray", width=200, height=200)

imagenmapa = tk.PhotoImage(file= "mapa.png")
imagenmapa_pequeno = imagenmapa.subsample(8,8)
labelimagenmapa = tk.Label(cuadromapa, image=imagenmapa_pequeno)


mapa = tk.Button(cuadrogris, text="Mapa")

def statsbox():
    cuadrogris.pack(fill="both", expand=True)
    iraljuegobutton.pack_forget()

    cuadromapa.place(relx=0.8, rely=0.1)
    labelimagenmapa.grid()
    otrocuadrogris.configure(width=350, height=175, bg="light grey")
    otrocuadrogris.grid(row=0, column=0)
    otrocuadromas.grid(row=0, column=0)

    my_nombre_en_cuadrogris.grid()
    my_nombre_en_cuadrogris.config(text=f"Jugador: {playername}        Personajes: {personajes_texto}")
    mapa.grid()
iraljuegobutton.config(command=statsbox)

escena1 = tk.Button(cuadrogris, text= "Palacio")
escena2 = tk.Button(cuadrogris, text= "Rancho")
escena3 = tk.Button(cuadrogris, text= "Bahía")
escena4 = tk.Button(cuadrogris, text= "Escuela")
escena5 = tk.Button(cuadrogris, text= "El campo")

global closemapa
closemapa= tk.Button(cuadrogris, text= "Cerrar mapa")
def  funcion_de_mapabutton():
    escena1.place(relx=0.3, rely=0.2)
    escena2.place(relx=0.1, rely=0.4)
    escena3.place(relx=0.3, rely=0.4)
    escena4.place(relx=0.4, rely=0.2)
    escena5.place(relx=0.45, rely=0.4)
    mapa.grid_forget()
    
    closemapa.grid()

mapa.config(command=funcion_de_mapabutton)

def funcion_de_closemapaButton():
    closemapa.grid_forget()
    mapa.grid()
    escena1.place_forget()
    escena2.place_forget()
    escena3.place_forget()
    escena4.place_forget()
    escena5.place_forget()
closemapa.config(command=funcion_de_closemapaButton)


window1.mainloop()