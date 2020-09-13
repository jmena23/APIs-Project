#!/usr/bin/env python3
import argparse

def etiquetado():

    parser = argparse.ArgumentParser(description='Estadísticas jugadores NBA temporada 2019-2020')

    parser.add_argument('-r', dest='roster', type = str, default='LAL', help="Iniciales del equipo seleccionado. Deben ser 3 letras mayúsculas")
    parser.add_argument('-p', dest='name', type = str, default='LeBron James', help="Jugador seleccionado")
    parser.add_argument('-c', dest='nationality', type = str, default='Spain', help="País seleccionado")
    parser.add_argument('-j', dest='part_jug', type = int, default='60', help="Partidos jugados")
               
    args = parser.parse_args()
    
    return args