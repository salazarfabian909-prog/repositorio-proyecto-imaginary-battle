import tkinter as tk
from tkinter import messagebox
import random


window1 = tk.Tk()
window1.state("zoomed") #hace que la ventana se abra en pantalla completa
window1.configure(padx=0, pady=0,highlightthickness=0) #el hight... hace que el grosor no resalte si está en cero
window1.title("Imaginary Battles")

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
    labelinfo.pack(pady=20) # Añadimos un poco de margen arriba
    
    global labelinfolabel
    # Añadimos wraplength para que el texto quepa en la pantalla
    labelinfolabel = tk.Label(labelinfo, font="Arial, 20", 
                              text="Este juego es trabajo del proyecto imaginary battles, en este juego te adentraras en un " \
                                   "mundo donde existen criaturas llamadas hollos, a quienes debes derrotar para terminar la historia",
                              wraplength=600, justify="center")
    
    # Especificamos filas (row) para que no se encimen
    labelinfolabel.grid(row=0, column=0, padx=20, pady=10)
    labelinfoclosebutton.grid(row=1, column=0, pady=20)
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

personajes_salvados = []

zonas_completadas = []

ZONAS_TOTALES = 5

def ir_a_galeria(*args):
    ventanapersonajes.pack()
    infopersonajes.place(relx=0.1, rely= 0.9)
    galeriabutton1.pack_forget()
galeriabutton1.config(command= ir_a_galeria)

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
    "Mateo": {"vida": 115, "atq": 17, "defe": 20},
    "Roberto": {"vida": 90, "atq": 35, "defe": 10},
    "Cebolla": {"vida": 70, "atq": 40, "defe": 3}}
global ventana_info_personajes

nombres_lista = list(stats_personajes.keys())

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
    else:
        botoncontinue.configure(state="disabled")
vars_check = [] #aqui se guarda la información los estados de seleccion de cada personaje

mis_personajes = []

mis_botones = [] #crea dos listas

#crea labels de los 15 personajes, y checkbuttons para seleccionarlos, y los mete en la lista de mis_personajes y mis_botones respectivamente, para luego ser usados en la función de guardar personajes
for i in range(len(nombres_lista)):
    var = tk.IntVar()
    vars_check.append(var) #mete el "sensor" var, crado anteriormente a vars_check, para observar en tiempo 
    lbl = tk.Label(ventanapersonajes, text=nombres_lista[i], font= "Arial, 18") #real lo marcado
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

#función que guarda los personajes seleccionados, y luego muestra un mensaje de confirmación con los personajes elegidos, para después mostrar el botón que te llevará al juego, y también guarda la información de los personajes seleccionados en variables globales para ser usadas en el juego
def guardarpersonajes(*args):

    global texto_personaje1, texto_personaje2, texto_personaje3, personajes_texto, mispersonajes
    mispersonajes = []
    for i in range(len(vars_check)):
        if vars_check[i].get() == 1: #si el espacio del checkbutton = 1, se guarda, osea, si está marcado
            stats_copia = stats_personajes[nombres_lista[i]].copy()
            # Guardamos la vida máxima para poder curarlos después
            vida_maxima = stats_copia['vida']
            mispersonajes.append({
                "nombre": nombres_lista[i], 
                "stats": stats_copia,
                "vida_max": vida_maxima
             })
    # Esta linea lee lo marcado para guardarlo para despues, y ser usado como texto de confirmación, y también para mostrarlo en la interfaz de juego
    personajes_texto = ", ".join([p["nombre"] for p in mispersonajes])
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
    texto_personaje1 = f"{mispersonajes[0]['nombre']}"
    texto_personaje2 = f"{mispersonajes[1]['nombre']}"
    texto_personaje3 = f"{mispersonajes[2]['nombre']}"
    botones_cambio_personaje()
    if len(mispersonajes) == 3:
        # Accedemos a ['stats']['vida'] en lugar de solo ['vida']
        personaje_en_uso.config(
            text=f"En uso: {mispersonajes[2]['nombre']} | Vida: {mispersonajes[2]['stats']['vida']}"
        )
        cambio_a_personaje1.config(text=f"Cambiar a {mispersonajes[0]['nombre']}")
        cambio_a_personaje2.config(text=f"Cambiar a {mispersonajes[1]['nombre']}")
    actualizar_interfaz_combate()
    

