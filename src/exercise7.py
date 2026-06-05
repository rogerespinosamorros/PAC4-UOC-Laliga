# Hem instalat networkx i importem llibreries necessàries
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
# Importem arxiu de configuració
import config
# Importem la funció de l'exercici1, de la càrrega de dades
from exercise1 import load_and_eda


# Definim la funció graf
def graf(data: pd.DataFrame, five_teams_selected: list[str]) -> None:
    """
    A network graph of matches between top five teams in LaLiga.
    """
    # Filtrem l'informació on els equips de casa estan a la llista dels 5 equips i igual quan juguen a fora
    filtered_data = data[data["HomeTeam"].isin(five_teams_selected) & data["AwayTeam"].isin(five_teams_selected)]
    # Definim els enfrontaments entre ells. Anem recorrent les files i es queda amb els partits on coincideixen equips de la llista filtrada.
    # Independentment de si juguen a casa o fora, si coincideixen es crea la connexió. El .apply(axis=1) recorrer el df fila per fila.
    # La fila es guarda a 'row', i creem una llista amb els enfrontaments, el sorted ordena alfabèticament. Un cop ordenat, ho guardem en tuples.
    # No importa si és Barça-Madrid o Madrid-Barça, es quedarà guardat com Barça-Madrid(connexió). Amb value_counts contem la cantidad de connexions.
    # Tot i les dues línies de codi que venen, per obtenir les connexions hi ha hagut mols intents per fer-ho correctament (i crec que ho estan)
    filtered_data["Matchup"] = filtered_data.apply(
        lambda row: tuple(sorted([row["HomeTeam"], row["AwayTeam"]])), axis=1)
    # Definim les conexions entre equips, els matchups, contant els valors i creant el df
    connections = (filtered_data["Matchup"].value_counts().reset_index())
    # Renombrem les noves columnes
    connections.columns = ["Teams", "Connections"]
    # Creem el graf gràcies a la llibreria networkx (utilitzat en l'anterior PAC)
    G = nx.Graph()
    # Hem d'afegir els nodes, que seran els equips
    for team in five_teams_selected:
        G.add_node(team)
    # Ara, les arestes que són les connexions, anem recorrent aquestes connexions
    for _, row in connections.iterrows():
        # Treiem els equips de les files
        team_1, team_2 = row["Teams"]
        # Afegim la connexió un cop trobada
        G.add_edge(team_1, team_2, weight=row["Connections"]) # Estem guardant quants cops s'enfrenten dos equips
    # Ara definim les posicions dels equips en el graf
    pos = nx.spring_layout(G) # spring_layout en la doc oficial explica que és un algoritme que atrau els nodes que més relació tenen
                                # i rebutgen els que no tenen relació. Bastant utilitzat
    # Hem de dibuixar els nodes i arestes (equips i connexions)
    plt.figure(figsize=(12, 8))
    nx.draw(
        G, # El graf
        pos, # Les posicions
        with_labels=True, # Amb etiquetes
        node_size=2000, # Mida dels nodes (ho he fet una mica aleatori el valor)
        font_size=11 # Mida de la lletra 
    )
    # Hem d'ensenyar les etiquetes de les connexions com indica l'enunciat
    connections_labels = nx.get_edge_attributes(G, "weight")   
    # Hem de veure també el nombre de connexions  
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=connections_labels # Etiquetes definides anteriorment
    )        
    # Diria que ja està el graf, ara definim el títol
    plt.title("Matchups Connections Between Top 5 Teams")    
    # Guardem la figura a img, com indica l'enunciat
    plt.savefig(f"img/grafica_ex7_{config.nom_alumne}_{config.date_time}.png")
    # Mostrem el graf
    plt.show()      




# Així, permetem reutilitzar i cridar les funcions i no tot l'arxiu en altres llocs, i també
# permetem que el codi només s'executi quan executem aquest arxiu directament, i no quan importem les funcions en altres arxius
if __name__ == "__main__":
    # Carreguem el dataset
    data = load_and_eda("data/LaLiga_Matches.csv")

    # Definim els 5 equips que millor puntuació tenen
    five_teams_selected = [
        "Barcelona",
        "Real Madrid",
        "Ath Madrid",
        "Valencia",
        "Ath Bilbao"
    ]
    # La funció graf
    graf(data, five_teams_selected)


    # # Filtrem l'informació on els equips de casa estan a la llista dels 5 equips i igual quan juguen a fora
    # filtered_data = data[data["HomeTeam"].isin(five_teams_selected) & data["AwayTeam"].isin(five_teams_selected)]
    # # Definim els enfrontaments entre ells. Anem recorrent les files i es queda amb els partits on coincideixen equips de la llista filtrada.
    # # Independentment de si juguen a casa o fora, si coincideixen es crea la connexió. El .apply(axis=1) recorrer el df fila per fila.
    # # La fila es guarda a 'row', i creem una llista amb els enfrontaments, el sorted ordena alfabèticament. Un cop ordenat, ho guardem en tuples.
    # # No importa si és Barça-Madrid o Madrid-Barça, es quedarà guardat com Barça-Madrid(connexió). Amb value_counts contem la cantidad de connexions.
    # # Tot i les dues línies de codi que venen, per obtenir les connexions hi ha hagut mols intents per fer-ho correctament (i crec que ho estan)
    # filtered_data["Matchup"] = filtered_data.apply(
    #     lambda row: tuple(sorted([row["HomeTeam"], row["AwayTeam"]])), axis=1)

    # connections = (filtered_data["Matchup"].value_counts().reset_index())
    # connections.columns = ["Teams", "Connections"]
    # print(connections)

    # El bloc superior comentat, han sigut comprovacions fetes per obtenir les coincidències entre els 5 equips que demanava l'enunciat