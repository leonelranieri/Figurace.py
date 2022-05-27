import os
import json

def apertura_de_archivo():
    """
    Abrir el archivo json.

    Función que genera la ruta para el archivo jugadores.json,
    genera la apertura del mismo con la sentencia 'with' y 
    retorna los datos en un diccionario.
    En manejo de excepciones carga datos por defecto.
    """

    datos_por_defecto = {"señor x": ["83", "m"]} 

    jugadores = os.path.join(os.getcwd(), "src\core", "data", "jugadores.json")

    try:
        with open(jugadores, "r", encoding="utf-8") as entrada:
            usuarios = json.load(entrada)
    except FileNotFoundError:
        usuarios = datos_por_defecto 

    return usuarios

def carga_de_datos(perfiles):
    """ 
    Carga datos del diccionario a un archivo json. Cierra el archivo.  
    """
    usuarios = perfiles
    jugadores = os.path.join(os.getcwd(), "src\core", "data", "jugadores.json")
    with open(jugadores, "w", encoding="utf-8") as salida:
        json.dump(usuarios, salida)
    salida.close()

#apertura_de_archivo()