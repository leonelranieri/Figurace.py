import PySimpleGUI as sg
import perfil_de_usuario as perfil
import ventana_de_configuracion as config

nombres = ["elija el usuario", "pao", "leo", "valen"]
dificultad = ["elija la dificultad", "fácil", "normal", "difícil"]

def preparar_menu(nombres, dificultad):
    """
    función que crea y retorna una ventana menú para el juego 
    """
    frame_layout =[
                  [sg.T('---Menú---')],
                  [sg.Button("Jugar")],
                  [sg.Button("Configuración")], 
                  [sg.Button("Puntajes")],
                  [sg.Button("Perfil")],
                  [sg.Button("Salir")],
                  [sg.Combo(nombres, default_value=nombres, s=(13,1)), sg.Combo(dificultad, default_value=dificultad, s=(15,1))]
               ]

    layout = [
             [sg.Frame("FIGURACE", frame_layout, font="Any 12", title_color="DarkBlue")]]

    menu = sg.Window("MENÚ - FIGURACE -", layout, enable_close_attempted_event=True, margins=(100, 100))   

    return menu


def ventana_de_inicio(nombres, dificultad):
    """
    asigna eventos y valores leídos desde la ventana menú, 

    permite salir del menú o acceder a otras ventanas.  
    """
    sg.theme('BrightColors')

    while True:
        event, values = preparar_menu(nombres, dificultad).read()
        if (event == sg.WIN_CLOSE_ATTEMPTED_EVENT or event == "Salir") and sg.popup_yes_no("¿Realmente desea salir?") == "Yes":
            break
        elif event == "Configuración":
            config.preparar_configuración()
        elif event == "Puntajes":
            sg.Text("ventana de puntajes")
        elif event == "Perfil":
            perfil.usuario()
    preparar_menu(nombres, dificultad).close()
#---------------------------------------------------------------------------------

ventana_de_inicio(nombres, dificultad)



