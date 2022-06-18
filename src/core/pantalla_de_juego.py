import os
import csv
import random

import PySimpleGUI as sg
from puntajes import agregar_alatabla
import configuracion as config
import funciones_pantalla_juego as fp
import jugadores

def main(dificultad, nombre_usuario): 
    archivos_categorias = [
        "peliculas_figurace.csv",
        "lagos_pandas.csv",
        "artistas_pandas.csv"
    ]

    perfiles = jugadores.apertura_de_archivo()
    configuracion = config.carga_config()

    # Randomiza un dataset:
    categoria = random.choice(archivos_categorias)
    nombre_categoria = fp.get_nombre_categoria(categoria)

    # Nombre de Usuario:
    nombre = nombre_usuario[1]

    # ------------------------------------- [RUTAS] -------------------------------------

    # Ruta Archivo:
    ruta_archivo = os.path.join(os.getcwd(), "src", "core", "folder_csv", categoria)
    # Ruta Imagen:
    ruta_imagen = fp.get_ruta_imagen(categoria)
    # Carga de configuración:
    nivel_de_dificultad ={}
    nivel_de_dificultad = configuracion[dificultad['-DIFI-']]
    cant_caracteristicas = int(nivel_de_dificultad['cara'])
    sumar_puntos = nivel_de_dificultad['suma']
    restar_puntos = nivel_de_dificultad['resta']

    # Lectura de dataset:
    archivo_cvs = open(ruta_archivo, "r", encoding="UTF-8")
    csvreader = csv.reader(archivo_cvs, delimiter=',')
    filas_de_dataset = []

    for elem in csvreader:
        filas_de_dataset.append(elem)

    # Mostrar "caracteristica a adivinar", "opciones" etc: 
    caracteristica_a_adivinar = str(filas_de_dataset[0][5])
    lista_seleccionada = random.choice(filas_de_dataset) # Seleciona una fila del archivo csv
    respuesta_correcta = (lista_seleccionada[5]) # Seleciona el campo a adivinar de la lista (depende del csv puede cambiar)
    opciones = fp.lista_opciones(filas_de_dataset, respuesta_correcta) # Seleciona posibles respuestas del campo a adivinar del archivo csv y las mezcla con la respuesta correcta

    respuestas = '' 
    total_respuestas = {} # Guarda las respuestas del usuario y los correspondientes puntos de la ronda.

    # ------------------------------------- [VARIABLES PARA LAYOUT VENTANA PRINCIPAL] -------------------------------------

    frame_categoria = fp.crear_layout_categoria(nombre_categoria,ruta_imagen)
    frame_dificultad = fp.crear_layout_dificultad(dificultad['-DIFI-'],nivel_de_dificultad)
    frame_respuestas = fp.crear_layout_respuestas(nombre, respuestas)
    frame_opciones = fp.crear_layout_opciones(opciones, filas_de_dataset,
                     lista_seleccionada,caracteristica_a_adivinar, cant_caracteristicas)

    # ------------------------------------- [PANTALLA PRINCIPAL] -------------------------------------

    main_window = fp.crear_pantalla(frame_categoria,frame_dificultad,frame_respuestas,frame_opciones)

