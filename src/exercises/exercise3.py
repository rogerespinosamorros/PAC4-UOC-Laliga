"""
Tercer exercici. Observació de la distribució dels gols.
"""
# Importem les llibreries
import pandas as pd
import matplotlib.pyplot as plt
# Importem arxiu de configuració
import config

# Definim la funció de l'exercici 3, goals_distribution, on retornarà una tupla amb dos dataframes
def goals_distribution(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Calculate goal distribution for home and away teams.
    """
    # Primer calculem la quantitat de gols per l'equip local
    home_distribution = data["FTHG"].value_counts()
    # Calculem la quantitat de gols dels equips visitants
    away_distribution = data["FTAG"].value_counts()
    # Ordenem els resultats pel nombre de gols (índex)
    home_distribution = home_distribution.sort_index()
    away_distribution = away_distribution.sort_index()
    # Convertim a dataframes
    home_distribution = home_distribution.reset_index()
    away_distribution = away_distribution.reset_index()
    # Renombrem les columes amb els noms adients
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
    # Primer gràfica pels equips locals, el gràfic de l'esquerre
    axes[0].bar(home_distribution["Goals"], home_distribution["Matches"])
    # Títol i etiquetes per l'equip local
    axes[0].set_title("Home Team Goals Distribution")
    axes[0].set_xlabel("Goals")
    axes[0].set_ylabel("Matches")
    # Gràfica per l'equip visitant, el de la dreta
    axes[1].bar(away_distribution["Goals"], away_distribution["Matches"])
    # Titol i etiquetes per l'equip visitant
    axes[1].set_title("Away Team Goals Distribution")
    axes[1].set_xlabel("Goals")
    axes[1].set_ylabel("Matches")
    # Ajustem espais entre gràfiques
    plt.tight_layout()
    # Guardem la figura com indica l'enunciat
    plt.savefig(f"img/grafica_ex3_{config.nom_alumne}_{config.date_time}.png")
    # Mostrem la figura
    plt.show()

