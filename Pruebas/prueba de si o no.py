import tkinter as tk
ventana = tk.Tk()
ventana.geometry("1080x1080")

etiqueta = tk.Label(ventana, text= "¿estas ahi?")
etiqueta.configure(font= "Arial, 12")
etiqueta.pack()


boton_si = tk.Frame(ventana)
boton_si.configure(width = 300, height=200, bd =5)
boton_si.pack()


boton1 = tk.Button(boton_si, text= "si")
boton1.configure(font="Arial, 12")
boton1.pack()

def cambio1():
    etiqueta.configure(text="ok, ecribe tu nombre a continuacion")

boton1.config(command=cambio1)

boton_no = tk.Frame(ventana)
boton_no.configure(width=300, height=400, bd=5)
boton_no.pack()

boton2 = tk.Button(boton_no, text="no")
boton2.configure(font="Arial, 12")
boton2.pack()

def cambio2():
    etiqueta.configure(text="mjm, con que graciosito no?, escriba su nombre")
boton2.config(command=cambio2)

ventana.mainloop()