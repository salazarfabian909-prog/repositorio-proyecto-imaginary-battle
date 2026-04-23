import tkinter as tk

ventana = tk.Tk()
ventana.geometry("1080x1080")

frame_info_de_personajes = tk.LabelFrame(ventana)
frame_info_de_personajes.configure(bd= 0, relief="flat", bg="gray")
frame_info_de_personajes.pack(fill="both", expand=True)

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

def mostrar_stats(nombre, *args):
    if nombre in stats_personajes:
        datos = stats_personajes[nombre]
        print(f"Stats de {nombre}: Vida={datos['vida']}, ATQ={datos['atq']}, DEF={datos['defe']}")

mostrar_stats("Mateo")

# 1. Crear el string con el formato de lista
texto_estadisticas = ""
for nombre, stats in stats_personajes.items():
    texto_estadisticas += f"{nombre}: Vida: {stats['vida']}, Atq: {stats['atq']}, Defe: {stats['defe']}\n"

# 2. Crear y empaquetar el Label
label_lista = tk.Label(
    frame_info_de_personajes, 
    text=texto_estadisticas, 
    justify="left",      # Alinea el texto a la izquierda
    bg="gray",           # Para que combine con tu frame
    fg="white",          # Color de letra (puedes cambiarlo)
    font=("Arial", 10)   # Fuente opcional
)
label_lista.pack(padx=10, pady=10)


ventana.mainloop()