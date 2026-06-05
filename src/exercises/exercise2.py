# Importem configuració del config.py
import config
# Hem d'importar la funció de càrrega de dades de l'exercici 1
from src.exercises.exercise1 import load_and_eda
# Importem llibreries necessàries
import pandas as pd
import matplotlib.pyplot as plt

# Funció de l'exercici 2, total de partis jugats per cada equip
def total_matches(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total matches played by each team.
    """
    # Contem els partits jugats com a local primer
    home_matches = data["HomeTeam"].value_counts()
    # Contem els partits jugats com a visitant
    away_matches = data["AwayTeam"].value_counts()
    # Ara hem de sumar els partits jugats a casa i els jugats a fora
    total_matches = home_matches + away_matches
    # Hem d'ordenar els equips pel nombre de partits jugats de més a mneys
    total_matches = total_matches.sort_values(ascending=False)
    # Ara volem convertir a dataframe 
    total_matches_by_team = total_matches.reset_index()
    # Aquí he vist que s'han de renombrar les columnes, perquè una s'anomena 'índex'
    total_matches_by_team.columns = ["Team", "Total_Matches"]
    # Finalment retornem el dataframe modificat
    return total_matches_by_team

# Funció per veure els equips que sempre han estat a primera divisió
def teams_always_in_first_division(total_matches_by_team: pd.DataFrame) -> pd.DataFrame:
    """
    Return teams that have always been in the first division.
    """
    # Hem de buscar el número de partits màxims jugats possible
    max_matches = total_matches_by_team["Total_Matches"].max()
    # Filtrem equips que compleixen el número màxim de partits possibles
    always_first_division = total_matches_by_team[total_matches_by_team["Total_Matches"] == max_matches]
    # Retornem el dataframe
    return always_first_division

# Funció per crear un plot on es representi el nombre de partits jugats per equip
def plot_matches_team_total(total_matches_by_team: pd.DataFrame) -> None:
    """
    Plot total matches played by team
    """
    # Creem el plot primer
    plt.figure(figsize=(18, 8))
    # Fem un barplot on l'eix x són els equips i l'eix y els partits jugats
    plt.bar(
        total_matches_by_team["Team"],
        total_matches_by_team["Total_Matches"]
    )
    # Definim el títol i les etiquetes
    plt.title("Total Matches Played by Team")
    plt.xlabel("Team")
    plt.ylabel("Total Matches")
    # Rotem etiquetes per evitar solapar (vist a posteriori)
    plt.xticks(rotation=90)
    # Ajustem espais i evitem solapar etiquetes
    plt.tight_layout()
    # Guardem el plot com indica l'enunciat
    plt.savefig(f"img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png")
    # Ensenyem el plot
    plt.show()



# Així, permetem reutilitzar i cridar les funcions i no tot l'arxiu en altres llocs, i també
# permetem que el codi només s'executi quan executem aquest arxiu directament, i no quan importem les funcions en altres arxius
if __name__ == "__main__":
    data = load_and_eda("data/LaLiga_Matches.csv")
    total_matches_by_team = total_matches(data)
    print(total_matches_by_team.head(10))
    always_first_division = teams_always_in_first_division(total_matches_by_team)
    print(always_first_division)

    plot_matches_team_total(total_matches_by_team)
    
