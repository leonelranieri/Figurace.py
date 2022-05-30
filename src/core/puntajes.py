import csv, os
import PySimpleGUI as sg

archivo_tabla = os.path.join(os.getcwd(), "src", "core", "data", "tabla_puntajes.csv")

def cargar_tabla():
    """
        carga la tabla de puntajes si es que existe
        sino, manda a crear el archivo con los cabezales
    """
    try:
        with open(archivo_tabla, "r") as data_set:
            reader = csv.reader(data_set,delimiter=",")
            reader.__next__()
            archivo = list(reader)
    except FileNotFoundError:
            guardar_tabla(None)
    
    return archivo

def guardar_tabla(valores):
    """
        crea una tabla con los headers.
        guarda la lista con los puntajes ordenada por mayor puntuacion.
    """
    with open(archivo_tabla, "w") as salida:
        writer = csv.writer(salida,delimiter=",")
        writer.writerow(["puntaje", "usuario", "dificultad"])
        if valores:
            valores.sort(key=lambda elem :
                            int(elem[0]), reverse=True)
            writer.writerows(valores)

def agregar_alatabla(puntos, usuario, dificultad):
    """
        se le pasa el ultimo resultado del juego
        lo agrega a la tabla y luego limpia para que queden 20 en su dificultad
    """
    liston = cargar_tabla()
    liston.append([puntos, usuario, dificultad])
    actualizo = list(filter(lambda elem:
                                elem[2] == dificultad, liston))
    if len(actualizo) > 20:
        liston.sort(key=lambda elem: 
                        (elem[2] != dificultad, int(elem[0])),
                            reverse=True)
        liston.pop()
    guardar_tabla(liston)


def mostrar_tabla():
    """
        crea una tabla vacia hasta que se elija en que dificultad se quieren ver los puntos
        y luego se muestran los susodichos
        al menos eso entendi del enunciado
    """
    cabezal = ("puntaje", "usuario", "dificultad")
    data = []
    layout = [
            [sg.Table(values=data, headings=cabezal,
                justification="right",
                num_rows=20,
                key="-TABLA-",
                )],
            [sg.Button("Salir"), sg.Button("facil"),
                sg.Button("normal"), sg.Button("dificil")]
    ]

    window = sg.Window("tabla", layout,
                        font="Any 18", margins=(100, 50))

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Salir"):
            break
        elif event == "facil":
            window["-TABLA-"].update(list(filter(lambda elem: 
                                elem[2] == "facil", cargar_tabla())
                            ))
        elif event == "normal":
            window["-TABLA-"].update(list(filter(lambda elem: 
                                elem[2] == "normal", cargar_tabla())
                            ))
        elif event == "dificil":
            window["-TABLA-"].update(list(filter(lambda elem: 
                                elem[2] == "dificil", cargar_tabla())
                            ))

    window.close()
