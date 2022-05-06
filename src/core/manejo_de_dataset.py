import os
import csv

carpeta_archivo = os.path.join("src\core", "archive (1)")
ruta_archivos = os.path.join(os.getcwd(), carpeta_archivo)
spotify_csv = os.path.join(ruta_archivos, "Spotify 2010 - 2019 Top 100.csv")

csv_modificado = os.path.join(ruta_archivos, "copia.csv")

adaptación = os.path.join(ruta_archivos, "resultante_spotify.csv")


def modificacion_del_spotifycsv(spotify_csv, csv_modificado):

    """ en base a un archivo csv ('Spotify 2010 - 2019'), genera otro denominado 
    'copia.csv' con los datos de la columna género modificados según una serie de pautas
    """

    with open(spotify_csv, "r", encoding="utf-8") as data_set:
        reader = csv.reader(data_set, delimiter=',')
        encabezado = reader.__next__()

        with open(csv_modificado, "x", encoding="utf-8") as copia:
            writer = csv.writer(copia)
            writer.writerow(encabezado)
     
            siglas = ["EDM", "DFW", "UK", "R&B", "LGBTQ+"]

            for row in reader: 
                linea = list(row)
                if row[2].split(" ")[0].upper() in siglas: 
                    sigla = row[2].split(" ")[0].upper()
                    genero = sigla + " ".join(row[2].split(" ")[1:])
                    linea[2] = genero
                elif row[2].split("-")[0] == "k":
                    char = row[2].split(" ")[0].upper()
                    genero = char + "-".join(row[2].split(" ")[1:])
                    linea[2] = genero
                else:
                    genero = row[2].title()
                    linea[2] = genero
                writer.writerow(linea)    

def generar_archivo_de_trabajo(csv_modificado, adaptación):
    """ esta función recibe el archivo 'copia.csv' y genera un nuevo archivo 'resultante_spotify.csv'
        eliminando las columnas que no son de intéres
    """
    with open(csv_modificado, "r", encoding="utf-8") as data_set:
        reader = csv.reader(data_set, delimiter=",")

        encabezado = reader.__next__()

        encabezado_salida = []

        encabezado_salida.append(encabezado[2].title())
        encabezado_salida.append(encabezado[16].title())
        encabezado_salida.append(encabezado[3].title())
        encabezado_salida.append(encabezado[15].title())
        encabezado_salida.append(encabezado[5].upper())
        encabezado_salida.append(encabezado[1].title())

        with open(adaptación, "x", encoding="utf-8") as salida:
            writer = csv.writer(salida)    

            writer.writerow(encabezado_salida)
            
            for row in reader:
                if row != []:
                    linea = []
                    linea.append(row[2])
                    linea.append(row[16])
                    linea.append(row[3])
                    linea.append(row[15])
                    linea.append(row[5])
                    linea.append(row[1])
                    writer.writerow(linea)


modificacion_del_spotifycsv(spotify_csv, csv_modificado)
generar_archivo_de_trabajo(csv_modificado, adaptación)

   # with open(adaptación, "x", encoding="utf-8") as salida:
    #    writer = csv.writer(salida)
     #   writer.writerow(encabezado_salida)

    




