import tkinter as tk
window1 = tk.Tk()
window1.geometry("1080x1080")


stats_personajes = {
    "Patrolclo": {"vida": 100, "atq": 20, "defe": 15},
    "Benzemá": {"vida": 120, "atq": 15, "defe": 25},
    "Juan": {"vida": 90, "atq": 25, "defe": 10},
    "Seis": {"vida": 110, "atq": 18, "defe": 18},
    "Veroliz": {"vida": 85, "atq": 30, "defe": 5},
    "Esteban": {"vida": 150, "atq": 10, "defe": 30},
    "Jeff": {"vida": 100, "atq": 22, "defe": 12},
    "Elena": {"vida": 95, "atq": 28, "defe": 8},
    "Leylani": {"vida": 105, "atq": 20, "defe": 20},
    "Pancracio": {"vida": 130, "atq": 12, "defe": 22},
    "Yomelaximohamillyilmar Cariliana": {"vida": 200, "atq": 5, "defe": 40},
    "Don Krilinger": {"vida": 80, "atq": 35, "defe": 5},
    "Mateo": {"vida": 115, "atq": 17, "defe": 20}
}

botonataque = tk.Button(window1, text="atacar")
botonataque.place(relx=0.8, rely=0.70)

infomia = tk.Label(window1, text="vida")
infomia.place(relx=0.8, rely=0.60)

inforival= tk.Label(window1, text="vida: rival")
inforival.place(relx=0.2, rely=0.15)

exitbutton= tk.Button(window1, text="Salir")
exitbutton.place(relx=0.01, rely=0.01)

cambio1 = tk.Button(window1, text= "personaje1")
cambio1.place(relx=0.93, rely=0.45)

cambio2 = tk.Button(window1, text="personaje 2")
cambio2.place(relx=0.93, rely=0.5)


window1. mainloop()