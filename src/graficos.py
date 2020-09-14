import matplotlib.pyplot as plt
from pandas.plotting import table

def pctiro(df, ini_equipo):
    
    a = df[['nombre', 'edad', 'altura_cm', 'peso_kg', 'pct_tiro']][df.iniciales_equipo == ini_equipo].sort_values(by = 'pct_tiro')

    fig, ax = plt.subplots(figsize = (10,8))
    x = [i for i in a.nombre]
    theme1 = plt.get_cmap('Wistia')
    plt.bar(a.nombre, a.pct_tiro, color = [theme1(1. * i / len(x)) for i in range(len(x))])
    ax.set_xticks(x)
    ax.set_xticklabels(x, rotation = 90)
    plt.xlabel("Jugadores", fontsize = 14)
    plt.ylabel("porcentaje de tiro", fontsize = 14)
    plt.suptitle(f"Porcentaje de tiro por jugador {ini_equipo}", y = 0.92, fontsize = 15)
    plt.savefig("output/graficos/pct_tiro.png", bbox_inches = 'tight')

def jugpais(df, team):
    labels = sorted(df[df.iniciales_equipo == team]['pais'].unique())
    datos = df[df.iniciales_equipo == team].groupby("pais")["pais"].count()
    fig = plt.figure(figsize = (5,5))
    theme = plt.get_cmap('tab20c')
    plt.pie(datos, autopct = "%0.1f %%", radius = 2, labels = labels, colors = [theme(1. * i / len(labels)) for i in range(len(labels))])
    plt.suptitle("DISTRIBUCIÓN DE LOS JUGADORES POR PAISES", y = 1.3, fontsize = 16)
    plt.savefig("output/graficos/dist_jug_pais.png", bbox_inches = 'tight')

def porpais(df, nat):
    print(df[df.pais == nat].sort_values(by = 'part_jug', ascending = False))

def roster(df, team):
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

    