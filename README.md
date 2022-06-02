=====================

GRUPO 11 - FIGURACE -

INTEGRANTES DEL PROYECTO:
  Ricardo Federico Colantonio Von Saldern
  Lucas Guerendiain
  Joaquin Bruno Mateos 
  Leonel Alejandro Ranieri

===========================================================

FORMAS DE EJECUTAR CADA APLICACIÓN:

1ro - instalar los requerimientos que se piden en requirements.txt
2do - ejecutar los modulos para procesar datos (**)
3ro - ejecutar "figurace.py" con python

(**):archivos que generan los data set que se uilizan:
lagos.py.ipynb
artistas.ipynb
peliculas.ipynb

todos se ejecutan desde el jupyter notebook correspondiente

proyecto disponible en rama "main"
===========================================================

SITIO DESDE DONDE SE OBTUVIERON LOS DATASET:

Grupo A
1) Top 100 de temas musicales de Spotify 2010 a 2019
https://www.kaggle.com/datasets/muhmores/spotify-top-100-songs-of-20152019
3) Lagos
https://drive.google.com/file/d/1PzfCgiAhPAq8Cztx9psk3puxDPHsjnqJ/view?usp=sharing
(extraído de https://www.ign.gob.ar/NuestrasActividades/Geografia/DatosArgentina/Lagos)

Grupo B
1) Películas
https://www.kaggle.com/datasets/disham993/9000-movies-dataset
Deberá adaptar los datos de la siguiente forma:
● Descartar las películas que no tienen “overview”.
● Descartar las películas cuyo idioma original tenga más de 2 caracteres.
● Tomar las 100 palabras más comunes de todos los overviews combinados.
● Para generar el ”Overview” de cada película para el archivo de salida se deberán
descartar las palabras que se encuentren dentro de las 100 más comunes de todos los
overviews y se deberá generar un string con 3 palabras tomadas al azar y ordenadas al
azar (ver random.sample()) de ese resultado. Nota: luego de filtrar las palabras
comunes algunos overviews pueden tener menos de 3 palabras, en esos casos se
tomarán las palabras que se pueda.

===========================================================

