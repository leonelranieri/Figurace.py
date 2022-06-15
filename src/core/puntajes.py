import csv, os
import PySimpleGUI as sg
from promedios_con_pandas import ordenar_datos as ordenar

archivo_tabla = os.path.join(
                            os.getcwd(), "src", "core", "data",
                                            "tabla_puntajes.csv")

def cargar_tabla():
    """
        carga la tabla de puntajes si es que existe
        sino, manda a crear el archivo con los cabezales
    """
    try:
        with open(archivo_tabla, "r", encoding="utf-8") as data_set:
            reader = csv.reader(data_set,delimiter=",")
            reader.__next__()
            archivo = list(reader)
    except FileNotFoundError:
            guardar_tabla(None)
            archivo = []
    return archivo

def guardar_tabla(valores):
    """
        crea una tabla con los headers.
        guarda la lista con los puntajes ordenada por mayor puntuacion.
    """
    with open(archivo_tabla, "w", encoding="utf-8",newline='') as salida:
        writer = csv.writer(salida,delimiter=",")
        writer.writerow(["puntaje", "usuario", "dificultad"])
        if valores: 
             valores.sort(key=lambda elem :
                            int(elem[0]), reverse=True)           
             for elem in valores:
                 if elem:
                     writer.writerow(elem)

def agregar_alatabla(puntos, usuario, dificultad):
    """
        se le pasa el ultimo resultado del juego
        lo agrega a la tabla y luego limpia para que queden 20 en su dificultad
    """
    listabla = cargar_tabla()
    listabla.append([puntos, usuario, dificultad])
    # Genero una lista con los puntajes de la dificultad, para luego confirmar que no pasen de 20
    actualizo = list(filter(lambda elem:
                                elem[2] == dificultad, listabla))
    if len(actualizo) > 20:
        # Deja ultimo de la lista al elemento con menor puntaje de la dificultad entrante
        listabla.sort(key=lambda elem: 
                        (elem[2] != dificultad, int(elem[0])),
                            reverse=True)
        listabla.pop()
    guardar_tabla(listabla)

def cargar_data(dificultad):
    """
        separa los datos de la dificultad pasada y agrega el valor de posicion.
        pasa los datos limpios para mostrar en pantalla.
    """
    datos_crudos = list(filter(lambda elem: elem[2] == dificultad, 
                                            cargar_tabla()))
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
    """
    ---------------ORIGINAL-----------------
    cabezal = ("Pos.", "Puntaje", "Usuario", "Dificultad")
    data = []
    layout = [
            [sg.Table(values=data,
                    headings=cabezal,
                    justification="right",
                    num_rows=20,
                    key="-TABLA-",
                    )],
            [sg.Button("Salir"),
                sg.Button("facil"),
                sg.Button("normal"),
                sg.Button("dificil")
            ]
    ]"""

    cabezal_puntaje = ("Pos", "Puntaje", "Usuario")
    cabezal_promedio = ("Pos", "Promedio", "Usuario")
    data = []
    layout = [
            [sg.Table(values=data,headings=cabezal_puntaje,key="-TABLA-PUNTAJE-"), sg.Table(values=data,
                    headings=cabezal_promedio, key="-TABLA-PROMEDIO-")],
            [sg.Button("Salir"),
                sg.Button("facil"),
                sg.Button("normal"),
                sg.Button("dificil")
            ]
    ]

    window = sg.Window("tabla", layout,
                        font="Any 18", margins=(100, 50))

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Salir"):
            break
        elif event == "facil":
            window["-TABLA-PUNTAJE-"].update(cargar_data("facil"))
            window["-TABLA-PROMEDIO-"].update(ordenar('facil'))
        elif event == "normal":
            window["-TABLA-PUNTAJE-"].update(cargar_data("normal"))
            window["-TABLA-PROMEDIO-"].update(ordenar('normal'))
        elif event == "dificil":
            window["-TABLA-PUNTAJE-"].update(cargar_data("dificil"))
            window["-TABLA-PROMEDIO-"].update(ordenar('dificil'))

    window.close()
