import pandas as pd
import os

carpeta_archivo = os.path.join("src", "core", "data")
ruta_archivos = os.path.join(os.getcwd(), carpeta_archivo)

tabla_puntajes = os.path.join(ruta_archivos, "tabla_puntajes.csv")
tabla_promedios = os.path.join(ruta_archivos, "tabla_promedios.csv")

try:
    data_frame = pd.read_csv(tabla_puntajes, encoding='utf-8')
except FileNotFoundError:
    data_frame = pd.DataFrame(columns=("usuario", "dificultad", "partidas jugadas", 
        "puntos acumulados", "promedio"))
    data_frame.to_csv(tabla_promedios, index=False)

if not data_frame.empty:
    promedios = data_frame.copy()

    #pasar a lista
    partidas_jugadas = promedios.groupby(["usuario", "dificultad"])["puntaje"].count()
    puntos_por_jugador = promedios.groupby(["usuario", "dificultad"])["puntaje"].sum()

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

    print(promedios)


#obtengo la cantidad de cada uno print(partidas_jugadas.iloc[1])
#obtengo la cantidad total de punto por usuario y dificulta print(puntos_por_jugador.iloc[0])
#print(serie_partidas_jugadas)