botoncontinue.config(command=guardarpersonajes)

cuadrogris = tk.LabelFrame(window1)
cuadrogris.configure(bd=0, relief="flat") #relief controla el efecto de sombra, flat hace que no tenga efectos de sombra
cuadrogris.propagate(False)

otrocuadrogris = tk.LabelFrame(cuadrogris, font="Arial, 20")

otrocuadromas = tk.LabelFrame(otrocuadrogris, font="Arial, 15")

my_nombre_en_cuadrogris = tk.Label(otrocuadromas, font="Arial, 15")
label_rescatados = tk.Label(otrocuadromas, font="Arial, 15", fg="green")
label_rescatados.grid(row=1, column=0)

cuadromapa = tk.LabelFrame(cuadrogris)
cuadromapa.configure(bg="gray", width=200, height=200)

imagenmapa = tk.PhotoImage(file= "mapa3.png")
imagenmapa_pequeno = imagenmapa.subsample(8,8)
labelimagenmapa = tk.Label(cuadromapa, image=imagenmapa_pequeno)

mapa = tk.Button(cuadrogris, text="Mapa")

#función que muestra la interfaz de juego, con el mapa, los personajes rescatados, y el nombre del jugador, además de ocultar el botón que te lleva a esta interfaz
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
    actualizar_personajes_rescatados()
    mapa.grid()
iraljuegobutton.config(command=statsbox)

escena1 = tk.Button(cuadrogris, text= "Palacio")
escena2 = tk.Button(cuadrogris, text= "Rancho")
escena3 = tk.Button(cuadrogris, text= "Bahía")
escena4 = tk.Button(cuadrogris, text= "Escuela")
escena5 = tk.Button(cuadrogris, text= "El campo")

global closemapa
closemapa= tk.Button(cuadrogris, text= "Cerrar mapa")
#función que muestra los botones de las escenas, y también deshabilita los botones de las escenas que ya se han completado, además de ocultar el botón del mapa y mostrar el botón de cerrar mapa
def funcion_de_mapabutton():
    # Mostrar los botones
    escena1.place(relx=0.3, rely=0.2)
    escena2.place(relx=0.1, rely=0.4)
    escena3.place(relx=0.3, rely=0.4)
    escena4.place(relx=0.4, rely=0.2)
    escena5.place(relx=0.45, rely=0.4)
    
    # Lógica para deshabilitar si ya se completó
    if "Palacio" in zonas_completadas: escena1.config(state="disabled", text="Palacio (LIBRE)")
    if "Rancho" in zonas_completadas: escena2.config(state="disabled", text="Rancho (LIBRE)")
    if "Bahía" in zonas_completadas: escena3.config(state="disabled", text="Bahía (LIBRE)")
    if "Escuela" in zonas_completadas: escena4.config(state="disabled", text="Escuela (LIBRE)")
    if "El campo" in zonas_completadas: escena5.config(state="disabled", text="El campo (LIBRE)")
    
    mapa.grid_forget()
    closemapa.grid()

mapa.config(command=funcion_de_mapabutton)
#cierra el mapa y vuelve a la interfaz de juego, además de ocultar los botones de las escenas y el botón de cerrar mapa
def funcion_de_closemapaButton():
    closemapa.grid_forget()
    mapa.grid()
    escena1.place_forget()
    escena2.place_forget()
    escena3.place_forget()
    escena4.place_forget()
    escena5.place_forget()
closemapa.config(command=funcion_de_closemapaButton)

botonatk = tk.Button(cuadrogris, text="Atacar")
botonexit = tk.Button(cuadrogris, text="Salir del combate")

hollows_stats = {
    "Hollo1": {"vida": 80, "atq": 15, "defe": 10},
    "Hollo2": {"vida": 120, "atq": 20, "defe": 15},
    "Hollo3": {"vida": 100, "atq": 18, "defe": 12},
    "Hollo4": {"vida": 90, "atq": 22, "defe": 8},
    "Hollo5": {"vida": 110, "atq": 25, "defe": 20}}

