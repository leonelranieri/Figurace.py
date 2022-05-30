import PySimpleGUI as sg
import os
from json import (load as jsonload, dump as jsondump)

"""
    pantalla de configuracion del juego
    usa el formato json para guardar y cargar los datos
    
"""

ARCHIVO_CONFIG = os.path.join(os.getcwd(), "src", "core", "data", "config.json")
#represenacion visual del formato de configuracion
DEFAULT_CONFIG = { 
                    "facil" : {
                                "tiempo" : 30, 
                                "rondas" : 5, 
                                "suma" : 3, 
                                "resta" : 1, 
                                "cara" : 5, 
                    },
                    "normal" : {
                                "tiempo" : 15, 
                                "rondas" : 10, 
                                "suma" : 2, 
                                "resta" : 2, 
                                "cara" : 4, 
                    },
                    "dificil" : {
                                "tiempo" : 10, 
                                "rondas" : 25, 
                                "suma" : 1, 
                                "resta" : 3, 
                                "cara" : 3, 
                    }
}
#esto es para pivotear las keys
KEY_CONFIG = {
            "tiempo" : "-TIEMPO-",
            "rondas" : "-RONDAS-", 
            "suma" : "-SUMA-", 
            "resta" : "-RESTA-", 
            "cara" : "-CARACT-", 
}

def carga_config():
    """ 
        si existe un archivo de guardado, lo carga.
        de lo contrario, pasa la configuracion default para que la guarden
    """
    try:
        with open(ARCHIVO_CONFIG, "r") as entrada:
            configuracion = jsonload(entrada)
    except FileNotFoundError:
        configuracion = DEFAULT_CONFIG
        guarda_config(configuracion, None)
    return configuracion

def guarda_config(configuracion, values):
    """ 
        actualiza la configuracion usando values
        a menos que no exista un archivo de configuracion previo
        en tal caso, se guarda la configuracion como llega
    """
    if values:
        for key in KEY_CONFIG:
            configuracion[values["-DIFI-"][0]][key] = values[KEY_CONFIG[key]]
    
    with open(ARCHIVO_CONFIG, "w") as salida:
        jsondump(configuracion, salida)

def crear_ventana(configuracion):
    """
        crea la interfaz para configurar la dificultad
    """

    choices = ("facil", "normal", "dificil")

    layout = [
        [sg.Text("Configuracion", font="Any 25", pad=((10, 0), 30))],
        [sg.Text("seleccionar dificultad"),
                sg.Listbox(choices, size=(15, len(choices)),
                key=("-DIFI-"), enable_events=True)
        ],
        [sg.Text("tiempo limite por ronda", pad=((10, 5), 20)), 
                    sg.OptionMenu(values=("10", "15", "20", "30"), 
                    size=(5, 1), key="-TIEMPO-")
        ],
        [sg.Text("rondas por juego", pad=((10, 5), 20)), 
                    sg.OptionMenu(values=("5", "10", "20", "25"), 
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
        [sg.Text(size=(5, 1))],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]

    # ni idea que es finalize, pero si no lo pongo explota todo
    window = sg.Window("Configuracion", layout, 
            font="Any 18", margins=(100, 50), finalize="TRUE")

    return window

def main():
    """
        la idea es que la ventana sea interactiva
    """
    configuracion = carga_config()
    window = crear_ventana(configuracion)
    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        if event == "Save":
            try:
                guarda_config(configuracion, values)
                window.close()
            except IndexError:
                sg.popup("falta elegir la dificultad a cambiar")
        if values["-DIFI-"]:
            for key in KEY_CONFIG:
                window[KEY_CONFIG[key]].update(configuracion[values["-DIFI-"][0]][key])
            window.refresh()

    window.close()
