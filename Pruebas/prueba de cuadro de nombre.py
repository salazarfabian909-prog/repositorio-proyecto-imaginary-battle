import tkinter as tk
ventana = tk.Tk()
ventana.geometry("1080x1080")

boton1 = tk.Button(ventana, text="boton de prueba")
boton1.pack()
def escribir_nombre():
    boton1.pack()
    cuadro = tk.Entry(ventana)
    cuadro.pack()
    butonguardarnombre = tk.Button(text="Guardar nombre")
    butonguardarnombre.pack()
    def guardar_nombre():
        nombre = cuadro.get()
        etiquetaname = tk.Label(text= nombre)
        etiquetaname.pack()
    butonguardarnombre.config(command= guardar_nombre)
boton1.config(command= escribir_nombre)


ventana.mainloop()