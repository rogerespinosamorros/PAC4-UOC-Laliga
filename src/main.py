"""
Main file to execute all PAC4 exercises.
"""
# Utilitzarem argparse que tenia algun coneixement anteriorment.
# La documentació oficial de python argparse, crec que és més robust i manipulable que sys
import argparse
from exercises.exercise1 import(load_and_eda, plot_home_away_goals)
from exercises.exercise2 import(total_matches, plot_matches_team_total)
from exercises.exercise3 import(goals_distribution, plot_goals_distribution)
from exercises.exercise4 import(FTR, plot_FTR)
from exercises.exercise5 import(add_points, fun_total_points, alltime_winner)
from exercises.exercise6 import(
    fun_total_goals, fun_total_goals_by_team, fun_summary_1996_2025, podium
    )
from exercises.exercise7 import(graf)


# Definim un 'parser', amb argument 'ArgumentParser' que s'encarrega d'interpretar els comandos de la terminal
# 'description' és un text que apareixerà, és informatiu simplement.
parser = argparse.ArgumentParser(description="Execute exercises PAC4")
# Afegirem un argument que demana la PAC, que és executar un exercici i els anteriors a aquests ("--ex")
parser.add_argument(
    "--ex",
    type=int, # després de '--ex' s'ha d'escriure un nombre enter que farà referència al número de l'exercici
    help="Execute exercises from 1 to 7" # Missatge que apareixerà a la terminal
)
# 'parse_args' llegeix els arguments que hem escrit a la terminal (exemple --help) i els processa
args = parser.parse_args()
# Ara definim la lògica del loop que seguirà l'execució dels exercicis
if args.ex is None: # Si no li diem quin exercici volem en concret, executarà els 7 exercicis
    ex = 7
else:
    ex = args.ex # Aquí executarà l'exercici que li diem i els anteriors



# Execucions de les funcions dels exercicis
# Execucions exercici 1, funció load_and_eda
# Càrrega del dataset sempre en un inici fora de l'execució de l'exercici 1
data = load_and_eda("data/LaLiga_Matches.csv")
# Si escrivim a la terminal --ex 1, executarà l'exercici 1
if ex >= 1:
    print(data.head())
    # Funció plot_home_away_goals
    plot_home_away_goals(data)


# Si escrivim a la terminal --ex 2, executarà l'exercici 2 i anteriors
if ex >= 2:
    # Execucions exercici 2, funció total_matches
    total_matches_by_team = total_matches(data)
    print("\nTotal matches by team:") # Li donem estètica al resultat, \n és un salt de línia
    print(total_matches_by_team.head(10))
    # Mostrem equips sempre a 1a divisió
    maxim_matches = total_matches_by_team["Total_Matches"].max()
    always_in_first_division = total_matches_by_team[total_matches_by_team["Total_Matches"] == maxim_matches]
    print("\nTeams always in first division:") # Li donem estètica al resultat, \n és un salt de línia
    print(always_in_first_division)
    # Funció plot_matches_team_total
    plot_matches_team_total(total_matches_by_team)


# Si escrivim a la terminal --ex 3, executarà l'exercici 3 i anteriors
if ex >= 3:
    # Execucions exercici 3, funció goals_distribution
    home_distribution, away_distribution = goals_distribution(data)
    print("\nGoals distribution by Home teams") # Li donem estètica al resultat, \n és un salt de línia
    print(home_distribution)
    print("\nGoals distribution by Away teams") # Li donem estètica al resultat, \n és un salt de línia
    print(away_distribution)
    # Funció plot_goals_distribution
    plot_goals_distribution(home_distribution, away_distribution)



# Si escrivim a la terminal --ex 4, executarà l'exercici 4 i anteriors
if ex >= 4:
    # Execucions exercici 4, funció FTR
    ftr = FTR(data)
    print("\nFull time results") # Li donem estètica al resultat, \n és un salt de línia
    print(ftr)
    # Percentatge de victòries a casa
    wins_at_home = ftr.loc[ftr["Result"] == "H", "Matches"].iloc[0]
    total_matches_ftr = ftr["Matches"].sum()
    wins_at_home_percentage = (wins_at_home / total_matches_ftr) * 100
    print(f"Wins at home percentage: {wins_at_home_percentage:.2f}%") # .2f arrodoneix a 2 decimals
    # Funció plot_FTR
    plot_FTR(ftr)



# Si escrivim a la terminal --ex 5, executarà l'exercici 5 i anteriors
if ex >= 5:
    # Execucions exercici 5, funció add_points
    data_with_team_points = add_points(data)
    # Hem de mostrar els 10 primers valors
    print(data_with_team_points[["HomeTeam", "AwayTeam", "FTR", "points_home", "points_away"]].head(10))
    # Funció fun_total_points
    total_points, df_total_points = fun_total_points(data_with_team_points)
    print("\nTotal points accumulated")
    print(df_total_points.head(10))
    # Funció alltime_winner
    winner = alltime_winner(df_total_points)
    print(f"Most accumulated points by a team is: {winner}")



# Si escrivim a la terminal --ex 6, executarà l'exercici 6 i anteriors
if ex >= 6:
    # Execucions exercici 6, funció fun_total_goals
    home_goals, away_goals, total_goals = fun_total_goals(data)
    print(f"Home goals: {home_goals}")
    print(f"Away goals: {away_goals}")
    print(f"Total goals: {total_goals}")
    # Funció fun_total_goals_by_team
    team_home_goals, team_away_goals, total_goals_by_team = fun_total_goals_by_team(data)
    print("\nTotal goals by team")
    print(total_goals_by_team.head(10))
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




# Si escrivim a la terminal --ex 7, executarà l'exercici 7 i anteriors
if ex >= 7:
    # Execucions exercici 7, funció graf
    five_teams_selected = [
        "Barcelona",
        "Real Madrid",
        "Ath Madrid",
        "Valencia",
        "Ath Bilbao"
    ]

    graf(data, five_teams_selected)
