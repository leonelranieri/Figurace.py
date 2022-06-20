import os
import random
import PySimpleGUI as sg

def acumular_puntos(diccionario, ayuda, dificultad):
    total = 0
    if dificultad == "normal":
        ayuda = ayuda + 1
    elif dificultad == "dificil":
        ayuda = ayuda + 2
    for elem in diccionario.values():
            total = total + elem
    return total - ayuda

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
    mins = t // 60
    secs = t % 60
    timer = '{:02d}:{:02d}'.format(mins, secs) # {:02d} sintaxis de formato para 00 minutos : 00 segundos

    dif_frame_layout = [
        [sg.Text('Dificultad: '+ dificultad.upper())],
        [sg.Text('Cantidad de Rondas: '+ str(nivel['rondas']))],
        [sg.Text('Tiempo Restante: '+ timer, key = '-TIMER-')],
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
        [sg.Multiline(respuestas, size=(80,20), disabled = True, background_color = "#65778d",
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

    boton1 = botones[0]
    boton2 = botones[1]
    boton3 = botones[2]
    boton4 = botones[3]
    boton5 = botones[4]

    opciones_frame_layout = [
        [sg.Text('características: '.upper())], 
        [sg.Text(mostrar_caracteristicas(filas_dataset, lista_seleccionada, cant_caracteristicas), 
                key='-OPTIONS-')],
        [sg.Text('Característica a Adivinar: '  + caracteristica_a_adivinar)],
        [sg.Button(boton1, key='-INPUT1-')],
        [sg.Button(boton2, key='-INPUT2-')],
        [sg.Button(boton3, key='-INPUT3-')],
        [sg.Button(boton4, key='-INPUT4-')],
        [sg.Button(boton5, key='-INPUT5-')],
        [sg.Button('OK'), sg.Button('PASAR >'), sg.Button('AYUDA', key="-AYUDA-")]#agrego ayuda
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
        sg.Frame('', pantalla_categoria, font='Any 12', title_color='white', size=(350,150)), 
        sg.Frame('', pantalla_dificultad, font='Any 12', title_color='white', size=(350,150))
        ],
        # row 2:
        [
        sg.Frame('', pantalla_respuestas, font='Any 12', title_color='white', size=(350,400)),
        sg.Frame('', pantalla_opciones, font='Any 12', title_color='white', size=(350,400))
        ]
    ]

    window = sg.Window("Pantalla de Juego", layout, margins=(90,60))
    return window

