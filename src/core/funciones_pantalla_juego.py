import os
import random
import time
import PySimpleGUI as sg
import pandas as pd

def acumular_puntos(diccionario, restar, dificultad, con_ayuda):
    total = 0
    if con_ayuda:
        """if dificultad == "normal":
            ayuda = ayuda + 1
        elif dificultad == "dificil":
            ayuda = ayuda + 2"""
        for elem in diccionario.values():
            total = total + elem
        total = total - restar
    else:
        for elem in diccionario.values():
            total = total + elem
    
    return total

def limpiar_cadena(cadena):
    """ Devuelve una cadena de texto sin guiones bajos """
    return cadena.replace('_', ' ').lower()

def mostrar_caracteristicas(filas_de_dataset, lista_seleccionada, cant_caracteristicas):
    """ 
        Devuelve una cadena de String con las caracteristicas que debe mostrar en
        pantalla para el usuario.

        :param filas_de_dataset: Listas de cada lista (Fila) del Dataset
        :type filas_de_dataset: List

        :param lista_seleccionada: Listas Elegida del Dataset
        :type filas_de_dataset: List

        :param cant_caracteristicas: Cantidad de carateristicas a mostrar.
        :type cant_caracteristicas: int

        :returns: String
    """
    cadena = ''
    for i,elem in enumerate(filas_de_dataset[0]):
        if  i < cant_caracteristicas:
            cadena = cadena + elem + ": "
            cadena = cadena + lista_seleccionada[i] + "\n" 
            cadena = limpiar_cadena(cadena)
    return cadena

def lista_opciones(filas_de_dataset, respuesta_correcta):
    """
       crea una lista de opciones (falsas) apartir de las filas de un dataset y reemplaza uno de 
       esos valores con la respuesta correcta en una posición random. 

       :param filas_de_dataset: Listas de cada lista (Fila) del Dataset
       :type filas_de_dataset: List

       :param respuesta_correcta: Respuesta que debe ser adivinada y mezclada entre las opciones
       :type respuesta_correcta: String

       returns: List
    """
    lista = []
    
    for i in range(5):
        lista_random = random.choice(filas_de_dataset)
        lista.append(lista_random[5])

    lista[random.randrange(5)] = respuesta_correcta # Pisa un valor de la lista con la respuesta correcta

    return lista

def get_ruta_imagen(categoria):
    """
        Genera una ruta apartir de un string pasado por parámetro

        :param categoria: nombre de la categoria en base a la que debe buscar la imagen
        :type categoria: String

        returns: os path
    """

    if categoria == "peliculas_figurace.csv" :
        try:
            ruta_imagen = os.path.join(os.getcwd(), "src", "core", "images", "categoria peliculas.png")
        except FileNotFoundError:
            sg.Popup("Archivo 'categoria peliculas.png' no encontrado")
    elif categoria == "lagos_pandas.csv":
        try:
            ruta_imagen = os.path.join(os.getcwd(), "src", "core", "images", "categoria lagos.png")
        except FileNotFoundError:
            sg.Popup("Archivo 'categoria lagos.png' no encontrado")
    else:
        try:
            ruta_imagen = os.path.join(os.getcwd(), "src", "core", "images", "categoria spotify.png")
        except FileNotFoundError:
            sg.Popup("Archivo 'categoria spotify.png' no encontrado")
    return ruta_imagen

def get_nombre_categoria (categoria):
    """
        devuelve un string con el nombre de una categoria para mostrarse en
        el layout de la ventana del juego.

        :param categoria: nombre de la categoria 
        :type categoria: String

        returns: string
    """
    if categoria == "peliculas_figurace.csv" :
        nombre_categoria = "Películas"   
    elif categoria == "lagos_pandas.csv":
        nombre_categoria = "Lagos" 
    else: nombre_categoria = "spotify" 

    return nombre_categoria

def asignar_valores_botones(opciones):
    """
        Asigna desde una lista de opciones el string que debe mostrar
        cada botón desde los cuales el usuario elegirá su respuesta.
        Una vez tomada una opcion (de forma random) dicha opcion se eliminará
        de la lista para evitar que aparezcan opciones repetidas en los botones.

        :param opciones: lista de strings
        :type opciones: list

        returns: List
    """
    botones = []

    boton1 = random.choice(opciones)
    opciones.remove(boton1)  
    botones.append(boton1)

    boton2 = random.choice(opciones)
    opciones.remove(boton2)  
    botones.append(boton2)

    boton3 = random.choice(opciones)
    opciones.remove(boton3)  
    botones.append(boton3)

    boton4 = random.choice(opciones)
    opciones.remove(boton4)  
    botones.append(boton4)

    boton5 = random.choice(opciones)
    opciones.remove(boton5)  
    botones.append(boton5)

    return botones

