import os
import csv
import random
import uuid

import time
import PySimpleGUI as sg
from puntajes import agregar_alatabla
import configuracion as config
import funciones_pantalla_juego as fp
import jugadores

def main(dificultad, nombre_usuario, con_ayuda): 
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
    my_uuid = uuid.uuid4()

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
    csvreader = list(csv.reader(archivo_cvs, delimiter=','))
    filas_de_dataset = []

    for elem in csvreader:
        filas_de_dataset.append(elem)

    # Mostrar "caracteristica a adivinar", "opciones" etc: 
    caracteristica_a_adivinar = str(filas_de_dataset[0][5])
    lista_seleccionada = random.choice(filas_de_dataset) # Seleciona una fila del archivo csv
    respuesta_correcta = (lista_seleccionada[5]) # Seleciona el campo a adivinar de la lista (depende del csv puede cambiar)
    opciones = fp.lista_opciones(filas_de_dataset, respuesta_correcta) # Seleciona posibles respuestas del campo a adivinar del archivo csv y las mezcla con la respuesta correcta
    ayudas = opciones.copy()

    respuestas = '' 
    total_respuestas = {} # Guarda las respuestas del usuario y los correspondientes puntos de la ronda.

    #Lista de datos de la partida actual:
    partida_actual = []

    # ------------------------------------- [VARIABLES PARA LAYOUT VENTANA PRINCIPAL] -------------------------------------
    frame_categoria = fp.crear_layout_categoria(nombre_categoria,ruta_imagen)
    frame_dificultad = fp.crear_layout_dificultad(dificultad['-DIFI-'],nivel_de_dificultad)
    frame_respuestas = fp.crear_layout_respuestas(nombre, respuestas)
    if con_ayuda:
        frame_opciones = fp.crear_layout_opciones(opciones, filas_de_dataset,
                lista_seleccionada,caracteristica_a_adivinar, cant_caracteristicas)
    else:
        frame_opciones = fp.crear_layout_opciones_sin_ayuda(opciones, filas_de_dataset,
                lista_seleccionada,caracteristica_a_adivinar, cant_caracteristicas)

# ------------------------------------- [PANTALLA PRINCIPAL] -------------------------------------
    main_window = fp.crear_pantalla(frame_categoria,frame_dificultad,frame_respuestas,frame_opciones)
