import PySimpleGUI as sg


def preparar_configuración():
    puntaje_restado_por_respuesta = 0 
    puntaje_sumado_por_ronda = 0
    
    while True: 
        frame_layout = [ [sg.Text("Ingrese los segundos por ronda")], [sg.Input(key="segundos")],
               [sg.Text("Elija la cantidad de rondas por juego")], [sg.Input(key="rondas")],
               [sg.Text("Puntaje sumado por ronda: ")], [sg.Output(key=puntaje_sumado_por_ronda)],
               [sg.Text("Puntaje restado por cada respuesta incorrecta")], [sg.Output(key=puntaje_restado_por_respuesta)],
               [sg.Button("Listo")]
              ]

        layout = [
             [sg.Frame("CONFIGURACIÓN", frame_layout, font="Any 8", title_color="DarkPurple")]]          

        configuracion = sg.Window("Ventana de configuración del juego", layout, margins=(100,100), finalize=True)

        event, values = configuracion.read()       
        
        if event == "Listo" and event == sg.WIN_CLOSED:
            configuracion.close()
            break
           
        





