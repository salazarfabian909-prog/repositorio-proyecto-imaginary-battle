import tkinter as tk
ventana = tk.Tk()
ventana.geometry("1080x1080")
ventana.title("Campo de pelea")


listaataque = ["ataque12", "curarse1"]
campoframe = tk.LabelFrame(ventana, text="ataque1")
campoframe.pack(fill="both", expand=True)

pelea1 = tk.Button(campoframe)
pelea1.grid(padx=5, pady=5, row=0, column=0)

ventana.mainloop()