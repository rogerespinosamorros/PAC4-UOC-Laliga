"""
Cinquè exercici. Càlcul dels punts aconseguits per cada equip.
"""
# Fem les importacions necesàrries, llibreries primer
import pandas as pd


# Definim la funció add_points
def add_points(data: pd.DataFrame) -> pd.DataFrame:
    """
    Add home and away points according to the match result.
    """
    # Necessitem els punts guanyats a casa, per tant necessitarem un dict, ja que volem la clau i el valor
    home_points = {
        "H": 3,  # Guanyes 3 punts
        "D": 1,  # Empates és 1 punt
        "A": 0   # Perds sumes 0 punts
    }
    # Punts guanyats per l'equip de fora de casa
    away_points = {
        "H": 0,  # 0 punts
        "D": 1,  # Empat és 1 punt
        "A": 3,  # Guanyes a fora 3 punts
    }

    # Ara hem d'afegir noves columnes amb aquests dicts definits
    data["points_home"] = data["FTR"].map(home_points) # el .map() agafa el valor numèric en aquest cas
    data["points_away"] = data["FTR"].map(away_points)
    # Retornem la funció
    return data

# Definim la funció fun_total_points(data), que mostra el total de punts aconseguits per cada equip
def fun_total_points(data: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame]:
    """
    Calculate total accumulated points for each team between 1995-2025.
    """
    # Com que tenim els punts acumulats depenent de victòria com equip local o visitant, agrupem primer per equip local
    home_points_total = data.groupby("HomeTeam")["points_home"].sum()
    # Ara agrupem per equip visitant
    away_points_total = data.groupby("AwayTeam")["points_away"].sum()
    # Tenint els punts a casa i fora de cada equip, els hem de sumar
    total_points = home_points_total + away_points_total
    # Els volem ordenats, per tant anem a fer-ho
    total_points = total_points.sort_values(ascending=False)
    # Convertim a dataframe reininciant els índexs
    df_total_points = total_points.reset_index()
    # Renombrem el nom de les columnes
    df_total_points.columns = ["Team", "Total_Points"]
    # Tornem el df en forma de tupla, amb una variable Series i una variable df
    return total_points, df_total_points

# Funció alltime_winner que tornarà l'equip amb més punts 
def alltime_winner(df_total_points: pd.DataFrame) -> str:
    """
    Return the all time winner.
    """
    # Definim l'equip guanyador, el primer valor que trobem dins de "Team" (en aquest hem vist que és el Barça)
    winner = df_total_points.iloc[0]["Team"]
    # Retornem el guanyador
    return winner