#codigo creado por gemini, esta función genera un grupo de enemigos para cada escena, con un hollow y tres personajes de apoyo, y guarda la información en una lista de diccionarios para cada escena
def generar_grupo(nombre_hollow, nombres_apoyo):
    grupo = [{"nombre": nombre_hollow, "stats": hollows_stats[nombre_hollow], "vida": hollows_stats[nombre_hollow]['vida']}]
    for n in nombres_apoyo:
        grupo.append({"nombre": n, "stats": stats_personajes[n], "vida": stats_personajes[n]['vida']})
    return grupo

# Definimos los grupos aquí afuera para que sean globales de verdad
grupo_escena1 = generar_grupo('Hollo1', random.sample(nombres_lista, 3))
grupo_escena2 = generar_grupo('Hollo2', random.sample(nombres_lista, 3))
grupo_escena3 = generar_grupo('Hollo3', random.sample(nombres_lista, 3))
grupo_escena4 = generar_grupo('Hollo4', random.sample(nombres_lista, 3))
grupo_escena5 = generar_grupo('Hollo5', random.sample(nombres_lista, 3))

global rival_actual
rival_actual = None

class enemigos:
    # esta seccion es para mostrar las estadísticas de los enemigos en cada escena, y también para mostrar el nombre del rival actual, además de guardar la información de los enemigos en variables globales para ser usadas en el combate
    global texto
    texto = ""
    # Leemos directamente del grupo que ya creaste arriba
    for enemigo in grupo_escena1:
        n = enemigo['nombre']
        s = enemigo['stats']
        texto += f"{n}: vida:{s['vida']}, atq:{s['atq']}, defe:{s['defe']}\n"
    
    global label_stats_random
    label_stats_random = tk.Label(cuadrogris, text=f"Enemigos de la zona:\n{texto}", justify="left", font=("Arial", 12))

    global texto2
    texto2 = ""
    # Leemos directamente del grupo que ya creaste arriba
    for enemigo in grupo_escena2:
        n = enemigo['nombre']
        s = enemigo['stats']
        texto2 += f"{n}: vida:{s['vida']}, atq:{s['atq']}, defe:{s['defe']}\n"
    
    global label_stats_random2
    label_stats_random2 = tk.Label(cuadrogris, text=f"Enemigos de la zona:\n{texto2}", justify="left", font=("Arial", 12))

    global texto3
    texto3 = ""
    # Leemos directamente del grupo que ya creaste arriba
    for enemigo in grupo_escena3:
        n = enemigo['nombre']
        s = enemigo['stats']
        texto3 += f"{n}: vida:{s['vida']}, atq:{s['atq']}, defe:{s['defe']}\n"

    global label_stats_random3
    label_stats_random3 = tk.Label(cuadrogris, text=f"Enemigos de la zona:\n{texto3}", justify="left", font=("Arial", 12))
    
    global texto4
    texto4 = ""
    # Leemos directamente del grupo que ya creaste arriba
    for enemigo in grupo_escena4:
        n = enemigo['nombre']
        s = enemigo['stats']
        texto4 += f"{n}: vida:{s['vida']}, atq:{s['atq']}, defe:{s['defe']}\n"

    global label_stats_random4
    label_stats_random4 = tk.Label(cuadrogris, text=f"Enemigos de la zona:\n{texto4}", justify="left", font=("Arial", 12))

    global texto5
    texto5 = ""
    # Leemos directamente del grupo que ya creaste arriba
    for enemigo in grupo_escena5:
        n = enemigo['nombre']
        s = enemigo['stats']
        texto5 += f"{n}: vida:{s['vida']}, atq:{s['atq']}, defe:{s['defe']}\n"

    global label_stats_random5
    label_stats_random5 = tk.Label(cuadrogris, text=f"Enemigos de la zona:\n{texto5}", justify="left", font=("Arial", 12))


    global label_rival_escena1, label_rival_escena2, label_rival_escena3, label_rival_escena4, label_rival_escena5
    
    label_rival_escena1 = tk.Label(cuadrogris, text="", font="Arial, 20", fg="red")
    label_rival_escena2 = tk.Label(cuadrogris, text="", font="Arial, 20", fg="red")
    label_rival_escena3 = tk.Label(cuadrogris, text="", font="Arial, 20", fg="red")
    label_rival_escena4 = tk.Label(cuadrogris, text="", font="Arial, 20", fg="red")
    label_rival_escena5 = tk.Label(cuadrogris, text="", font="Arial, 20", fg="red")

