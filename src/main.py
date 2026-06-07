# Execucions de les funcions dels exercicis

# Exercici 1
from exercises.exercise1 import(load_and_eda, plot_home_away_goals)
# Execucions exercici 1, funció load_and_eda
data = load_and_eda("data/LaLiga_Matches.csv")
print(data.head())
# Funció plot_home_away_goals
plot_home_away_goals(data)


# Exercici 2
from exercises.exercise2 import(total_matches, plot_matches_team_total)
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


# Exercici 3
from exercises.exercise3 import(goals_distribution, plot_goals_distribution)
# Execucions exercici 3, funció goals_distribution
home_distribution, away_distribution = goals_distribution(data)
print("\nGoals distribution by Home teams") # Li donem estètica al resultat, \n és un salt de línia
print(home_distribution)
print("\nGoals distribution by Away teams") # Li donem estètica al resultat, \n és un salt de línia
print(away_distribution)
# Funció plot_goals_distribution
plot_goals_distribution(home_distribution, away_distribution)



# Exercici 4
from exercises.exercise4 import(FTR, plot_FTR)
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



# Exercici 5
from exercises.exercise5 import(add_points, fun_total_points, alltime_winner)
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



# Exercici 6
from exercises.exercise6 import(fun_total_goals, fun_total_goals_by_team, fun_summary_1996_2025, podium)
# Execucions exercici 6, funció fun_total_goals
home_goals, away_goals, total_goals = fun_total_goals(data)
print(f"Home goals: {home_goals}")
print(f"Away goals: {away_goals}")
print(f"Total goals: {total_goals}")
# Funció fun_total_goals_by_team
team_home_goals, team_away_goals, total_goals_by_team = (fun_total_goals_by_team(data))
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



# Exercici 7
from exercises.exercise7 import(graf)
# Execucions exercici 7, funció graf
five_teams_selected = [
    "Barcelona",
    "Real Madrid",
    "Ath Madrid",
    "Valencia",
    "Ath Bilbao"
]

graf(data, five_teams_selected)