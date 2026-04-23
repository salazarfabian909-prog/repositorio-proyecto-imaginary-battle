import tkinter as tk
ventana = tk.Tk()

ventana.title("juego prueba")
ventana.geometry("1080x720") #la primera linea llamada ventana abre una ventana, la segunda da el titulo a la ventana, la pone su resolucion inicial


etiqueta = tk.Label(ventana, text="¿hola?")
etiqueta.configure(font=("Arial, 14"))
etiqueta.pack() #la primera linea crea una etiqueta que dice "¿hola?", la segunda da el tipo de letra y su tamaño, esta linea llama a la etiqueta


startbutton = tk.Frame(ventana)
startbutton.configure(width = 300, height=200, bd =5)

startbutton.pack() #esta seccion crea un cuadro y lo llama

boton = tk.Button(startbutton, text= "continuar")
boton.configure(font=("Arial, 14"))
boton.pack() #esta define el boton "continuar, le la tipo de letra, tamaño, y la lama

def funcion_boton():
    etiqueta.config(text="¿estás ahí?")

boton.config(command = funcion_boton)

etiqueta2 = tk.Label(ventana, text="ingrese su nombre de jugador")
etiqueta2.pack()

ingresarnombre = tk.Entry(ventana)
ingresarnombre.pack()

def guardar_nombre():
    nametag = ingresarnombre.get()
    etiqueta2.config(text=nametag)

boton_nombre = tk.Button(ventana, text= "Aplicar nombre", command = guardar_nombre)
boton_nombre.pack()









ventana.mainloop()
#hacer laberframe de personajes
