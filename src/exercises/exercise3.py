# Primer importem llibreries que segur que utilitzarem
import pandas as pd
import matplotlib.pyplot as plt
# Importem l'arxiu de configuració
import config
# Carreguem el dataset amb la funció de l'exercici 1
from src.exercises.exercise1 import load_and_eda

# Definim la funció goals_distribution(data) com indica l'enunciat 
# Retorna una tupla perquè conté dos dataframes, un per l'equip local i un per l'equip visitant
def goals_distribution(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Calculate goal distribution for home and away teams.
    """
    # Primer calculem la distribució de gols per l'equip local
    home_distribution = data["FTHG"].value_counts()
    # Calculem també la distribució de gols per l'equip visitant
    away_distribution = data["FTAG"].value_counts()
    # Ordenem els resultats pel nombre de gols (index)
    home_distribution = home_distribution.sort_index()
    away_distribution = away_distribution.sort_index()
    # Convertim a dataframes
    home_distribution = home_distribution.reset_index()
    away_distribution = away_distribution.reset_index()
    # Renombrem les columnes amb els noms adients
    home_distribution.columns = ["Goals", "Matches"]
    away_distribution.columns = ["Goals", "Matches"]
    # Finalment retornem la tupla amb els dos dataframes
    return home_distribution, away_distribution

# Funció per mostrar la distribució dels gols, una gràfica i dos plots
def plot_goals_distribution(home_distribution: pd.DataFrame, away_distribution: pd.DataFrame) -> None:
    """
    Plot goal distribution for home and away teams. 
    """
    # Creem la figura i els eixos de les dues gràfiques
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))
    # Gràfica per l'equip local, gràfic esquerre
    axes[0].bar(home_distribution["Goals"], home_distribution["Matches"])
    # Títol i etiquetes per l'equip local
    axes[0].set_title("Home Team Goals Distribution")
    axes[0].set_xlabel("Goals")
    axes[0].set_ylabel("Matches")
    # Gràfica per l'equip visitant, gràfic dret
    axes[1].bar(away_distribution["Goals"], away_distribution["Matches"])
    # Títol i etiquetes per l'equip visitant
    axes[1].set_title("Away Team Goals Distribution")
    axes[1].set_xlabel("Goals")
    axes[1].set_ylabel("Matches")
    # Ajustem espais entre gràfiques
    plt.tight_layout()
    # Guardem la figura com indica l'enunciat
    plt.savefig(f"img/grafica_ex3_{config.nom_alumne}_{config.date_time}.png")
    # Mostrem la figura
    plt.show()

# Així, permetem reutilitzar i cridar les funcions i no tot l'arxiu en altres llocs, i també
# permetem que el codi només s'executi quan executem aquest arxiu directament, i no quan importem les funcions en altres arxius
if __name__ == "__main__":
    # Carreguem el dataset
    data = load_and_eda("data/LaLiga_Matches.csv")
    # Calculem la distribució dels gols per equips locals i visitants
    distr_goals_home, distr_goals_away = goals_distribution(data)
    # Comprovem les gràfiques de distribució amb la funció de plot
    plot_goals_distribution(distr_goals_home, distr_goals_away)
    # També podriem imprimir els dataframes per verue les distribucions numèriques

