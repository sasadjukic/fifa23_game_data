

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data import get_clean_data

fifa_23 = get_clean_data()

def find_all_team_values() -> dict[str:int]:

    all_team_values = {}
    for club in fifa_23['club']:
        team = fifa_23[fifa_23['club'] == club]
        values = team['value'].tolist()
        all_team_values[club] = sum(values)
    
    return all_team_values 

def find_top_clubs_values(all_team_values: dict[str:int]) -> pd.Series:

    all_values = pd.Series(all_team_values).nlargest(n=10)
    return all_values

def find_average_club_values(all_team_values: dict[str:int]) -> int:

    avg_values = int(round(pd.Series(all_team_values).mean() / 1_000_000, 0))
    return avg_values

def display_top_team_values(teams: pd.Series, avg_values: int) -> None:

    top_teams = teams.index.tolist()
    top_values = [int(round(v / 1_000_000, 0)) for v in teams.values]
    average_values = avg_values
    colors = ['#170055', '#16FF00']

    width = 0.35
    x = np.arange(len(top_teams))
    
    fig, ax = plt.subplots()
    
    best_teams = ax.bar(
                       x + width / 2,
                       top_values,
                       width,
                       label = 'Top Team Roster Values',
                       color = colors[0]
                      )

    avg_teams = ax.bar(
                        x - width / 2,
                        average_values,
                        width, 
                        label = 'Average Team Roster Values',
                        color = colors[1]
                       )

    plt.suptitle(
                 'HIGHEST vs AVERAGE ROSTER VALUES IN FOOTBALL (SOCCER)',
                 fontname = 'Calibri',
                 fontsize = 18,
                 fontweight = 'bold'
                )

    plt.title(
              '*EA Sports FIFA 23',
              fontname = 'Calibri',
              fontsize = 8
             )

    ax.set_ylabel(
               'ROSTER VALUES IN EUROS (in Millions)',
               fontname = 'Calibri',
               fontsize = 15
               )

    ax.set_xlabel(
               'TOP CLUBS',
               fontname = 'Calibri',
               fontsize = 15
              )   

    ax.set_xticks(x, top_teams)
    ax.bar_label(avg_teams)
    ax.bar_label(best_teams)

    plt.legend()
    plt.show()
    
team_values = find_all_team_values()
avg_team_values = find_average_club_values(team_values)
top_team_values = find_top_clubs_values(team_values)
display_top_team_values(top_team_values, avg_team_values)