#codigo creado por gemini, esta función actualiza la información de los personajes rescatados en la interfaz de juego, mostrando sus nombres en un label específico, o indicando que no hay ninguno rescatado si la lista está vacía
def actualizar_personajes_rescatados():
    if personajes_salvados:
        nombres = ", ".join([p['nombre'] for p in personajes_salvados])
        label_rescatados.config(text=f"Rescatados: {nombres}")
    else:
        label_rescatados.config(text="Rescatados: Ninguno")

#codigo creado por gemini, esta función cura a todo el equipo completo, restaurando su vida al máximo, y luego actualiza la interfaz de combate para reflejar los cambios en la vida de los personajes
def curar_equipo_completo():
    global mispersonajes
    for personaje in mispersonajes:
        personaje['stats']['vida'] = personaje['vida_max']
    
    actualizar_interfaz_combate()

#esta función es para mostrar los botones de cambio de personaje, y también para asignar la función de cambio de personaje a cada botón, usando lambda para pasar el índice correcto del personaje de reserva a la función de cambio
def botones_cambio_personaje():
    global cambio_a_personaje1, cambio_a_personaje2, personaje_en_uso
    
    # Los creamos con textos genéricos que luego cambiaremos
    cambio_a_personaje1 = tk.Button(cuadrogris, text="Reserva 1")
    cambio_a_personaje2 = tk.Button(cuadrogris, text="Reserva 2")
    personaje_en_uso = tk.Label(cuadrogris, text="Cargando...", font="Arial 18", fg="blue")
    
    # IMPORTANTE: Asignar la función de intercambio aquí
    cambio_a_personaje1.config(command=lambda: cambiar_personaje(0))
    cambio_a_personaje2.config(command=lambda: cambiar_personaje(1))

#codigo creado por gemini, esta función cambia el personaje en uso por uno de los personajes de reserva, verificando que el personaje de reserva tenga vida mayor a cero antes de hacer el cambio, y luego actualiza la interfaz de combate para reflejar el cambio de personaje
def seleccionar_proximo_rival(grupo, label_escena, nombre_zona):
    global rival_actual, personajes_salvados, zonas_completadas
    aliados_vivos = [e for e in grupo[1:] if e['vida'] > 0]
    
    if aliados_vivos:
        rival_actual = aliados_vivos[0]
        label_escena.config(text=f"Rival: {rival_actual['nombre']} | Vida: {rival_actual['vida']}", fg="red")
    else:
        hollow = grupo[0]
        if hollow['vida'] > 0:
            rival_actual = hollow
            label_escena.config(text=f"hollow: {rival_actual['nombre']} | Vida: {rival_actual['vida']}", fg="purple")
        else:
            rival_actual = None
            label_escena.config(text="¡Victoria! Zona despejada", fg="green")
            
            if nombre_zona not in zonas_completadas:
                zonas_completadas.append(nombre_zona)
            
            # --- Lógica de Fin del Juego ---
            if len(zonas_completadas) == ZONAS_TOTALES:
                messagebox.showinfo("¡FELICIDADES!", f"¡Increíble, {playername}! Has limpiado todas las zonas y terminado el juego.")
                # Opcional: puedes cerrar el juego o deshabilitar botones aquí
            else:
                # Lógica de rescate existente
                aliados_en_zona = grupo[1:] 
                for aliado in aliados_en_zona:
                    if aliado['nombre'] not in [p['nombre'] for p in personajes_salvados]:
                        personajes_salvados.append(aliado)
                actualizar_personajes_rescatados()
                messagebox.showinfo("Zona Liberada", f"Has limpiado el {nombre_zona}. ¡Sigue así!")

