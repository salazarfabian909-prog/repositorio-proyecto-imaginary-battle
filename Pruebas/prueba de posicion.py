import tkinter as tk

ventana = tk.Tk()
ventana.title("Prueba de Posición")
ventana.geometry("400x300")

texto1 = tk.Label(ventana, text="celda 1")
texto1.grid(row=0, column=0,padx=5, pady=5)
 
texto2 =tk.Label(ventana, text= "celda 2")
texto2.grid(row=0, column=1, padx=5, pady=5)

texto3 = tk.Label(ventana, text="celda 3")
texto3.grid(row=1, column=0, padx=5, pady=5)

texto4 = tk.Label(ventana, text="celda 4")
texto4.grid(row=1, column=1, padx=5, pady=5)


ventana.mainloop()