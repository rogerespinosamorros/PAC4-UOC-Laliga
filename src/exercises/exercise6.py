# Importem les llibreries que utilitzarem
import pandas as pd
import matplotlib.pyplot as plt
# Importem arxiu de configuració
import config
# Importem la funció de l'exercici1, de la càrrega de dades
from src.exercises.exercise1 import load_and_eda
# També necessitarem la funció fun_total_points de l'exercici5 i també add_points
from src.exercises.exercise5 import fun_total_points, add_points

# Definim la funció fun_total_goals
def fun_total_goals(data: pd.DataFrame) -> tuple[int, int, int]:
    """
    Calculate home, away and total goals.
    """
    # Definim què són els gols a casa
    home_goals = data["FTHG"].sum()
    # Definim què són els gols a fora
    away_goals = data["FTAG"].sum()
    # Calculem els gols totals
    total_goals = home_goals + away_goals
    # Retornem els gols a casa, els gols a fora i els gols totals
    return home_goals, away_goals, total_goals

# Definim la funció fun_total_goals_by_team
def fun_total_goals_by_team(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Calculate home, away and totals goals by team.
    """
    # Hem d'agrupar per equips locals i sumar els gols que s'han marcat a casa
    team_home_goals = (data.groupby("HomeTeam")["FTHG"].sum().reset_index())
    # Agrupar per equip a casa i sumem els gols, creem df amb reset_index i a continuació donarem nom a les columnes
    team_home_goals.columns = ["Team", "Home_Goals"]
    # Aquí igual que amb els gols fets a casa
    team_away_goals = (data.groupby("AwayTeam")["FTAG"].sum().reset_index())
    # Hem de tornar a renombrar les columnes dels gols marcats a fora
    team_away_goals.columns = ["Team", "Away_Goals"]
    # Calculem els gols totals. No funciona simplemente sumant, em donava error i poso les operacions completes
    team_total_goals = (data.groupby("HomeTeam")["FTHG"].sum() + data.groupby("AwayTeam")["FTAG"].sum())
    # Hem d'ordenar de més gols a menys i resetejar índexs per crear el dataframe
    team_total_goals = (team_total_goals.sort_values(ascending=False).reset_index())
    # Renombrem les columnes
    team_total_goals.columns = ["Team", "Total_Goals"]
    # Retornem la funció
    return (team_home_goals, team_away_goals, team_total_goals)

# Ara definim la funció fun_summary_1996_2025
def fun_summary_1996_2025(
        total_points: pd.DataFrame, team_home_goals: pd.DataFrame, team_away_goals: pd.DataFrame, team_total_goals: pd.DataFrame
        ) -> pd.DataFrame:
    """
    A big dataframe with points and goals, from dataframes already created.
    """
    # Utilitzarem la funció merge(), que permet combinar dataframes a partir de la mateixa columna (si la tenen)
    summary_1996_2025 = total_points.merge(team_home_goals, on="Team") # "Team" és comú en tots els dfs
    # Un cop tenim el primer df combinat, afegim els altres a partir de la columna "Team"
    summary_1996_2025 = summary_1996_2025.merge(team_away_goals, on="Team")

    summary_1996_2025 = summary_1996_2025.merge(team_total_goals, on="Team")
    # Retornem el df final
    return summary_1996_2025

# Finalment la funció podium, per veure els 3 millors equips històricament (1995-2025)
def podium(summary_1996_2025: pd.DataFrame) -> None:
    """
    Plot historical top three teams in a podium.
    """
    # Definim primer quin és el top3 equips
    top3 = summary_1996_2025.head(3)
    # Hem d'extreure els noms dels tres primers equips
    best = top3.iloc[0]["Team"]
    second_best = top3.iloc[1]["Team"]
    third_best = top3.iloc[2]["Team"]
    # Definim les posicions dels equips
    positions = [0, 1, 2]
    # Definim les altures però imaginant-nos que és un podi, on el punt més alt és la posició central
    heights = [2, 3, 1] # El '3' és el punt més alt, a l'esquerre quedarà el segon més alt
    # Creem la figura
    plt.figure(figsize=(10,5))
    # Fem el gràfic de barres amb les posicions i altures que hem definit
    plt.bar(positions, heights)
    # Hem d'establir la posició del text, utilitzant les posicions i altures
    # Text del segon en el podi
    plt.text(
        0,  # Posició
        2.05,  # Altura
        second_best, # El segon millor que hem definit
        ha="center"  # Centra el nom de l'equip
    )
    # Text del primer en el podi
    plt.text(
        1,  # Posició
        3.05,  # Altura
        best,  # El primer en el podi, definit anteriorment
        ha="center"  
    )
    # Text del tercer
    plt.text(
        2,
        1.05,  # L'altura com veiem, és una mica més que on arribarà la barra del plot
        third_best,
        ha="center"
    )
    # L'enunciat diu que no hi ha d'haver etiquetes en els eixos
    plt.xticks([]) # Etiquetes buïdes
    plt.yticks([])
    # Títol del gràfic
    plt.title("La Liga Podium")
    # Guardem el gràfic a img
    plt.savefig(f"img/grafica_ex6_{config.nom_alumne}_{config.date_time}.png")
    # Mostrem el gràfic
    plt.show()







# Així, permetem reutilitzar i cridar les funcions i no tot l'arxiu en altres llocs, i també
# permetem que el codi només s'executi quan executem aquest arxiu directament, i no quan importem les funcions en altres arxius
if __name__ == "__main__":
    # Carreguem el dataset
    data = load_and_eda("data/LaLiga_Matches.csv")
    # Apliquem la funció add_points de l'exercici 5 (error anterior)
    data = add_points(data)
    # Funció fun_total_goals
    home_goals, away_goals, total_goals = fun_total_goals(data)

    print(f"Home goals: {home_goals}")
    print(f"Away goals: {away_goals}")
    print(f"Total goals: {total_goals}")

    # Funció fun_total_goals_by_team
    (team_home_goals, team_away_goals, total_goals_by_team) = fun_total_goals_by_team(data)
    print(total_goals_by_team.head(10))

    # Hem de cridar la funció fun_total_points de l'exercici 5 per crear el summary
    total_points, df_total_points = (fun_total_points(data))
    # Funció fun_summary_1996_2025
    summary_1996_2025 = fun_summary_1996_2025(
        df_total_points,
        team_home_goals,
        team_away_goals,
        total_goals_by_team
    )
    print(summary_1996_2025.head(10))

    # Funció podium
    podium(summary_1996_2025)