#codigo creado por gemini, esta función actualiza la interfaz de combate, mostrando la información del personaje en uso y los personajes de reserva, además de deshabilitar los botones de cambio de personaje si el personaje de reserva está derrotado
def actualizar_interfaz_combate():
    global mispersonajes, cambio_a_personaje1, cambio_a_personaje2, personaje_en_uso
    
    # 1. Actualizar el label del personaje que está peleando actualmente (índice 2)
    personaje_en_uso.config(
        text=f"En uso: {mispersonajes[2]['nombre']} | Vida: {mispersonajes[2]['stats']['vida']}",
        fg="blue" if mispersonajes[2]['stats']['vida'] > 0 else "gray"
    )
    
    # 2. Actualizar Botón de Reserva 1 (índice 0)
    if mispersonajes[0]['stats']['vida'] <= 0:
        cambio_a_personaje1.config(text=f"{mispersonajes[0]['nombre']} (DERROTADO)", state="disabled", fg="gray")
    else:
        cambio_a_personaje1.config(text=f"Cambiar a {mispersonajes[0]['nombre']}", state="normal", fg="black")

    # 3. Actualizar Botón de Reserva 2 (índice 1)
    if mispersonajes[1]['stats']['vida'] <= 0:
        cambio_a_personaje2.config(text=f"{mispersonajes[1]['nombre']} (DERROTADO)", state="disabled", fg="gray")
    else:
        cambio_a_personaje2.config(text=f"Cambiar a {mispersonajes[1]['nombre']}", state="normal", fg="black")

#codigo creado por gemini, funcion del boton atk, esta calcula el daño en base a la funcion recursiva de calculo de daño, luego actualiza la vida del rival actual,
#  y dependiendo de la escena en la que se esté peleando, identifica el label correspondiente para actualizar la información del rival, y si el rival es derrotado, 
# muestra un mensaje de victoria y llama a la función para seleccionar al próximo rival, pasando el grupo, el label y el nombre de la zona como argumentos
def atacar_enemigo():
    global rival_actual, mispersonajes
    
    if rival_actual is None or rival_actual['vida'] <= 0:
        return

    # --- Lógica de ataque (se mantiene igual) ---
    atq_jugador = mispersonajes[2]['stats']['atq']
    def_rival = rival_actual['stats']['defe']
    dano_final = calculo_de_dano(atq_jugador, def_rival)
    
    rival_actual['vida'] = max(0, rival_actual['vida'] - dano_final)
    label_obj = None
    grupo_obj = None
    nombre_zona_actual = "" # Nueva variable para el nombre

    if label_rival_escena1.winfo_viewable(): 
        label_obj, grupo_obj, nombre_zona_actual = label_rival_escena1, grupo_escena1, "Palacio"
    elif label_rival_escena2.winfo_viewable(): 
        label_obj, grupo_obj, nombre_zona_actual = label_rival_escena2, grupo_escena2, "Rancho"
    elif label_rival_escena3.winfo_viewable(): 
        label_obj, grupo_obj, nombre_zona_actual = label_rival_escena3, grupo_escena3, "Bahía"
    elif label_rival_escena4.winfo_viewable(): 
        label_obj, grupo_obj, nombre_zona_actual = label_rival_escena4, grupo_escena4, "Escuela"
    elif label_rival_escena5.winfo_viewable(): 
        label_obj, grupo_obj, nombre_zona_actual = label_rival_escena5, grupo_escena5, "El campo"

    if label_obj:
        label_obj.config(text=f"Rival: {rival_actual['nombre']} | Vida: {rival_actual['vida']}")

        if rival_actual['vida'] <= 0:
            messagebox.showinfo("Victoria", f"¡{rival_actual['nombre']} derrotado!")
            # LLAMADA CORREGIDA CON EL TERCER ARGUMENTO:
            seleccionar_proximo_rival(grupo_obj, label_obj, nombre_zona_actual)
        else:
            window1.after(1000, lambda g=grupo_obj, l=label_obj: turno_rival(g, l))
            
botonatk.config(command=atacar_enemigo)

def cambiar_personaje(indice_reserva):
    global mispersonajes

    if mispersonajes[indice_reserva]['stats']['vida'] <= 0:
        messagebox.showwarning("Incapacitado", f"¡{mispersonajes[indice_reserva]['nombre']} está derrotado y no puede luchar!")
        return # Sale de la función sin cambiar

    personaje_actual = mispersonajes[2]
    mispersonajes[2] = mispersonajes[indice_reserva]
    mispersonajes[indice_reserva] = personaje_actual
    
    personaje_en_uso.config(
        text=f"En uso: {mispersonajes[2]['nombre']} | Vida: {mispersonajes[2]['stats']['vida']}"
    )
    
    actualizar_interfaz_combate()

