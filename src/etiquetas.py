#!/usr/bin/env python3
import argparse

def etiquetado():
    """
    Mediante esta función se establecen 4 etiquetas para poder filtrar los resultados de main.py
    -t: filtrar franquicias por sus 3 iniciales
    -p: filtrar jugadores por su nombre
    -n: filtar dataset por nacionalidad de los jugadores
    -g: filtrar número de partidos que han jugado en la temporada 
    """

    parser = argparse.ArgumentParser(description='Estadísticas jugadores NBA temporada 2019-2020')

    parser.add_argument('-t', dest='roster', type = str, default='LAL', help="Iniciales del equipo seleccionado. Deben ser 3 letras mayúsculas")
    parser.add_argument('-p', dest='name', type = str, default='LeBron James', help="Jugador seleccionado")
    parser.add_argument('-n', dest='nationality', type = str, default='Spain', help="País seleccionado")
    parser.add_argument('-g', dest='part_jug', type = int, default='60', help="Partidos jugados")
               
    args = parser.parse_args()
    
    return args