def actualizar_botones(main_window, botones):
    """
        actualiza los botones en la ventana principal con las opciones cargadas en una lista
        botones = lista

        :param main_window: Ventana principal del modulo "pantalla_de_juego" a actualizar
        :type opciones: PySimpleGui Window

        :param botones: lista de strings
        :type botones: list

        returns: PySimpleGui Window
    """

    main_window['-INPUT1-'].update(botones[0]) 
    main_window['-INPUT2-'].update(botones[1])
    main_window['-INPUT3-'].update(botones[2])
    main_window['-INPUT4-'].update(botones[3])
    main_window['-INPUT5-'].update(botones[4]) 

    return main_window

"""
Ésta función será implementada para reemplazar los bloques de código
de -[ SELECTOR DE COLOR DE INPUT ]- en la pantalla principal del juego.
"""
"""
def color_selector(evento, color_original):
    
    colores = {}
    if evento == '-INPUT1-':
        colores = {0:[color_original,'light blue'],
                   1:['white', color_original],
                   2:['white', color_original],
                   3:['white', color_original],
                   4:['white', color_original]
        }

    elif evento == '-INPUT2-':
        colores = {0:['white', color_original],
                   1:[color_original,'light blue'],
                   2:['white', color_original],
                   3:['white', color_original],
                   4:['white', color_original]
        }

    elif evento == '-INPUT3-':
        colores = {0:['white', color_original],
                   1:['white', color_original],
                   2:[color_original,'light blue'],
                   3:['white', color_original],
                   4:['white', color_original]
        }
        
    elif evento == '-INPUT4-':
        colores = {0:['white', color_original],
                    1:['white', color_original],
                    2:['white', color_original],
                    3:[color_original,'light blue'],
                    4:['white', color_original]
        }

    elif evento == '-INPUT5-':
        colores = {0:['white', color_original],
                   1:['white', color_original],
                   2:['white', color_original],
                   3:['white', color_original],
                   4:[color_original,'light blue']
        }

    return colores
"""
# ------------------------------------- [FRAME LAYOUTS] -------------------------------------

# ------------------------------------- [CATEGORIA] -------------------------------------
def crear_layout_categoria(nombre_categoria, ruta_imagen):
    """
       crea el frame que muestra categoria e imagen de dicha categoria que se 
       usará en el layout de la pantalla principal del juego 

       :param nombre_categoria: string con el nombre de la categoria
       :type nombre_categoria: string

       :param ruta_imagen: lista de strings
       :type ruta_imagen: os path

       returns: List
    """
    cat_frame_layout = [
        [sg.Text('Categoría: '+ nombre_categoria.upper())],
        [sg.Image(ruta_imagen, size = (350,170))]
    ]
    return cat_frame_layout

# ------------------------------------- [DIFICULTAD] -------------------------------------
def crear_layout_dificultad(dificultad, nivel):
    """
       crea el frame que muestra el nivel de dificultad y el tiempo restante para responder que se
       usará en el layout de la pantalla principal del juego 
       
       :param dificultad: clave de diccionario donde se almacenan los parámetro de dificultad
       :type nivel: string

       :param nivel: parámetros del nivel de dificultad del cual se toma la cantidad de rondas a jugar
       :type nivel: diccionario 

       :returns: list
    """
    t = int(nivel['tiempo'])

    """
    mins = t // 60
    secs = t % 60
    timer = '{:02d}:{:02d}'.format(mins, secs) # {:02d} sintaxis de formato para 00 minutos : 00 segundos
    """ 
    dif_frame_layout = [
        [sg.Text('Dificultad: '+ dificultad.upper())],
        [sg.Text('Cantidad de Rondas: '+ str(nivel['rondas']))],
        [sg.Text('', key = '-COUNTDOWN-')],
        [sg.Button('COMENZAR', key = '-START-')]
    ]
    return dif_frame_layout

