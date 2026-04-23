import tkinter as tk
ventana = tk.Tk()
ventana.geometry("1080x720")

boton1 = tk.Frame(ventana)
boton1.configure(width=300, height=300, bg="gray", bd= 5)

boton1.pack()

boton2 = tk.Button(boton1, text="hola")
boton2.place(x=10, y=20)
boton2.pack


ventana.mainloop()