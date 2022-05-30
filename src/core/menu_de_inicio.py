from socket import timeout
import PySimpleGUI as sg
import perfil_de_usuario as perfil
import configuracion as config
import jugadores
import puntajes as tabla_puntajes
import os

def preparar_menu(nombres, dificultad):
    """
    Función que crea y retorna una ventana menú para el juego 
    """
    sg.theme('BrightColors')

    frame_layout = [
                        [sg.T('---Menú---')],
                        [sg.Button("Jugar", key=("-JUGAR-"))],
                        [sg.Button("Configuración", key=("-CONFIGURACION-"))], 
                        [sg.Button("Puntajes", key=("-PUNTAJES-"))],
                        [sg.Button("Perfil", key=("-PERFIL-"))],
                        [sg.Button("Salir", key=("-SALIR-"))],
                        [sg.Combo(nombres, default_value=nombres, s=(13,1)), 
                            sg.Combo(dificultad, default_value=dificultad, s=(13,1), key=("-DIFI-"))]
]

    layout = [[sg.Frame("FIGURACE", frame_layout, font="Any 12", title_color="DarkBlue")]]

    window = sg.Window("MENÚ - FIGURACE -", layout, enable_close_attempted_event=True, margins=(100, 100))
    
    return window

def ventana_de_inicio(perfiles, nivel):    
    """ 
    Inicia la ventana del juego.
    
    Asigna eventos y valores leídos desde la ventana menú. 
    Permite salir del menú o acceder a otras ventanas. Muestra 
    una lista de usuarios y la ultima dificultad elegida  
    """

    #nicks = list(perfiles.keys())
    nicks = [((i + 1), n) for i, n in enumerate(sorted(perfiles.keys()))]
    nombres = ["elija el usuario"] + nicks

    opc = list(nivel.keys())
    #opc = list(config.DEFAULT_CONFIG.keys())    
    dificultad = ["elija la dificultad"] + opc     
    window = preparar_menu(nombres, dificultad)
    
    while True:        
        event, values = window.read()

        if (event == sg.WIN_CLOSE_ATTEMPTED_EVENT or event == "-SALIR-") and sg.popup_yes_no("¿Realmente desea salir?", no_titlebar=True) == "Yes":
            break
        elif event == "-JUGAR-":
            if values["-DIFI-"][0] == "{" :
                sg.popup("seleccione una dificultad")
            else:
                sg.popup("la dificultad es : " +values["-DIFI-"])
        elif event == "-CONFIGURACION-":
            config.main()
            nivel = config.carga_config()
        elif event == "-PUNTAJES-":
            tabla_puntajes.mostrar_tabla()
        elif event == "-PERFIL-":  
            try:          
                perfil.usuario(perfiles)
            except AttributeError:
                img_name = "manito.png"
                img_folder = os.path.join("src", "core", "images")
                img = os.path.join(os.getcwd(),img_folder, img_name) 
                sg.popup("CHAU, ¡NOS VEMOS!", image=img, no_titlebar=True)
    

    window.close()
#--------------------------------------------------------------------------------
    
def ventana_principal():
    perfiles = jugadores.apertura_de_archivo()
    dificultad = config.carga_config()

    ventana_de_inicio(perfiles, dificultad)

ventana_principal()



