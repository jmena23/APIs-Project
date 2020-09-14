# APIs-Project
Tercer proyecto Ironhack - Bootcamp Data Analytics: APIs con Web Scraping

## Analizamos lo que han hecho los jugadores de la NBA en la temporada 2019 - 2020

![dcbef4ce-nba-jugadores](https://user-images.githubusercontent.com/61025562/93003467-c297f880-f536-11ea-9879-26863493321b.png)

## Objetivo

Los objetivos de este proyecto son varios. Por un lado, la elaboración de un script en python que pueda llamarse desde la terminal y que nos devuelva lo que le pidamos de un dataset a través de etiquetas. Otro de los objetivos es enriquecer el dataset mediante la incorporación de datos provenientes de una API o mediante web scraping. Y por último, generar un reporte de los outputs obtenidos.

El dataset utilizado en este proyecto proviene de https://www.kaggle.com/justinas/nba-players-data

La API utilizada ha sido https://rapidapi.com/theapiguy/api/free-nba/endpoints

## Metodología

La metodología seguida para el desarrollo de este proyecto es la siguiente:

- Elección de dataset, enriquecimiento del mismo mediante consulta a API y limpieza de datos
- Creación de script ejecutable desde consola
- Elaboración de funciones que alimentan al programa principal (main.py)
- Creación de reporte en pdf con los outputs del programa principal

## Organización del proyecto

- Archivo .ipynb donde se puede ver el dataset, su limpieza y la consulta a la API
- Archivo main.py el cual se puede ejecutar desde la terminal y hacer consultas filtradas mediante etiquetas
- Carpeta src donde se pueden ver 4 archivos .py que alimentan al principal.
    - etiquetas.py contiene etiquetas para aplicar filtros en el dataset
    - graficos.py contiene las funciones que elaboran los gráficos y tablas
    - pdf.py que elabora el reporte en pdf
    - web_scr.py que contiene un pequeño scrapeo a la web de la NBA para extraer los nombres de la franquicias
- Carpeta output que contiene un ejemplo de reporte en .pdf y una carpeta con los gráficos del reporte

## Enlaces de interés

https://docs.python.org/3/library/argparse.html

https://www.crummy.com/software/BeautifulSoup/bs4/doc/

https://pyfpdf.readthedocs.io/en/latest/index.html

https://pandas.pydata.org/docs/

https://matplotlib.org/3.3.1/contents.html

https://2.python-requests.org/en/master/
