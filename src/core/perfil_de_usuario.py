import PySimpleGUI as sg    
import string
import json
import os
import jugadores

"""def tratamiento_de_excepciones(nick, edad, genero):
    digitos = string.digits
    cant = 0
    es_numero = 0
    try:
        for caracter in edad:
            if caracter in digitos:
                cant += 1
        for char in genero:
            if char in digitos:
                es_numero += 1
            if cant != len(edad) or es_numero:
                raise ValueError
            if edad == "" or genero == "":
                raise ValueError           
    except ValueError:
        sg.popup_error("has ingresado datos incorrectos, volve a ingresarlos")
    else:
        perfiles.update({nick: [edad, genero]})  """  

def usuario_registrado(nick, perfiles):
    while True:
        layout = [
            [sg.Text('nick: '), sg.Text(nick)],
            [sg.Text('edad: '), sg.Text(perfiles[nick][0])],
            [sg.Text('género: '), sg.Text(perfiles[nick][1])],
            [sg.Button('Editar', key=("-EDITAR-")), sg.Button('Salir', key=("-SALIR-"))]
         ]

        perfil_de_usuario = sg.Window('Perfil de usuario registrado', layout, margins=(150,150), finalize=True)         
        
        event, values = perfil_de_usuario.read()
        
        if event == "-SALIR-" or event == sg.WIN_CLOSED:
            break
        elif event == "-EDITAR-":
            editar_usuario(nick, perfiles)
            break       
    
    perfil_de_usuario.close()
 

def editar_usuario(nick, perfiles):
    layout = [
             [sg.Text('nick: '), sg.Text(nick)],
             [sg.Text('edad: '), sg.Text(perfiles[nick][0]), sg.Input(key='-EDAD-')],
             [sg.Text('género: '), sg.Text(perfiles[nick][1]), sg.InputText(key='-GENERO-')],
             [sg.Button('listo', key=('-LISTO-')), sg.Button('salir', key=('-SALIR-'))]
            ]
    
    perfil_de_edición_de_usuario = sg.Window('Perfil de edición de usuario', layout, finalize=True)                

    while True:
        event, values = perfil_de_edición_de_usuario.read()
        
        edad = values['-EDAD-']
        genero = values['-GENERO-']

        if event == '-SALIR-' or event == sg.WIN_CLOSED:
            break
        elif event == "-LISTO-":
            if nick == "señor x":
                break
            perfiles[nick] = [edad, genero]

            digitos = string.digits
            cant = 0
            es_numero = 0
            try :
                for caracter in edad:
                    if caracter in digitos:
                        cant += 1
                for char in genero:
                    if char in digitos:
                        es_numero += 1
                if cant != len(edad) or es_numero:
                    raise ValueError
                    
                if edad == "" or genero == "":
                    raise ValueError           
            except ValueError:
                sg.popup_error("has ingresado datos incorrectos, volve a ingresarlos")
                break
            else:
                #perfiles.update({nick: [edad, genero]})
                jugadores.carga_de_datos(perfiles)
                break
    perfil_de_edición_de_usuario.close()

def nuevo_usuario(nick, perfiles):

    while True:
        layout = [
            [sg.Text('nick: '), sg.Text(nick)],
            [sg.Text('edad: ', ), sg.Input(key='-EDAD-')],
            [sg.Text('género: '), sg.In(key='-GENERO-')],
            [sg.Button('guardar', key=('-GUARDAR-')), sg.Button('salir', key=('-SALIR-'))]
         ]
    
        perfil_de_usuario = sg.Window('Perfil del usuario nuevo', layout, finalize=True)        
        event, values = perfil_de_usuario.read()

        edad = values['-EDAD-']
        genero = values['-GENERO-']
        
        if event == "-SALIR-" or event == sg.WIN_CLOSED:
            break
        elif event == "-GUARDAR-":
            perfiles[nick] = [edad, genero]
            #usuarios = perfiles 

            digitos = string.digits
            cant = 0
            es_numero = 0

            try:
                for caracter in edad:
                    if caracter in digitos:
                        cant += 1
                for char in genero:
                    if char in digitos:
                        es_numero += 1
                if cant != len(edad) or es_numero:
                    raise ValueError  #TypeError
                if edad == "" or genero == "":
                    raise ValueError           
            except ValueError:
                sg.popup_error("has ingresado datos incorrectos, volve a ingresarlos")
                del(perfiles[nick]) 
            else:
                #perfiles.update({nick: [edad, genero]})
                jugadores.carga_de_datos(perfiles)
            break 
    perfil_de_usuario.close()
#-------------------------------------------------------------------------------------------------

def usuario(perfiles):
    while True:
        nick = sg.PopupGetText("ingrese su nick", button_color="purple", text_color="black", no_titlebar=True)
        while nick == "" or  nick == None:
            sg.popup("ingrese un nick")
            nick = sg.PopupGetText("ingrese su nick", button_color="purple", text_color="black", no_titlebar=True)
            #sg.Popup('ingresaste el nick: ', nick, button_color="purple", text_color="black", no_titlebar=True)
        break
    
    if nick in perfiles.keys(): 
        sg.popup(f"{nick} es un usuario registrado", no_titlebar=True)  
        usuario_registrado(nick, perfiles)
    else:
        sg.popup(f"{nick} no es un usuario registrado, ingrese sus datos para jugar", no_titlebar=True)
        nuevo_usuario(nick, perfiles)


    
    

      

        


    