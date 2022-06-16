import PySimpleGUI as sg    
import string
import jugadores
import os

# COMENTARIO
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

def usuario_registrado(nick, perfiles, generos):
    """
    Muestra los datos de un usuario registrado.

    Recibe un diccionario y muestra los datos de la clave (nick),
    permitiendo, al mismo, tiempo salir de la ventana o 
    seleccionar la opción de edición del usuario registrado.
    """   
    while True:
        layout = [
            [sg.Text('nick: '), sg.Text(nick)],
            [sg.Text('edad: '), sg.Text(perfiles[nick][0])],
            [sg.Text('género: '), sg.Text(perfiles[nick][1])],
            [sg.Button('Editar', key=("-EDITAR-")), sg.Button('Salir', key=("-SALIR-"))]
         ]

        window = sg.Window('Perfil de usuario registrado', layout, 
            margins=(150,150), finalize=True)      
        
        event, values = window.read()
        
        if event == "-SALIR-" or event == sg.WIN_CLOSED:
            break
        elif event == "-EDITAR-":
            editar_usuario(nick, perfiles, generos)
            break       
    
    window.close()

def editar_usuario(nick, perfiles, generos):
    """
    Edita edad y genero de la clave recibida, guarda la información en un archivo json.

    Recibe un diccionario y muestra los datos de la clave (nick),
    permitiendo, al mismo, editar los valores de cada clave. 
    tiempo salir de la ventana o 
    seleccionar la opción de edición del usuario registrado.
    """
    def editar_ambos(generos):
        """
        retorna una ventana que permite editar la edad y el género al mismo tiempo.

        """
        layout_ambos = [
             [sg.Text('nick: '), sg.Text(nick)],
             [sg.Text('edad: '), sg.Text(perfiles[nick][0]), sg.Input(key='-EDAD-')],
             [sg.Text('género:'), sg.Text(perfiles[nick][1]), 
                sg.InputCombo(generos, key='-GENERO-')],
             [sg.Button('listo', key=('-LISTO-')), sg.Button('salir', key=('-SALIR-'))],
             [sg.Button('editar edad', key=('-EDITAR-EDAD-'))],
             [sg.Button('editar género', key=('-EDITAR-GENERO-'))]
            ]
        return sg.Window("ventana de edición de género y edad", layout_ambos, finalize=True)
    
    def editar_edad():
        """
        retorna una ventana que permite editar solo la edad.

        """
        layout_edad = [
             [sg.Text('nick: '), sg.Text(nick)],
             [sg.Text('edad: '), sg.Text(perfiles[nick][0]), sg.Input(key='-EDAD-')],
             [sg.Text('género: '), sg.Text(perfiles[nick][1])],
             [sg.Button('listo', key=('-LISTO-EDAD-')), sg.Button('salir', key=('-SALIR-'))],
             [sg.Button('volver', key=('-VOLVER-'))]
            ]
        return sg.Window("ventana de edición para la edad", layout_edad, finalize=True)

    def editar_genero(generos):
        """
        retorna una ventana que permite editar solo el género.

        """
        layout_genero = [
             [sg.Text('nick: '), sg.Text(nick)],
             [sg.Text('edad: '), sg.Text(perfiles[nick][0])],
             [sg.Text('género:'), sg.Text(perfiles[nick][1]), 
                sg.InputCombo(generos, key='-GENERO-')],
             [sg.Button('listo', key=('-LISTO-GENERO-')), sg.Button('salir', key=('-SALIR-'))],
             [sg.Button('volver', key=('-VOLVER-'))]             
            ]
        return sg.Window("ventana de edición para el género", layout_genero, finalize=True)    

    ventana_ambos = editar_ambos(generos)

    while True:
        current, event, values = sg.read_all_windows() 

        if event == '-SALIR-' or event == sg.WIN_CLOSED:
            usuario_registrado(nick, perfiles, generos)
            current.close()
            ventana_ambos.close()
            break        
        elif event == '-EDITAR-EDAD-':
            editar_edad()
            ventana_ambos.close()
            current.close()
        elif event == '-EDITAR-GENERO-':
            #window = editar_genero(generos)
            editar_genero(generos)
            ventana_ambos.close()
            current.close()
        elif event == '-VOLVER-':
            editar_ambos(generos)
            current.close()
            ventana_ambos.close()
        elif event == "-LISTO-": 
            edad = values["-EDAD-"]
            genero = values["-GENERO-"]
            #usuario por defecto
            if nick == "señor x":
                break
            perfil_inicial = [perfiles[nick][0], perfiles[nick][1]]
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
                if (cant != len(edad) or es_numero): 
                    raise TypeError
                if edad == "" or genero == "":
                    raise ValueError           
            except ValueError:
                sg.popup_error("ups!, no has ingresado datos, volve a intentarlo") 
                perfiles[nick] = perfil_inicial
            except TypeError:
                sg.popup_error("donde dice EDAD ingresa un número, donde dice GÉNERO" 
                     + " elejí una opción o escribi tu género auto percibido") 
                perfiles[nick] = perfil_inicial               
            else:
                #perfiles.update({nick: [edad, genero]})
                jugadores.carga_de_datos(perfiles)
                break
        elif event == "-LISTO-EDAD-":
            edad = values['-EDAD-']
            genero = perfiles[nick][1]
            #usuario por defecto
            if nick == "señor x":
                break
            perfil_inicial = [perfiles[nick][0], perfiles[nick][1]]
            perfiles[nick] = [edad, genero]
            digitos = string.digits
            cant = 0
            try :
                for caracter in edad:
                    if caracter in digitos:
                        cant += 1
                if (cant != len(edad)): 
                    raise TypeError
                if edad == "":
                    raise ValueError           
            except ValueError:
                sg.popup_error("ups!, no has ingresado datos, volve a intentarlo")
                perfiles[nick] = perfil_inicial
            except TypeError:
                sg.popup_error("donde dice EDAD ingresa un número") 
                perfiles[nick] = perfil_inicial
            else:
                #perfiles.update({nick: [edad, genero]})
                jugadores.carga_de_datos(perfiles)
                break       
        elif event == "-LISTO-GENERO-":
            edad = perfiles[nick][0]
            genero = values['-GENERO-']
            #usuario por defecto
            if nick == "señor x":
                break
            perfil_inicial = [perfiles[nick][0], perfiles[nick][1]]
            perfiles[nick] = [edad, genero]
            digitos = string.digits
            es_numero = 0
            try :
                for char in genero:
                    if char in digitos:
                        es_numero += 1
                if (es_numero): 
                    raise TypeError
                if genero == "":
                    raise ValueError           
            except ValueError:
                sg.popup_error("ups!, no has ingresado datos, volve a intentarlo") 
                perfiles[nick] = perfil_inicial
            except TypeError:
                sg.popup_error("donde dice GÉNERO elejí una opción o escribi tu género auto percibido") 
                perfiles[nick] = perfil_inicial
            else:
                #perfiles.update({nick: [edad, genero]})
                jugadores.carga_de_datos(perfiles)
                break

    current.close()
    ventana_ambos.close()
    #return perfil_de_edición_de_usuario


