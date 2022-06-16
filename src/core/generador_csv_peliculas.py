import csv
import os
from collections import Counter
import random
import pandas as pd

# Descartar las películas que no tienen “overview”.
# ● Descartar las películas cuyo idioma original tenga más de 2 caracteres.
# ● Tomar las 100 palabras más comunes de todos los overviews combinados.
# ● Para generar el ”Overview” de cada película para el archivo de salida se deberán
# descartar las palabras que se encuentren dentro de las 100 más comunes de todos los
# overviews y se deberá generar un string con 3 palabras tomadas al azar y ordenadas al
# azar (ver random.sample()) de ese resultado. Nota: luego de filtrar las palabras
# comunes algunos overviews pueden tener menos de 3 palabras, en esos casos se
# tomarán las palabras que se pueda.
# ● Se utilizarán como datos de las tarjetas: “Genre”, “Original_Language”, “Vote_Average”,
# “Release_Date” y 3 palabras aleatorias del overview separadas por “;”. Como dato a
# adivinar se utilizará “Title”. Descartar el resto de las columnas.
# ● El archivo resultante deberá tener las siguientes columnas (en este orden específico):
# “Genre”, “Original_Language”, “Release_Date”, “Vote_Average”, “Overview” y “Title”

#Genera las cadenas de 3 palabras o menos de acuerdo al si hay palabras de overview en word_list
def generar_cadena(cadena):
     """Busca palabra por palabra en la cadena de la linea de overviews y va descartando del la 
     linea si la palabra actual esta en la word list que contiene las 100 palabras que aparecen 
     en los overviews combinados"""
     data = []
     for palabra,word in zip(cadena,word_list):
         if palabra != word:
             data.append(palabra)
     data = ";".join(random.sample(data,min(len(data),3)))
     return data

ubicacion = os.path.join("folder_csv")
carpeta_actual = os.path.join("src")
carpeta_sig = os.path.join("core")
ruta_act = os.path.join(os.getcwd(),carpeta_actual,carpeta_sig) 
ruta_final = os.path.join(ruta_act,ubicacion)

with open(os.path.join(ruta_final,'mymoviedb.csv'), "r",encoding="utf8") as logs_peliculas:
     lector = csv.reader(logs_peliculas, delimiter=",")
     header, datos = next(lector), list(lector)
    
     #Lista de las 100 palabras mas comunes en el overview combinados de todas las peliculas    
     word_list = []
     for linea in datos:
         cadena = linea[2].split()
         for palabra in cadena:
             word_list.append(palabra)
     
     word_list = list(dict(Counter(word_list).most_common(100)).keys()) 
                             
     # Refino los datos a guardar en el csv en base a lo que pide el enunciado
     refined_data_list = []
     for linea in datos:
         idioma = len(linea[6])
         cadena = linea[2].split() #Lista de palabras de la cadena actual del overview
         if idioma == 2 and len(linea[2]) > 0:
             refined_data_list.append({'Genre': linea[7], 'Original_Language': linea[6],'Release_Date': linea[0],'Vote_Average': linea[5],'Overview': generar_cadena(cadena),'Title': linea[1]})

#Inserto los datos en el csv usando panda y saco el index creado por defecto
field_names =['Genre','Original_Language','Release_Date','Vote_Average','Overview','Title']
df = pd.DataFrame(refined_data_list,columns=field_names)
df.to_csv(os.path.join(os.getcwd(),ruta_final,'peliculas_figurace.csv'), index=False) 
