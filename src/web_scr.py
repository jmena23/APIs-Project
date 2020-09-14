#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import pandas as pd
import src.etiquetas as tq

def dimefranq():
    """
    Mediante esta función se obtienen los nombres de las 30 francquicias NBA haciendo una consulta a la web
    de la propia NBA
    """
    df = pd.read_csv('output/nbaplayers20192020.csv')
    args = tq.etiquetado()
    ini_equipo = args.roster

    res = requests.get("https://es.global.nba.com/teamindex/?_ga=2.248718414.854577378.1600093305-538605728.1600093305")
    soup = BeautifulSoup(res.text, 'html.parser')
    tag = soup.select(".nbap-nav__dropdown-link")
    equipos = []
    for i in tag:
        equipos.append((i.text).strip())
        
    equipos = sorted(equipos[:30])
    inic = sorted(df.iniciales_equipo.unique())

    indice_ini_eq = inic.index(ini_equipo)
    nombre_equipo = equipos[indice_ini_eq]
    return nombre_equipo