def turno_rival(grupo, label_escena):
    global rival_actual, mispersonajes
    
    if rival_actual is None or rival_actual['vida'] <= 0 or mispersonajes[2]['stats']['vida'] <= 0:
        return

    accion = random.choices(["atacar", "cambiar"], weights=[0.8, 0.2])[0]

    if accion == "cambiar":
        opciones = [e for i, e in enumerate(grupo) if i != 0 and e != rival_actual and e['vida'] > 0]
        if opciones:
            rival_actual = random.choice(opciones)
            messagebox.showinfo("IA Rival", f"El enemigo ha cambiado a {rival_actual['nombre']}!")
            label_escena.config(text=f"Rival: {rival_actual['nombre']} | Vida: {rival_actual['vida']}")
        else:
            accion = "atacar"

    if accion == "atacar":
        dano = calculo_de_dano(rival_actual['stats']['atq'], mispersonajes[2]['stats']['defe'])
        mispersonajes[2]['stats']['vida'] = max(0, mispersonajes[2]['stats']['vida'] - dano)
        
        # Actualizamos la interfaz para ver el daño y si los botones deben ponerse grises
        actualizar_interfaz_combate()

        if mispersonajes[2]['stats']['vida'] <= 0:
            messagebox.showerror("Personaje Derrotado", f"¡{mispersonajes[2]['nombre']} ha caído!")
            
            # Intentar cambiar al primer reserva (índice 0)
            if mispersonajes[0]['stats']['vida'] > 0:
                cambiar_personaje(0)
                messagebox.showinfo("Relevo Automático", f"¡{mispersonajes[2]['nombre']} entra al combate!")
            # Si el primero está muerto, intentar con el segundo (índice 1)
            elif mispersonajes[1]['stats']['vida'] > 0:
                cambiar_personaje(1)
                messagebox.showinfo("Relevo Automático", f"¡{mispersonajes[2]['nombre']} entra al combate!")
            else:
                messagebox.showerror("GAME OVER", "Todos tus personajes han sido derrotados...")
                window1.destroy() # O la lógica de reinicio que prefieras

