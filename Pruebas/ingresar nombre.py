import tkinter as tk
ventana = tk.Tk()
ventana.geometry("1080x1080")

saludo_inicial = tk.Label(ventana, text= "Hola, bienvenido al mundo de """)
saludo_inicial.pack()

ingresar_button = tk.Button(ventana, text= "continuar")
ingresar_button.pack()

guardar_nombre = tk.Button(ventana, text= "Guardar nombre")

cuadro_nombre = tk.Entry()  

def introducir_nombre():
    saludo_inicial.configure(text="¿Como te llamas?")
    cuadro_nombre.pack()
    ingresar_button.pack_forget()
    guardar_nombre.pack()

    

ingresar_button.config(command= introducir_nombre)

def myname():
    myname1 = cuadro_nombre.get()
    myname2 = tk.Label(text=myname1)
    myname2.pack()

guardar_nombre.config(command= myname)






ventana.mainloop()