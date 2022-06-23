import os
from pickle import TRUE
import PySimpleGUI as sg
from promedios_con_pandas import ordenar_datos as ordenar
import pandas as pd

archivo_tabla = os.path.join(
                            os.getcwd(), "src", "core", "data",
                                            "tabla_puntajes.csv")

def cargar_tabla():
    """
        carga la tabla de puntajes si es que existe
        sino, manda a crear el archivo con los cabezales
    """
    try:
        data_frame = pd.read_csv(archivo_tabla, encoding='utf-8')
    except FileNotFoundError:
        data_frame = pd.DataFrame(columns=
                    ("puntaje", "usuario", "dificultad")
                )
        guardar_tabla(data_frame)

    return data_frame

def guardar_tabla(valores):
    """
        crea una tabla con los headers.
        guarda la lista con los puntajes ordenada por mayor puntuacion.
    """
    if not valores.empty:
        valores.to_csv(archivo_tabla, index=False)
    else:
        data_frame = pd.DataFrame(columns=("puntaje", "usuario", "dificultad"))
        data_frame.to_csv(archivo_tabla, index=False)

def agregar_alatabla(puntos, usuario, dificultad):
    """
        se le pasa el ultimo resultado del juego
        lo agrega a la tabla y luego limpia para que queden 20 en su dificultad
    """
    listabla = cargar_tabla()
    nueva_data = pd.DataFrame(data=[[puntos, usuario, dificultad]],
                        columns=["puntaje", "usuario", "dificultad"]
                    )
    listabla = pd.concat([listabla, nueva_data], ignore_index=True)
    listabla = listabla.convert_dtypes()
    listabla.sort_values(by=["dificultad", "puntaje"],
                            ascending=False, inplace=True)

    guardar_tabla(listabla)

def cargar_data(dificultad):
    """
        separa los datos de la dificultad pasada y agrega el valor de posicion.
        pasa los datos limpios para mostrar en pantalla.
    """
    df = cargar_tabla()
    datos_crudos = df.loc[df["dificultad"] == dificultad,
                                ["puntaje", "usuario"]].head(20)
    datos_crudos = datos_crudos.values.tolist()
    mostrante = []
    for i, elem in enumerate(datos_crudos, start=1):
        pivot = [i]
        pivot.extend(elem)
        mostrante.append(pivot)
    
    return mostrante

def mostrar_tabla():
    """
        crea una tabla vacia hasta que se elija en que dificultad se quieren ver los puntos
        y luego se muestran los susodichos
        al menos eso entendi del enunciado
    """

    cabezal_puntaje = ("Pos", "Puntaje", "Usuario")
    cabezal_promedio = ("Pos", "Promedio", "Usuario")
    data = []
    layout = [
            [sg.Text("Dificultad mostrante: "), sg.Text(key=("-TRUCHO-"))],
            [sg.Table(values=data,headings=cabezal_puntaje,key="-TABLA-PUNTAJE-")
                , sg.Table(values=data,
                    headings=cabezal_promedio, key="-TABLA-PROMEDIO-")],
            [sg.Button("Salir"),
                sg.Button("facil"),
                sg.Button("normal"),
                sg.Button("dificil")
            ]
    ]

    window = sg.Window("Tabla", layout,
                        font="Any 18", margins=(100, 50),finalize=TRUE)
    window["-TABLA-PUNTAJE-"].update(cargar_data("facil"))
    window["-TABLA-PROMEDIO-"].update(ordenar('facil'))
    window["-TRUCHO-"].update("Facil")

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Salir"):
            break
        elif event == "facil":
            window["-TABLA-PUNTAJE-"].update(cargar_data("facil"))
            window["-TABLA-PROMEDIO-"].update(ordenar('facil'))
            window["-TRUCHO-"].update("Facil")
        elif event == "normal":
            window["-TABLA-PUNTAJE-"].update(cargar_data("normal"))
            window["-TABLA-PROMEDIO-"].update(ordenar('normal'))
            window["-TRUCHO-"].update("Normal")
        elif event == "dificil":
            window["-TABLA-PUNTAJE-"].update(cargar_data("dificil"))
            window["-TABLA-PROMEDIO-"].update(ordenar('dificil'))
            window["-TRUCHO-"].update("Dificil")
    window.close()
