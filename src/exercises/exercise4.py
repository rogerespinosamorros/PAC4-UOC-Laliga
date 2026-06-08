"""
Quart exercici. Partits guanyats pels equips de casa i de fora.
"""
# Primer de tot fem els imports que es necessitin, aquí llibreries
import pandas as pd
import matplotlib.pyplot as plt
# Funcions necessàries de l'arxiu config.py
from src import config

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

