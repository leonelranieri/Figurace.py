import pandas as pd
import os

def get_archivos():
    """Retorna dos archivos generando sus rutas correspondientes"""
    carpeta_archivo = os.path.join("src", "core", "data")
    ruta_archivos = os.path.join(os.getcwd(), carpeta_archivo)

    tabla_puntajes = os.path.join(ruta_archivos, "tabla_puntajes.csv")
    tabla_promedios = os.path.join(ruta_archivos, "tabla_promedios.csv")

    return tabla_puntajes, tabla_promedios

def control_archivos():
    """Controla la existencia del archivo a procesar, de no existir genera uno vacio"""
    tabla_puntajes, tabla_promedios = get_archivos()
    try:
        data_frame = pd.read_csv(tabla_puntajes, encoding='utf-8')
    except FileNotFoundError:
        data_frame = pd.DataFrame(columns=("usuario", "dificultad", "partidas jugadas", 
            "puntos acumulados", "promedio"))
        data_frame.to_csv(tabla_promedios, index=False)
    
    return tabla_promedios, data_frame

def generar_tabla_de_promedios():
    tabla_promedios, data_frame = control_archivos()
    if not data_frame.empty:

        #pasar a lista
        partidas_jugadas = data_frame.groupby(["usuario", "dificultad"])["puntaje"].count()
        puntos_por_jugador = data_frame.groupby(["usuario", "dificultad"])["puntaje"].sum()

        #puntajes_gral = pd.merge(partidas_jugadas, puntos_por_jugador,  on=('usuario', 'dificultad'))
        usuarios = [elemento[0] for elemento in list(partidas_jugadas.index)]
        dificultad = [elemento[1] for elemento in list(puntos_por_jugador.index)]

        promedios = pd.DataFrame(columns=("usuario", "dificultad", "partidas jugadas", 
            "puntos acumulados", "promedio"))
        promedios.usuario = usuarios
        promedios.dificultad = dificultad
        promedios["partidas jugadas"] = list(partidas_jugadas)
        promedios["puntos acumulados"] = list(puntos_por_jugador)
        promedios.promedio = round(promedios["puntos acumulados"] / promedios["partidas jugadas"], 3)

        promedios.to_csv(tabla_promedios, index=False)

    #print(promedios.sort_values("promedio", ascending=False))

    return promedios

def promedio_por_dificultad(dificultad):
    
    tabla_promedios = generar_tabla_de_promedios()

    if not tabla_promedios.empty:
        tabla_promedios =  tabla_promedios.drop(['partidas jugadas'], axis=1)
        tabla_promedios =  tabla_promedios.drop(['puntos acumulados'], axis=1)

        tabla_promedios = tabla_promedios.loc[tabla_promedios['dificultad'] == dificultad]

        #print(tabla_promedios)
        return tabla_promedios

def promedio_por_usuario(usuario):
    """
    Retorna una tabla (DataFrame) con todos los promedios de una determinado usuario.
    """    
    tabla_promedios = generar_tabla_de_promedios()

    if not tabla_promedios.empty:
        tabla_promedios =  tabla_promedios.drop(['partidas jugadas'], axis=1)
        tabla_promedios =  tabla_promedios.drop(['puntos acumulados'], axis=1)

        tabla_promedios = tabla_promedios.loc[tabla_promedios['usuario'] == usuario]

        #print(tabla_promedios)
        return tabla_promedios

def generar_lista(dificultad):
    tabla_promedios = promedio_por_dificultad(dificultad)
    usuarios =  tabla_promedios.usuario.tolist()
    promedios =  tabla_promedios.promedio.tolist()
    union = list(zip(promedios, usuarios))

    return union 


def ordenar_datos(dificultad):
    """Ordena los datos de forma tal que coincidan con el 
    formato de las estructuras de la ventana."""

    datos = generar_lista(dificultad)
    datos = sorted(datos, key=lambda x:x[1], reverse=True)

    datos_ordenados = []
    for elem in datos:
        datos_ordenados.append(elem)
        datos_ordenados = sorted(datos_ordenados, key=lambda x:x[1], reverse=True)
    
    nueva = []
    for i, elem in enumerate(datos_ordenados, start=1):
        indice = [i]
        indice.extend(elem)
        nueva.append(indice)
    
    if len(nueva) > 20:
        nueva = nueva[0:19]

    return nueva

