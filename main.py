#!/usr/bin/env python3
import argparse
import pandas as pd
import src.etiquetas as tq
import src.graficos as gf
import src.pdf as pf


def main():
    df = pd.read_csv('output/nbaplayers20192020.csv')

    args = tq.etiquetado()
    ini_equipo = args.roster
    jugador = args.name
    nationality = args.nationality
    part_jug = args.part_jug

    gf.porpais(df, nationality)
    gf.roster(df, ini_equipo)
    gf.uso_plantilla(df, ini_equipo, part_jug)
    gf.estad_equ(df, ini_equipo)
    gf.jugpais(df,ini_equipo)
    gf.est_jug(df, jugador)
    pf.imprimepdf()
    



if __name__ == "__main__":
    main()