def nuevo_usuario(nick, perfiles, generos):
    """
    Crea un nuevo usuario con la clave recibida, guarda la información en un archivo json.

    Recibe un diccionario y con la clave (nick) asocia dos valores 
    que ingresan por teclado, permitiendo, al mismo, salir sin registrarse.
    """
    while True:

        layout = [
            [sg.Text('nick: '), sg.Text(nick)],
            [sg.Text('edad: ', ), sg.Input(key='-EDAD-')],
            [sg.Text('género: -si no se identifica escriba otro-'), sg.InputCombo(generos, key='-GENERO-')],
            [sg.Button('guardar', key=('-GUARDAR-')), sg.Button('salir', key=('-SALIR-'))]
         ]
    
        window = sg.Window('Perfil de usuario nuevo', layout, finalize=True)        
        event, values = window.read()

        edad = values['-EDAD-']
        genero = values['-GENERO-']
        
        if event == "-SALIR-" or event == sg.WIN_CLOSED:
            usuario(perfiles)
            break
        if event == "-GUARDAR-":
            perfiles[nick] = [edad, genero]

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
                del(perfiles[nick])
                nuevo_usuario(nick, perfiles, generos)
                break
            else:
                #perfiles.update({nick: [edad, genero]})
                jugadores.carga_de_datos(perfiles)
                break 
    window.close()
#-------------------------------------------------------------------------------------------------

def usuario(perfiles):
    try:
        generos = ["femenino", "masculino", "no-binarie", "X", "cisgénero"]        
        hubo_registro = False
        while True:
            nick = sg.PopupGetText("ingrese su nick", button_color="purple", text_color="black", 
                no_titlebar=True)
            break
            
        if nick.strip(" ") == "" or nick == None:
            raise AttributeError
        else: 
            if nick in perfiles.keys(): 
                sg.popup(f"{nick} es un usuario registrado", no_titlebar=True)  
                usuario_registrado(nick, perfiles, generos)
                hubo_registro = True
            else:
                sg.popup(f"{nick} no es un usuario registrado, ingrese sus datos para jugar", no_titlebar=True)
                nuevo_usuario(nick, perfiles, generos)
                hubo_registro = True
    except AttributeError:
        img_name = "manito.png"
        img_folder = os.path.join("src", "core", "images")
        img = os.path.join(os.getcwd(),img_folder, img_name) 
        sg.popup("CHAU, ¡NOS VEMOS!", image=img, no_titlebar=True)
        
    return hubo_registro, perfiles
    

      

        


    