# ------------------------------------- [EVENT LOOP] -------------------------------------
    color_original = '#ff9fd6'
    respuesta_seleccionada = ''
    i = 0
    ayuda = 0
    partida_actual.append({'timestamp' : time.time(), 'id' : my_uuid, 'evento' : "inicio_partida", 'usuarie' : nombre, 'estado' : " ", 'texto_ingresado' : " ", 'respuesta' : " ", 'nivel' : dificultad['-DIFI-']})
    correcta = False
    correcta_anterior = ""

    while True:
        event,value = main_window.read()

        if event == sg.WIN_CLOSED or event == "ABANDONAR EL JUEGO":
            break
        
        if event == '-START-':
            tiempo_inicial = time.time()
            tiempo_por_ronda = int(nivel_de_dificultad['tiempo'])
            tiempo_transcurrido = float(time.time() - tiempo_inicial)
            tiempo_restante = (int(nivel_de_dificultad['tiempo'])- tiempo_transcurrido)
            tiempo_jugado = 0
            #Mostrar caracteristicas y opciones
            main_window['-OPTIONS-'].update(visible=True)
            main_window['-INPUT1-'].update(visible=True)
            main_window['-INPUT2-'].update(visible=True)
            main_window['-INPUT3-'].update(visible=True)
            main_window['-INPUT4-'].update(visible=True)
            main_window['-INPUT5-'].update(visible=True)

            while True:
                event,value = main_window.read(timeout=100)

                if event == sg.WIN_CLOSED or event == "ABANDONAR EL JUEGO":
                    break
            # -------------[ SELECTOR DE COLOR DE INPUT ]-------------
            
                if event == '-INPUT1-':
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
                    correcta_anterior = respuesta_correcta

                    lista = random.choice(filas_de_dataset)
                    respuesta_correcta = (lista[5])
                    # Actualizo lista de opciones:
                    opciones = fp.lista_opciones(filas_de_dataset, respuesta_correcta)
                    ayudas = opciones.copy()
                    # Fin de ronda
                    #print(con_ayuda)
                    if len(total_respuestas) == int(nivel_de_dificultad['rondas']):
                        agregar_alatabla(fp.acumular_puntos(total_respuestas, ayuda, dificultad["-DIFI-"], con_ayuda),
                                            nombre_usuario[1], dificultad["-DIFI-"]) 
                        partida_actual.append(fp.lamascara(my_uuid,event,nombre,correcta,respuesta_seleccionada,correcta_anterior,dificultad["-DIFI-"]))
                        partida_actual.append(fp.lamascara(my_uuid,"Salir del juego",nombre,correcta,respuesta_seleccionada,correcta_anterior,dificultad["-DIFI-"]))
                        sg.Popup('Fin de ronda de preguntas. Puntos acumulados en ésta ronda: '
                                + str(fp.acumular_puntos(total_respuestas, ayuda, dificultad["-DIFI-"], con_ayuda)),
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
                    #main_window['-AYUDA-'].update(lista_botones)
                    ayudas = lista_botones.copy()
                    #actualiza Temporizador
                    tiempo_jugado = tiempo_jugado + tiempo_transcurrido
                    tiempo_inicial = time.time()
                    main_window['-COUNTDOWN-'].update(F'Quedan: {fp.actualizar_temporizador(tiempo_por_ronda, tiempo_inicial)} segundos')

                # -------------[ AYUDA ]------------
                if event == "-AYUDA-":  #agrego ayuda
                    layout = [
                        [sg.T("¿DESEA CONTINUAR?")],   
                        [sg.Button("Si", key="-SI-")], 
                        [sg.Button("No", key="-NO-")]
                    ]
                    ventana = sg.Window("ventana de ayuda", layout, margins=(60,60))
                    
                    while True:
                        event, values = ventana.read()
                        
                        if event == "-NO-" or event == sg.WIN_CLOSED:
                            break
                        elif event == "-SI-":
                            try:
                                opcion = random.randrange(5)
                                if respuesta_correcta in ayudas:
                                    indice_correcta = ayudas.index(respuesta_correcta)
                                    ayudas.pop(indice_correcta)
                                    if ayuda < 2:
                                        try:
                                            ayuda = ayuda + 1 
                                            sg.PopupOK(f"SE MOSTRARA UNA DE LAS\n" 
                                                    " OPCIONES INCORRECTAS", {ayudas[opcion]},
                                                    "SE LE DESCONTARA", {ayuda}, "PUNTO MÁS EL ADICIONAL POR DIFICULTAD.")
                                        except IndexError:
                                            pass
                                    else:
                                        sg.PopupQuickMessage("SE QUEDO SIN AYUDAS")
                            except ValueError:     
                                pass   
                        break
                    ventana.close()
                # -------------[ OK ]-------------

                elif event == 'OK':
                    if respuesta_seleccionada == respuesta_correcta:
                        total_respuestas[i] = int(sumar_puntos)
                        i += 1
                        linea = (f"PREGUNTA {i}: CORRECTO!: +{sumar_puntos} puntos"+"\n")
                        respuestas = (f"{respuestas} {linea}""\n")
                        main_window['-ANSWERS OUTPUT-'].update(respuestas)
                        correcta = True

                    else:
                        total_respuestas[i] = int(restar_puntos) * -1
                        i += 1
                        linea = (f"PREGUNTA {i}: INCORRECTO! respuesta correcta:"+"\n"+f"{respuesta_correcta} : -{restar_puntos} puntos"+"\n")
                        respuestas = (f"{respuestas} {linea}""\n")
                        main_window['-ANSWERS OUTPUT-'].update(respuestas)
                        correcta = False

                    correcta_anterior = respuesta_correcta    
                    lista = random.choice(filas_de_dataset)
                    respuesta_correcta = (lista[5])
                    opciones = fp.lista_opciones(filas_de_dataset, respuesta_correcta)
                    ayudas = opciones.copy()

                    # Fin de Ronda
                    if len(total_respuestas) == int(nivel_de_dificultad['rondas']):
                        agregar_alatabla(fp.acumular_puntos(total_respuestas, ayuda, dificultad["-DIFI-"], con_ayuda),#agrego ayuda
                                            nombre_usuario[1], dificultad["-DIFI-"])
                        partida_actual.append(fp.lamascara(my_uuid,event,nombre,correcta,respuesta_seleccionada,correcta_anterior,dificultad["-DIFI-"]))
                        partida_actual.append(fp.lamascara(my_uuid,"Salir del juego",nombre,correcta,respuesta_seleccionada,correcta_anterior,dificultad["-DIFI-"]))
                        sg.Popup('Fin de ronda de preguntas. Puntos acumulados en ésta ronda: '+str(fp.acumular_puntos(total_respuestas, ayuda, dificultad["-DIFI-"], con_ayuda)),
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
                    ayudas = lista_botones.copy()
                    #actualiza Temporizador
                    tiempo_jugado = tiempo_jugado + tiempo_transcurrido
                    tiempo_inicial = time.time()
                    main_window['-COUNTDOWN-'].update(F'Quedan: {fp.actualizar_temporizador(tiempo_por_ronda, tiempo_inicial)} segundos')

                # -------------[ ABANDONAR JUEGO ]-------------
                if (event == '-ABANDONAR-') and sg.Popup('¿Desea Abandonar el Juego?', 
                                            custom_text = ('Abandonar', 'Continuar Jugando'), 
                                                keep_on_top=True) == 'Abandonar':
                    main_window.close()
                # --------------------------------------------[ TIEMPO AGOTADO ]--------------------------------------

                if (tiempo_restante == 0) and len(total_respuestas) != int(nivel_de_dificultad['rondas']):
                    total_respuestas[i] = int(restar_puntos)
                    i += 1 
                    linea = (f"PREGUNTA {i} : - {restar_puntos} puntos (Pasó)"+"\n")
                    respuestas = (f"{respuestas} {linea}""\n")
                    main_window['-ANSWERS OUTPUT-'].update(respuestas)

                    correcta_anterior = respuesta_correcta
                    lista = random.choice(filas_de_dataset)
                    respuesta_correcta = (lista[5])
                    # Actualizo lista de opciones:
                    opciones = fp.lista_opciones(filas_de_dataset, respuesta_correcta)

                    tiempo_inicial = time.time()
                    lista = random.choice(filas_de_dataset)
                    respuesta_correcta = (lista[5])
                    opciones = fp.lista_opciones(filas_de_dataset, respuesta_correcta)

                    main_window['-OPTIONS-'].update(fp.mostrar_caracteristicas(filas_de_dataset, lista, cant_caracteristicas))
                    
                    # Actualizo Botones:
                    lista_botones = fp.asignar_valores_botones(opciones)
                    # Actualizo ventana botones:  
                    main_window['-INPUT1-'].update(lista_botones[0]) 
                    main_window['-INPUT2-'].update(lista_botones[1])
                    main_window['-INPUT3-'].update(lista_botones[2])
                    main_window['-INPUT4-'].update(lista_botones[3])
                    main_window['-INPUT5-'].update(lista_botones[4])
                    #Actualizo el Countdown:
                    tiempo_jugado = tiempo_jugado + tiempo_transcurrido
                    main_window['-COUNTDOWN-'].update(F'Quedan: {fp.actualizar_temporizador(tiempo_por_ronda, tiempo_inicial)} segundos')
                    partida_actual.append(fp.lamascara(my_uuid,event,nombre,correcta,respuesta_seleccionada,correcta_anterior,dificultad["-DIFI-"]))
            
                # -----------------------------------------[ ACTUALIZAR TIEMPO ]----------------------------------------
                tiempo_transcurrido = int(time.time() - tiempo_inicial)
                tiempo_restante = (int(nivel_de_dificultad['tiempo'])- tiempo_transcurrido)
                main_window['-COUNTDOWN-'].update(F'Quedan: {tiempo_restante} segundos')
                if event != "__TIMEOUT__":
                    if not event in ["-INPUT1-", "-INPUT2-", "-INPUT3-", "-INPUT4-", "-INPUT5-"]:
                        partida_actual.append(fp.lamascara(my_uuid,event,nombre,correcta,respuesta_seleccionada,correcta_anterior,dificultad["-DIFI-"]))
            
            fp.generar_datos_partida(partida_actual)      
            main_window.close()

#---------------------------------------------------------

