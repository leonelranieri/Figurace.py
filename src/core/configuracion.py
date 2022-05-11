import PySimpleGUI as sg
from os import path
from json import (load as jsonload, dump as jsondump)

"""
    pantalla de configuracion del juego
    usa el formato json para guardar y cargar los datos
    en proceso de desarrollo
"""

ARCHIVO_CONFIG = path.join(".", "data", "config.json")
#la idea es que "dificultad" sirva para cambiar varios aspectos de la configuracion a la vez, pero que puedas seguir modificando cada una por separado 
DEFAULT_CONFIG = {
                "tiempo" : 15, 
                "rondas" : 10, 
                "suma" : 2, 
                "resta" : 2, 
                "cara" : 4, 
                "dificultad" : "normal"
}
DEFAULT_EASY = {
                "tiempo" : 20, 
                "rondas" : 5, 
                "suma" : 3, 
                "resta" : 1, 
                "cara" : 5, 
                "dificultad" : "facil"
}
DEFAULT_DIFFICULT = {
                "tiempo" : 10, 
                "rondas" : 45, 
                "suma" : 1, 
                "resta" : 3, 
                "cara" : 3, 
                "dificultad" : "dificil"
}
KEY_CONFIG = {
            "tiempo" : "-TIEMPO-",
            "rondas" : "-RONDAS-", 
            "suma" : "-SUMA-", 
            "resta" : "-RESTA-", 
            "cara" : "-CARACT-", 
            "dificultad" : "-DIFI-"
}


def carga_config():
    try:
        with open(ARCHIVO_CONFIG, "r") as entrada:
            configuracion = jsonload(entrada)
    except FileNotFoundError:
        configuracion = DEFAULT_CONFIG
        guarda_config(configuracion, None)
    
    return configuracion

def guarda_config(configuracion, values):
    if values:
        for key in KEY_CONFIG:
            configuracion[key] = values[KEY_CONFIG[key]]
    
    with open(ARCHIVO_CONFIG, "w") as salida:
        jsondump(configuracion, salida)


layout = [
        [sg.Text("Configuracion", font="Any 25", pad=((10, 0), 30))],
        [sg.Text("tiempo limite por ronda", pad=((10, 5), 20), 
                    text_color="black"), 
                    sg.OptionMenu(values=("10", "15", "20"), 
                    size=(5, 1), key="-TIEMPO-")
        ],
        [sg.Text("rondas por juego", pad=((10, 5), 20)), 
                    sg.OptionMenu(values=("5", "10", "45"), 
                    size=(5, 1), key=("-RONDAS-"))
        ],
        [sg.Text("puntaje sumado por respuesta correcta", 
                    pad=((10, 5), 20)), 
                    sg.OptionMenu(values=("1", "2", "3"), 
                    size=(3, 1), key=("-SUMA-"))
        ],
        [sg.Text("puntaje restado por respuesta incorrecta", 
                    pad=((10, 5), 20)), 
                    sg.OptionMenu(values=("1", "2", "3"), 
                    size=(3, 1), key=("-RESTA-"))
        ],
        [sg.Text("cantidad de caracteristicas a mostrar", 
                    pad=((10, 5), 20)), 
                    sg.OptionMenu(values=("3", "4", "5"), 
                    size=(3, 1), key=("-CARACT-"))
        ],
        [sg.Text("dificultad general", pad=((10, 5), 20)), 
                    sg.OptionMenu(values=("facil", "normal", 
                    "dificil", "Custom"),
                    size=(10, 1), key=("-DIFI-"))
        ],
        [sg.Text(size=(5, 1))],
        [sg.Button("Save"), sg.Button("Cancel")]
]

# ni idea que es finalize, pero si no lo pongo explota todo
window = sg.Window("Configuracion", layout, 
            font="Any 18", margins=(150, 100), finalize="TRUE")

configuracion = carga_config()

for key in KEY_CONFIG:
    window[KEY_CONFIG[key]].update(value=configuracion[key])

###falta implementar el tab de dificultad, pero no se me ocurre como

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Cancel"):
        break
    if event == "Save":
        guarda_config(configuracion, values)
        break

window.close()
