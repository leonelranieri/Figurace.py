import PySimpleGUI as sg    


def usuario_registrado(nick, perfiles):
    while True:
        layout = [
            [sg.Text('nick: '), sg.Text(nick)],
            [sg.Text('edad: '), sg.Text(perfiles[nick][0])],
            [sg.Text('género: '), sg.Text(perfiles[nick][1])],
            [sg.Button('Editar'), sg.Button('Salir')]
         ]

        perfil_de_usuario = sg.Window('Perfil de usuario registrado', layout, margins=(150,150), finalize=True)         
        
        event, values = perfil_de_usuario.read()
        
        if event == "Salir" or event == sg.WIN_CLOSED:
            break
        elif event == "Editar":
            editar_usuario(nick, perfiles)
 

def editar_usuario(nick, perfiles):
    while True:
        layout = [
             [sg.Text('nick: '), sg.Text(nick)],
             [sg.Text('edad: '), sg.Text(perfiles[nick][0]), sg.In(key='edad')],
             [sg.Text('género: '), sg.Text(perfiles[nick][1]), sg.In(key='género')],
             [sg.Button('Listo'), sg.Button('Salir')]
            ]
    
        perfil_de_edición_de_usuario = sg.Window('Perfil de edición de usuario', layout, finalize=True)                
                
        event, values = perfil_de_edición_de_usuario.read()

        if event == 'Salir' or event == sg.WIN_CLOSED:
            break
        elif event == "Listo":
            perfiles.update({nick: [values['edad'], values['género']]})
            sg.Popup(f"datos del jugador \n, nombre {nick} : \n edad y género {perfiles[nick]}", no_titlebar=True)
            break
  
def nuevo_usuario(nick, perfiles):
    while True:
        layout = [
            [sg.Text('nick: '), sg.Text(nick)],
            [sg.Text('edad: ', ), sg.In(key='edad')],
            [sg.Text('género: '), sg.In(key='género')],
            [sg.Button('Guardar'), sg.Button('Salir')]
         ]
    
        perfil_de_usuario = sg.Window('Perfil del usuario nuevo', layout, finalize=True)        
        event, values = perfil_de_usuario.read()

        if event == "Salir" or event == sg.WIN_CLOSED:
            break
        elif event == "Guardar":
            perfiles.update({nick: [values['edad'], values['género']]})
            sg.Popup(f"datos del jugador \n, nombre {nick} : \n edad y género {perfiles[nick]}", no_titlebar=True)
            usuario_registrado(nick, perfiles)
            break    

#------------------------------------------------------------
perfiles = {"leo": ["39", "M"]}

def usuario():
    while True:
        nick = sg.PopupGetText("ingrese su nick", button_color="purple", text_color="black", no_titlebar=True)
        break
    sg.Popup('ingresaste el nick: ', nick, button_color="purple", text_color="black", no_titlebar=True)

    if nick in perfiles.keys(): 
        sg.popup(f"{nick} es un usuario registrado", no_titlebar=True)  
        usuario_registrado(nick, perfiles)
    else:
        sg.popup(f"{nick} no es un usuario registrado, ingrese sus datos para jugar", no_titlebar=True)
        nuevo_usuario(nick, perfiles)

      

        


    