#aqui empieza la parte de las escenas, cada función de escena hace lo mismo pero con los enemigos y labels correspondientes a
#  cada escena, además de llamar a la función de seleccionar próximo rival con el grupo, label y nombre de zona correspondiente
class escenas:
    def escenapelea1():
        escena1.place_forget()
        escena2.place_forget()
        escena3.place_forget()
        escena4.place_forget()
        escena5.place_forget()
        cuadromapa.place_forget()
        otrocuadromas.grid_forget()
        mapa.grid_forget()
        closemapa.grid_forget()
        otrocuadrogris.grid_forget()
        botonatk.place(relx=0.8, rely=0.6)
        botonexit.place(relx=0.9, rely=0.1)
        label_stats_random.place(relx=0.1, rely=0.2)
        label_rival_escena1.place(relx=0.1, rely=0.1)
        seleccionar_proximo_rival(grupo_escena1, label_rival_escena1, "Palacio")
        cambio_a_personaje1.place(relx=0.8, rely=0.4)
        cambio_a_personaje2.place(relx=0.8, rely=0.45)
        personaje_en_uso.place(relx=0.7, rely=0.5)
        
    escena1.config(command= escenapelea1)

    def escenapelea2():
        escena1.place_forget()
        escena2.place_forget()
        escena3.place_forget()
        escena4.place_forget()
        escena5.place_forget()
        cuadromapa.place_forget()
        otrocuadromas.grid_forget()
        mapa.grid_forget()
        closemapa.grid_forget()
        otrocuadrogris.grid_forget()
        botonatk.place(relx=0.8, rely=0.6)
        botonexit.place(relx=0.9, rely=0.1)
        label_rival_escena2.place(relx=0.1, rely=0.1)
        label_stats_random2.place(relx=0.1, rely=0.2)
        seleccionar_proximo_rival(grupo_escena2, label_rival_escena2, "Rancho")
        cambio_a_personaje1.place(relx=0.8, rely=0.4)
        cambio_a_personaje2.place(relx=0.8, rely=0.45)
        personaje_en_uso.place(relx=0.7, rely=0.5)
    escena2.config(command= escenapelea2)

    def escenapelea3():
        escena1.place_forget()
        escena2.place_forget()
        escena3.place_forget()
        escena4.place_forget()
        escena5.place_forget()
        cuadromapa.place_forget()
        otrocuadromas.grid_forget()
        mapa.grid_forget()
        closemapa.grid_forget()
        otrocuadrogris.grid_forget()
        botonatk.place(relx=0.8, rely=0.6)
        botonexit.place(relx=0.9, rely=0.1)
        label_rival_escena3.place(relx=0.1, rely=0.1)
        label_stats_random3.place(relx=0.1, rely=0.2)
        seleccionar_proximo_rival(grupo_escena3, label_rival_escena3, "Bahía")
        cambio_a_personaje1.place(relx=0.8, rely=0.4)
        cambio_a_personaje2.place(relx=0.8, rely=0.45)
        personaje_en_uso.place(relx=0.7, rely=0.5)
    escena3.config(command= escenapelea3)

    def escenapelea4():
        escena1.place_forget()
        escena2.place_forget()
        escena3.place_forget()
        escena4.place_forget()
        escena5.place_forget()
        cuadromapa.place_forget()
        otrocuadromas.grid_forget()
        mapa.grid_forget()
        closemapa.grid_forget()
        otrocuadrogris.grid_forget()
        botonatk.place(relx=0.8, rely=0.6)
        botonexit.place(relx=0.9, rely=0.1)
        label_rival_escena4.place(relx=0.1, rely=0.1)
        label_stats_random4.place(relx=0.1, rely=0.2)
        
        seleccionar_proximo_rival(grupo_escena4, label_rival_escena4, "Escuela")
        cambio_a_personaje1.place(relx=0.8, rely=0.4)
        cambio_a_personaje2.place(relx=0.8, rely=0.45)
        personaje_en_uso.place(relx=0.7, rely=0.5)
    escena4.config(command= escenapelea4)

    def escenapelea5():
        escena1.place_forget()
        escena2.place_forget()
        escena3.place_forget()
        escena4.place_forget()
        escena5.place_forget()
        cuadromapa.place_forget()
        otrocuadromas.grid_forget()
        mapa.grid_forget()
        closemapa.grid_forget()
        otrocuadrogris.grid_forget()
        botonatk.place(relx=0.8, rely=0.6)
        botonexit.place(relx=0.9, rely=0.1)
        label_rival_escena5.place(relx=0.1, rely=0.1)
        label_stats_random5.place(relx=0.1, rely=0.2)
        seleccionar_proximo_rival(grupo_escena5, label_rival_escena5, "El campo")
        cambio_a_personaje1.place(relx=0.8, rely=0.4)
        cambio_a_personaje2.place(relx=0.8, rely=0.45)
        personaje_en_uso.place(relx=0.7, rely=0.5)
    escena5.config(command= escenapelea5)

    def botonexitfuncion():
        cuadromapa.place(relx=0.8, rely=0.1)
        labelimagenmapa.grid()
        otrocuadrogris.configure(width=350, height=175, bg="light grey")
        otrocuadrogris.grid(row=0, column=0)
        otrocuadromas.grid(row=0, column=0)
        my_nombre_en_cuadrogris.grid()
        mapa.grid()
        botonatk.place_forget()
        botonexit.place_forget()
        label_rival_escena1.place_forget()
        label_rival_escena2.place_forget()
        label_rival_escena3.place_forget()
        label_rival_escena4.place_forget()
        label_rival_escena5.place_forget()
        label_stats_random.place_forget()
        label_stats_random2.place_forget()
        label_stats_random3.place_forget()
        label_stats_random4.place_forget()
        label_stats_random5.place_forget()
        cambio_a_personaje1.place_forget()
        cambio_a_personaje2.place_forget()
        personaje_en_uso.place_forget()
        curar_equipo_completo()
        
    botonexit.config(command= botonexitfuncion)
#esta función es para calcular el daño, restando la defensa al ataque,
#  y si el resultado es menor o igual a cero, se llama a la función recursivamente con valores mínimos para asegurar que siempre se haga al menos 1 de daño
def calculo_de_dano(atq, defe):
    dano = atq - defe
    if dano > 0:
        return dano
    else:
        return calculo_de_dano(1, 0)



window1.mainloop()