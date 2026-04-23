import tkinter as tk
ventana = tk.Tk()
ventana.geometry("1000x1000")

cuadrogris = tk.LabelFrame(ventana)
cuadrogris.configure(bg="light grey")
cuadrogris.configure(width=350, height=170)
cuadrogris.grid()

ventana.mainloop()