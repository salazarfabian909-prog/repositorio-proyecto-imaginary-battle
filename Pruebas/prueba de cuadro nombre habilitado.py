import tkinter as tk
ventana = tk.Tk()
ventana.geometry("720x1080")

def verificar_entrada(*args):
    if textcube.get().strip():
        textcubebutton.config(state="normal")
    else:
        textcubebutton.config(state="disabled")

variable = tk.StringVar()


textcube = tk.Entry(ventana, textvariable=variable)
textcube.pack(pady=10)

textcubebutton = tk.Button(text="Continuar", state="disabled")
textcubebutton.pack()
variable.trace_add("write", verificar_entrada)

ventana.mainloop()