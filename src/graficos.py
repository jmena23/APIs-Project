#!/usr/bin/env python3
import matplotlib.pyplot as plt
from pandas.plotting import table
import seaborn as sns

def estad_equ(df, ini):
    """
    Elabora gráfico de caja y bigotes con las estadísticas de la franquicia
    """
    fig, ax = plt.subplots(figsize = (9,7))
    sns.boxplot(x=['pts', 'reb', 'ast'], y=[df.pts, df.reb, df.ast])
    plt.suptitle(f"Estadísticas de la plantilla de {ini}", y = 0.92, fontsize = 15)
    plt.savefig("output/graficos/pts_reb_asis.png", bbox_inches = 'tight')

def jugpais(df, team):
    """
    Elabora gráfico circular con la distribución de jugadores según país de procedencia
    """
    labels = sorted(df[df.iniciales_equipo == team]['pais'].unique())
    datos = df[df.iniciales_equipo == team].groupby("pais")["pais"].count()
    fig = plt.figure(figsize = (5,5))
    theme = plt.get_cmap('tab20c')
    plt.pie(datos, autopct = "%0.1f %%", radius = 2, labels = labels, colors = [theme(1. * i / len(labels)) for i in range(len(labels))])
    plt.suptitle("DISTRIBUCIÓN DE LOS JUGADORES POR PAISES", y = 1.3, fontsize = 16)
    plt.savefig("output/graficos/dist_jug_pais.png", bbox_inches = 'tight')

def porpais(df, nat):
    """
    Imprime por pantalla los jugadores de la nacionalidad elegida
    """
    print(df[['nombre', 'iniciales_equipo', 'part_jug']][df.pais == nat].sort_values(by = 'part_jug', ascending = False))

def roster(df, team):
    """
    Elabora una tabla con la plantilla de los jugadores de la franquicia elegida
    """
    a = df[['nombre', 'edad', 'altura_cm', 'peso_kg', 'pct_tiro']][df.iniciales_equipo == team]
    a['peso_kg'] = a['peso_kg'].apply(lambda x: round((x),2))
    a['pct_tiro'] = a['pct_tiro'].apply(lambda x: round((x),2))
    fig, ax = plt.subplots(figsize=(12, 5)) 

    ax.xaxis.set_visible(False)  
    ax.yaxis.set_visible(False)  

    ax.set_frame_on(False)  

    tab = table(ax, a, loc='upper right')  

    tab.auto_set_font_size(False)
    tab.set_fontsize(8)
    fig.savefig('output/graficos/roster_equipo.png')

def uso_plantilla(df, equipo, partidos):
    """
    Elabora una tabla con los jugadores de la franquicia elegida que han jugados al menos 
    el nº de partidos elegido
    """
    datos = df[['nombre', 'part_jug']][(df.iniciales_equipo == equipo) & (df.part_jug >= partidos)]
    fig, ax = plt.subplots(figsize=(8, 6)) 

    ax.xaxis.set_visible(False)  
    ax.yaxis.set_visible(False)  

    ax.set_frame_on(False)  

    tab = table(ax, datos, loc='upper right')  

    tab.auto_set_font_size(False)
    tab.set_fontsize(8)
    fig.savefig('output/graficos/uso_plantilla.png')

def est_jug(df, jug):
    """
    Elabora una tabla que compara las estadísticas del jugador con la media de su equipo en
    puntos, rebotes y asistencias
    """
    jugador = df[['nombre', 'iniciales_equipo', 'pts', 'reb', 'ast']][df.nombre == jug]
    team = jugador.iniciales_equipo.iloc[0]
    equip = df[['nombre', 'iniciales_equipo', 'pts', 'reb', 'ast']][df.iniciales_equipo == team]
    jugador.loc[1] = ["MEDIA EQUIPO", team, round((equip.pts.mean()),2), round((equip.reb.mean()),2), round((equip.ast.mean()),2)]
    jugador = jugador.reset_index(drop = True)
    fig, ax = plt.subplots(figsize=(10, 6)) 

    ax.xaxis.set_visible(False)  
    ax.yaxis.set_visible(False)  

    ax.set_frame_on(False)  

    tab = table(ax, jugador, loc='center')  

    tab.auto_set_font_size(False)
    tab.set_fontsize(9)
    fig.savefig('output/graficos/est_jug_equipo.png')

    