import tkinter as tk

characterwindow = tk.Tk()
characterwindow.title("seleccion de personajes")
characterwindow.geometry("1080x1080")

label1 = tk.Label(text="Seleciona tus personajes")
label1.pack()

checkvar = tk.BooleanVar()

option1 = tk.Checkbutton(characterwindow, text="personaje", variable=checkvar)
option1.pack()

character_save = tk.Button(text= "Guardar personajes")
character_save.pack()


def characterselect():
    label2 = tk.Label(characterwindow, text= checkvar)
    label2.pack()

character_save.config(command= characterselect)


characterwindow.mainloop()