"""
Segon exercici. Observació dels partits jugats.
"""
# Importem les llibreries necessàries
import pandas as pd
import matplotlib.pyplot as plt
# Importem arxiu de configuració
import config



# Funció de l'exercici 2, total de partits jugats per cada equip
def total_matches(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total matches played by each team.
    """
    # Contem els partits jugats pels locals en primer lloc
    home_matches = data["HomeTeam"].value_counts()
    # Contem els partits jugats com a visitant
    away_matches = data["AwayTeam"].value_counts()
    # Sumem els partits jugats a casa i a fora
    total_matches = home_matches + away_matches
    # Hem d'ordenar els equips pel nombre de partits jugats de més a menys
    total_matches = total_matches.sort_values(ascending=False)
    # Convertim a dataframe
    total_matches_by_team = total_matches.reset_index()
    # Un cop convertit a df, s'han de renombrar les columnes, una s'anomena índex
    total_matches_by_team.columns = ["Team", "Total_Matches"]
    # Retornem el df modificat
    return total_matches_by_team

# Funció per crear un plot on es representi el nombre de partits jugats per equip
def plot_matches_team_total(total_matches_by_team: pd.DataFrame) -> None:
    """
    Plot total matches played by team.
    """
    # Creem la figura primer
    plt.figure(figsize=(18, 8))
    # Fem un barplot on l'eix x són els equip i l'eix y els partits jugats
    plt.bar(
        total_matches_by_team["Team"],
        total_matches_by_team["Total_Matches"]
    )
    # Definim el títol i les etiquetes
    plt.title("Total Matches Played By a Team")
    plt.xlabel("Team")
    plt.ylabel("Total Matches")
    # Rotem etiquetes per evitar solapar (vist a posteriori)
    plt.xticks(rotation=90)
    # Ajustem espais i evitem solapar etiquetes
    plt.tight_layout()
    # Guardem el plot com indica l'enunciat
    plt.savefig(f"img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png")
    # Mostrem el plot
    plt.show()