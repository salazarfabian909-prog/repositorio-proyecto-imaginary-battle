import tkinter as tk

ventana = tk.Tk()
ventana.geometry("1080x720")

namebox = tk.Entry()
namebox.pack()

namebutton = tk.Button(text= "continuar")
namebutton.pack()

nametext = tk.Label()

continuebutton = tk.Button(text="continuar")

characterselectiontext = tk.Label(ventana, text= "Ahora, selecciona a los personajes de preferencia")
def personajes():
    characterselectiontext.pack()
continuebutton.config(command= personajes)

def guardarnombre():
    savename = namebox.get()
    nametext.configure(text=f"Tu nombre es {savename}")
    nametext.pack()
    namebox.pack_forget()
    namebutton.pack_forget()
    ventana.after(2000, nametext.pack_forget)
    ventana.after(2500, continuebutton.pack)
namebutton.config(command= guardarnombre)



ventana.mainloop()