# ------------------------------------- [RESPUESTAS] -------------------------------------
def crear_layout_respuestas(nombre_usuario, respuestas):
    """
        crea el frame que muestra que respuestas fueron respondidas correctamente y cuales no
        junto con los correspondientes puntos acumulados a usarse en el layout de la pantalla
        principal del juego.

        :param nombre_usuario: es el nombre de usuario (¡menos mal que lo aclaramos!) 
        :type nombre_usuario: string

        :param respuestas: es una concatenación de string que luego se mostrará en pantalla
                           si la respuesta seleccionada fué correcta o nó (en caso de no serlo
                           se concatena también cual era la respuesta correcta) y los puntos
                           ganados o restados según corresponda.
        :type respuestas: string

        :returns: list
    """
    respuestas_frame_layout = [
        [sg.Text('usuario: '+ nombre_usuario.upper())],
        [sg.Multiline(respuestas, size=(80,18), disabled = True, background_color = "#65778d",
        text_color = 'white', key = '-ANSWERS OUTPUT-' )],
        [sg.Button('ABANDONAR JUEGO', key = '-ABANDONAR-')]
    ] 
    return respuestas_frame_layout

# ------------------------------------- [OPCIONES] -------------------------------------
def crear_layout_opciones(opciones, filas_dataset, lista_seleccionada, caracteristica_a_adivinar, cant_caracteristicas):
    """
        crea el frame donde frame donde aparecerán las caracteristicas que servirán como pista para el usuario
        y las opciones disponibes en los botones.

        :param filas_de_dataset: Listas de cada lista (Fila) del Dataset
        :type filas_de_dataset: List

        :param lista_seleccionada: Listas Elegida del Dataset
        :type filas_de_dataset: List

        :param caracteristica_a_adivinar: string a adivinar por el usuario
        :type caracteristica_a_adivinar: string

        :param cant_caracteristicas: Cantidad de carateristicas a mostrar.
        :type cant_caracteristicas: int

        :returns: List
    """
    botones = asignar_valores_botones(opciones)

    opciones_frame_layout = [
        [sg.Text('características: '.upper())], 
        [sg.Text(mostrar_caracteristicas(filas_dataset, lista_seleccionada, cant_caracteristicas), 
                visible=False, key='-OPTIONS-')],
        [sg.Text('Característica a Adivinar: '  + caracteristica_a_adivinar)],
        [sg.Button(botones[0],visible=False, key='-INPUT1-')],
        [sg.Button(botones[1],visible=False, key='-INPUT2-')],
        [sg.Button(botones[2],visible=False, key='-INPUT3-')],
        [sg.Button(botones[3],visible=False, key='-INPUT4-')],
        [sg.Button(botones[4],visible=False, key='-INPUT5-')],
        [sg.Button('OK'), sg.Button('PASAR >'), sg.Button('AYUDA', key="-AYUDA-")]#agrego ayuda
    ]
    return opciones_frame_layout

def crear_layout_opciones_sin_ayuda(opciones, filas_dataset, lista_seleccionada, caracteristica_a_adivinar, cant_caracteristicas):
    """
        crea el frame donde frame donde aparecerán las caracteristicas que servirán como pista para el usuario
        y las opciones disponibes en los botones.

        :param filas_de_dataset: Listas de cada lista (Fila) del Dataset
        :type filas_de_dataset: List

        :param lista_seleccionada: Listas Elegida del Dataset
        :type filas_de_dataset: List

        :param caracteristica_a_adivinar: string a adivinar por el usuario
        :type caracteristica_a_adivinar: string

        :param cant_caracteristicas: Cantidad de carateristicas a mostrar.
        :type cant_caracteristicas: int

        :returns: List
    """
    botones = asignar_valores_botones(opciones)

    opciones_frame_layout = [
        [sg.Text('características: '.upper())], 
        [sg.Text(mostrar_caracteristicas(filas_dataset, lista_seleccionada, cant_caracteristicas), 
                visible=False, key='-OPTIONS-')],
        [sg.Text('Característica a Adivinar: '  + caracteristica_a_adivinar)],
        [sg.Button(botones[0],visible=False, key='-INPUT1-')],
        [sg.Button(botones[1],visible=False, key='-INPUT2-')],
        [sg.Button(botones[2],visible=False, key='-INPUT3-')],
        [sg.Button(botones[3],visible=False, key='-INPUT4-')],
        [sg.Button(botones[4],visible=False, key='-INPUT5-')],
        [sg.Button('OK'), sg.Button('PASAR >')]#agrego ayuda
        ]
    return opciones_frame_layout
# ------------------------------------- [VENTANA PRINCIPAL DEL JUEGO] -------------------------------------

