# Primer exercici
# Importem pandas
import pandas as pd
# Importem matplotlib
import matplotlib.pyplot as plt
# Importem informació de l'arxiu config.py
import config

# Definim la funció load_and_eda
def load_and_eda(file: str) -> pd.DataFrame:
    """
    Load dataset and perform EDA.
    """
    # Carreguem dataset
    data = pd.read_csv(file)
    # Com diu l'enunciat, borrem les columes HTHG, HTAG i HTR
    data = data.drop(columns=["HTHG", "HTAG", "HTR"])
    # Mostrem les primeres files del dataset
    print(data.head())
    # Mostrem les últimes files del dataset
    print(data.tail())
    # Mostrem informació del dataset
    data.info()
    # Mostrem una descripció del dataset
    print(data.describe())
    # Retornem el dataset modificat
    return data


# Funció pels dos plots. Gols pels equips de casa i pels de fora
def plot_home_away_goals(data: pd.DataFrame) -> None:
    """
    Plot home and away goals distribution.
    """
    # Primer creem la figura i els eixos. 2 plots amb 1 fila i 2 columnes
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    # Primer el boxplot dels gols dels equips de casa
    axes[0].boxplot(data["FTHG"], tick_labels=["Home Goals"]) # axes[0] és el plot de la 1a posició
    axes[0].set_title("Home Goals")
    axes[0].set_ylabel("Goals")
    # Segon boxplot, amb els gols dels equips de fora
    axes[1].boxplot(data["FTAG"], tick_labels=["Away Goals"]) # axes[1] plot en la 2a posició
    axes[1].set_title("Away Goals")
    axes[1].set_ylabel("Goals")
    # Ajustem espais i evitem solapació en etiquetes
    plt.tight_layout()
    # Guardem el plot amb el nom de l'alumne i la data actual
    plt.savefig(f"img/grafica_ex1_{config.nom_alumne}_{config.date_time}.png")
    # Mostrem el plot
    plt.show()


# Així, permetem reutilitzar i cridar les funcions i no tot l'arxiu en altres llocs, i també
# permetem que el codi només s'executi quan executem aquest arxiu directament, i no quan importem les funcions en altres arxius
if __name__ == "__main__":
    data = load_and_eda("data/LaLiga_Matches.csv")
    plot_home_away_goals(data)