# ------------------------------------- [EVENT LOOP] -------------------------------------
    color_original = '#ff9fd6'
    respuesta_seleccionada = ''
    i = 0

    while True:
        event,value = main_window.read()
    
        if event == sg.WIN_CLOSED or event == "ABANDONAR EL JUEGO":
            break

        # -------------[ SELECTOR DE COLOR DE INPUT ]-------------
        
        elif event == '-INPUT1-':
            respuesta_seleccionada = frame_opciones[3][0].GetText()
            main_window['-INPUT1-'].update(button_color=('black','light blue'))
            main_window['-INPUT2-'].update(button_color=('black', color_original))
            main_window['-INPUT3-'].update(button_color=('black', color_original))
            main_window['-INPUT4-'].update(button_color=('black', color_original))
            main_window['-INPUT5-'].update(button_color=('black', color_original))
        
        elif event == '-INPUT2-':
            respuesta_seleccionada = frame_opciones[4][0].GetText()
            main_window['-INPUT1-'].update(button_color=('black', color_original))
            main_window['-INPUT2-'].update(button_color=('black','light blue'))
            main_window['-INPUT3-'].update(button_color=('black', color_original))
            main_window['-INPUT4-'].update(button_color=('black', color_original))
            main_window['-INPUT5-'].update(button_color=('black', color_original))

        elif event == '-INPUT3-':
            respuesta_seleccionada = frame_opciones[5][0].GetText()
            main_window['-INPUT1-'].update(button_color=('black', color_original))
            main_window['-INPUT2-'].update(button_color=('black', color_original))
            main_window['-INPUT3-'].update(button_color=('black','light blue'))
            main_window['-INPUT4-'].update(button_color=('black', color_original))
            main_window['-INPUT5-'].update(button_color=('black', color_original))

        elif event == '-INPUT4-':
            respuesta_seleccionada = frame_opciones[6][0].GetText()
            main_window['-INPUT1-'].update(button_color=('black', color_original))
            main_window['-INPUT2-'].update(button_color=('black', color_original))
            main_window['-INPUT3-'].update(button_color=('black', color_original))
            main_window['-INPUT4-'].update(button_color=('black','light blue'))
            main_window['-INPUT5-'].update(button_color=('black', color_original))

        elif event == '-INPUT5-':
            respuesta_seleccionada = frame_opciones[7][0].GetText()
            main_window['-INPUT1-'].update(button_color=('black', color_original))
            main_window['-INPUT2-'].update(button_color=('black', color_original))
            main_window['-INPUT3-'].update(button_color=('black', color_original))
            main_window['-INPUT4-'].update(button_color=('black', color_original))
            main_window['-INPUT5-'].update(button_color=('black','light blue'))

        # -------------[ PASAR ]-------------

        elif event == 'PASAR >':
            total_respuestas[i] = int(restar_puntos) * -1
            i += 1 
            linea = (f"PREGUNTA {i} : - {restar_puntos} puntos (Pasó)"+"\n") 
            respuestas = (f"{respuestas} {linea}""\n")
            main_window['-ANSWERS OUTPUT-'].update(respuestas)

            lista = random.choice(filas_de_dataset)
            respuesta_correcta = (lista[5])
            # Actualizo lista de opciones:
            opciones = fp.lista_opciones(filas_de_dataset, respuesta_correcta)
            
            # Fin de ronda
            if len(total_respuestas) == int(nivel_de_dificultad['rondas']):
                agregar_alatabla(fp.acumular_puntos(total_respuestas),
                                    nombre_usuario[1], dificultad["-DIFI-"])
                sg.Popup('Fin de ronda de preguntas. Puntos acumulados en ésta ronda: '
                        + str(fp.acumular_puntos(total_respuestas)),
                        custom_text = ('Volver a Jugar', 'Salir del Juego')
                            , keep_on_top=True)
                if event == 'Salir del Juego':
                    break 
                break
            
            # Actualiza Tarjeta: 
            main_window['-OPTIONS-'].update(fp.mostrar_caracteristicas(filas_de_dataset, lista, cant_caracteristicas))
            # Actualizo Botones:
            lista_botones = fp.asignar_valores_botones(opciones)
            # Actualizo ventana botones:  
            main_window['-INPUT1-'].update(lista_botones[0]) 
            main_window['-INPUT2-'].update(lista_botones[1])
            main_window['-INPUT3-'].update(lista_botones[2])
            main_window['-INPUT4-'].update(lista_botones[3])
            main_window['-INPUT5-'].update(lista_botones[4])
            
        # -------------[ OK ]-------------

        elif event == 'OK':
            if respuesta_seleccionada == respuesta_correcta:
                total_respuestas[i] = int(sumar_puntos)
                i += 1
                linea = (f"PREGUNTA {i}: CORRECTO!: +{sumar_puntos} puntos"+"\n")
                respuestas = (f"{respuestas} {linea}""\n")
                main_window['-ANSWERS OUTPUT-'].update(respuestas)

            else:
                total_respuestas[i] = int(restar_puntos) * -1
                i += 1
                linea = (f"PREGUNTA {i}: INCORRECTO! respuesta correcta:"+"\n"+f"{respuesta_correcta} : -{restar_puntos} puntos"+"\n")
                respuestas = (f"{respuestas} {linea}""\n")
                main_window['-ANSWERS OUTPUT-'].update(respuestas)
                
            lista = random.choice(filas_de_dataset)
            respuesta_correcta = (lista[5])
            opciones = fp.lista_opciones(filas_de_dataset, respuesta_correcta)

            # Fin de Ronda
            if len(total_respuestas) == int(nivel_de_dificultad['rondas']):
                agregar_alatabla(fp.acumular_puntos(total_respuestas),
                                    nombre_usuario[1], dificultad["-DIFI-"])
                sg.Popup('Fin de ronda de preguntas. Puntos acumulados en ésta ronda: '+str(fp.acumular_puntos(total_respuestas)),
                        custom_text = ('Volver a Jugar', 'Salir del Juego'), keep_on_top=True)
                if event == 'Salir del Juego':
                    break 
                break
            
            # Actualiza Tarjeta: 
            main_window['-OPTIONS-'].update(fp.mostrar_caracteristicas(filas_de_dataset, lista, cant_caracteristicas)) 
            # Actualizo Botones:
            lista_botones = fp.asignar_valores_botones(opciones)
            # Actualizo ventana botones:  
            main_window['-INPUT1-'].update(lista_botones[0]) 
            main_window['-INPUT2-'].update(lista_botones[1])
            main_window['-INPUT3-'].update(lista_botones[2])
            main_window['-INPUT4-'].update(lista_botones[3])
            main_window['-INPUT5-'].update(lista_botones[4])

        # -------------[ ABANDONAR JUEGO ]-------------
        if (event == '-ABANDONAR-') and sg.Popup('¿Desea Abandonar el Juego?', 
                                    custom_text = ('Abandonar', 'Continuar Jugando'), 
                                        keep_on_top=True) == 'Abandonar':
            main_window.close()
            #agregar_alatabla(fp.acumular_puntos(total_respuestas),
            #                nombre_usuario[1], dificultad["-DIFI-"])

    main_window.close()

#---------------------------------------------------------