def crear_pantalla(pantalla_categoria, pantalla_dificultad, pantalla_respuestas, pantalla_opciones):
    """ 
        crea la pantalla principal del juego conformada por 4 frames:
        -tipo de categoria
        -nivel de dificultad
        -puntaje acumulado
        -caracteristicas y opciones selecionables.

        :param pantalla_categoria: Lista de parámetros a mostrar en un PySimpleGui Frame type
        :type pantalla_categoria: List

        :param pantalla_dificultad: Lista de parámetros a mostrar en un PySimpleGui Frame type
        :type pantalla_dificultad: List

        :param pantalla_respuestas: Lista de parámetros a mostrar en un PySimpleGui Frame type
        :type pantalla_respuestas: List

        :param pantalla_opciones: Lista de parámetros a mostrar en un PySimpleGui Frame type
        :type pantalla_opciones: List

        :returns: PysimpleGui Window
    """
    layout = [
        # row 1:
        [
        sg.Frame('', pantalla_categoria, font='Any 12', title_color='white', size=(350,140)), 
        sg.Frame('', pantalla_dificultad, font='Any 12', title_color='white', size=(350,140))
        ],
        # row 2:
        [
        sg.Frame('', pantalla_respuestas, font='Any 12', title_color='white', size=(350,360)),
        sg.Frame('', pantalla_opciones, font='Any 12', title_color='white', size=(350,360))
        ]

    ]

    window = sg.Window("Pantalla de Juego", layout)
    return window

# ------------------------------------- [TEMPORIZADOR] -------------------------------------

def actualizar_temporizador(tiempo_total, tiempo_inicial):
    """
    resetea el temporizador a cero.
    :param tiempo_total: tiempo total de la ronda
    :type tiempo_total: int

    :param tiempo_inicial: valor ortorgado por time.time()
    :type tiempo_inicial: float 
    """
    tiempo_transcurrido = int(time.time() - tiempo_inicial)
    tiempo_restante = (tiempo_total- tiempo_transcurrido)
    return int(tiempo_restante)

# ------------------------------------- [DATOS DE PARTIDA] -------------------------------------
def generador_estado(event, correcta):
    """
       genera evento y estado adecuados para el registro
       correcta es un bool que es true cuando el usuarie respondio bien
    """
    if event == sg.WIN_CLOSED or event == '-ABANDONAR-':
        return ("fin", "abandonada")
    elif event == 'PASAR >':
        return ("intento", "pasa")
    elif event == 'OK':
        return ("intento", "ok" if correcta else "error")
    elif event == 'Salir del juego':
        return ("fin", "finalizada")
    elif event == "__TIMEOUT__":
        return ("intento", "timeout")
    else:
        return ("fin", "timeout")

def lamascara(
            id,
            event, 
            usuarie, 
            ok_error, 
            respuesta_seleccionada, 
            respuesta_correcta, 
            dificultad
        ):
    """
        esta para evitar tanta repeticion de codigo no muy lindo
        adapta los valores de respuesta para que no aparezcan donde no debieran
    """
    evento, estado = generador_estado(event, ok_error)
    if evento == "fin":
        respuesta_correcta = ""
        respuesta_seleccionada = ""
    elif estado == "timeout":
        respuesta_seleccionada = ""
    tiempo = time.time()

    return {'timestamp' : tiempo, 'id' : id, 'evento' : evento,
            'usuarie' : usuarie, 'estado' : estado,
            'texto_ingresado' : respuesta_seleccionada,
            'respuesta' : respuesta_correcta, 'nivel' : dificultad}

def generar_datos_partida(partida_actual):
        """Genera el log de la partidas actuales y proximas para el analisis de los datos"""
        ruta_archivo = os.path.join(os.getcwd(),
                                "src", "core", "data",'log_de_partidas.csv')
        
        field_names = ['timestamp','id','evento','usuarie', 
                        'estado', 'texto_ingresado','respuesta','nivel']
        df_partida = pd.DataFrame(partida_actual,columns=field_names)
        if not os.path.exists(ruta_archivo):
            df_partida.to_csv(ruta_archivo,index=False,encoding='utf-8')
        else:
            df_partida.to_csv(ruta_archivo,index=False,mode="a",
            header=False,encoding='utf-8')      

def confirmar_respuesta(respuesta_seleccionada, respuesta_correcta):
    """
    Devuelve un valor booleando dependiendo si los valores de string pasado por parámetro coinciden o no.
    :param respuesta_seleccionada: variable string almacenada por el evento '-INPUT#-'
    :type respuesta_seleccionada: string

    :param respuesta_correcta: variable string creada en "pantalla_de_juego.py" donde almacena el contenido
                                de la posición 5 (donde se encuentra la respuesta a adivinar) de una lista 
    :type respuesta_correcta: string

    """
    if respuesta_seleccionada == respuesta_correcta:
        return True
    else:
        return False
