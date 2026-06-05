# Primer de tot fem els imports que es necessitin, aquí llibreries
import pandas as pd
import matplotlib.pyplot as plt
# Funcions necessàries de l'arxiu config.py
import config
from src.exercises.exercise1 import load_and_eda

# Definim la funció on tindrem els partits guanyats a casa, a fora i els empats
def FTR(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate wins at home, away and draws.
    """
    # Anem a comprobar els resultats totals que hi ha
    ftr = data["FTR"].value_counts()
    # Convertim a dataframe reiniciant els índexs
    ftr = ftr.reset_index()
    # Donem nom a les columnes
    ftr.columns = ["Result", "Matches"]
    # Retornem el resultat de la funció
    return ftr

# Definim la funció del plot FTR
def plot_FTR(ftr: pd.DataFrame) -> None:
    """
    Plot full time results distribution.
    """
    # Definim la figura primer
    plt.figure(figsize=(10, 6))
    # Definim el gràfic de barres amb els resultats i partits
    plt.bar(ftr["Result"], ftr["Matches"])
    # Definim el títol i les etiquetes
    plt.title("Full Time Results")
    plt.xlabel("Result")
    plt.ylabel("Matches")
    # Ajustem les etiquetes i el layout
    plt.tight_layout()
    # Guardem l'imatge a /img com en els anteriors exercicis
    plt.savefig(f"img/grafica_ex4_{config.nom_alumne}_{config.date_time}.png")
    # Mostrem el gràfic
    plt.show()

# Així, permetem reutilitzar i cridar les funcions i no tot l'arxiu en altres llocs, i també
# permetem que el codi només s'executi quan executem aquest arxiu directament, i no quan importem les funcions en altres arxius
if __name__ == "__main__":
    # Carreguem el dataset
    data = load_and_eda("data/LaLiga_Matches.csv")
    # Funció FTR
    ftr = FTR(data)
    # Anem a comprovar el percentatge de victòries a casa
    # Obtenim les files de partits jugats a casa, i agafem el primer element de la fila (que és H)
    wins_at_home = ftr.loc[ftr["Result"] == "H", "Matches"].iloc[0]
    # Contem els partits totals jugats
    total_matches = ftr["Matches"].sum()
    # Calculem el percentatge
    wins_home_percentage = (wins_at_home / total_matches) * 100
    # Imprimim el percentatge
    print(f"Home win percentage: {wins_home_percentage:.2f}%")
    # Mostrem el gràfic de la funció plot_FTR
    plot_FTR(ftr)
