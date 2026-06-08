"""
Primer exercici. Càrrega dataset i anàlisis exploratori.
"""
# Importem llibreries primer de tot
import pandas as pd
import matplotlib.pyplot as plt
# Importem l'arxiu de configuració
from src import config
# Definim la primera funció de l'exercici load_and_eda
def load_and_eda(file: str) -> pd.DataFrame:
    """
    Load dataset from a file and perform an EDA.
    """
    # Primer carreguem dataset amb .read_csv
    data = pd.read_csv(file)
    # Seguim l'enunciat i borrem les columnes HTHG, HTAG i HTR
    data = data.drop(columns=["HTHG", "HTAG", "HTR"])
    # Mostrem les primeres files del dataset
    print(data.head())
    # Mostrem les últimes files del dataset
    print(data.tail())
    # Veiem informació del dataset
    data.info()
    # Mostrem la descripció del dataset
    print(data.describe())
    # Retornem el dataset
    return data

# La funció dels gràfics o plots. Un pels gols dels equips de casa i un pels de fora
def plot_home_away_goals(data: pd.DataFrame) -> None:
    """
    Plot home and away goals distribution.
    """
    # Primer de tot, creem la figura i els eixos, 2 plots amb 1 fila i 2 columnes
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    # Hem de fer un boxplot dels gols dels equips de casa
    axes[0].boxplot(data["FTHG"], tick_labels=["Home Goals"]) # axes[0] és el plot de la 1a posició
    axes[0].set_title("Home Goals")
    axes[0].set_ylabel("Goals")
    # Segon boxplot, amb els gols dels equips de fora
    axes[1].boxplot(data["FTAG"], tick_labels=["Away Goals"]) # axes[1] plot en la 2a posició 
    axes[1].set_title("Away Goals")
    axes[1].set_ylabel("Goals")
    # Ajustem espais i evitem que les etiquetes es solapin
    plt.tight_layout()
    # Guardem el gràfic amb el nom de l'alumne i la data a la carpeta /img
    plt.savefig(f"img/grafica_ex1_{config.nom_alumne}_{config.date_time}.png")
    # Mostrem el plot
    plt.show()