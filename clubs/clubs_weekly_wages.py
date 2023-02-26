

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data import get_clean_data

fifa_23 = get_clean_data()

def find_all_wages() -> dict[str:int]:

    all_teams = {}
    for club in fifa_23['club']:
        team = fifa_23[fifa_23['club'] == club]
        wages = team['wage'].tolist()
        all_teams[club] = sum(wages)

    return all_teams

def find_top_wages(t_wages: dict[str:int]) -> pd.Series:

    top_wages = pd.Series(t_wages).nlargest(n=10)
    return top_wages 

def find_average_wages(t_wages: dict[str:int]) -> int:

    avg_wages = int(round(pd.Series(t_wages).mean() / 1_000, 0))
    return avg_wages

def display_top_team_wages(teams: pd.Series, avg_wages: int) -> None:

    top_teams = teams.index.tolist()
    top_wages = [int(round(v / 1_000, 0)) for v in teams.values]
    averages = avg_wages 
    colors = ['#222831', '#FFE227']

    x = np.arange(len(top_teams))
    width = 0.35

    fig, ax = plt.subplots()

    top_wages = ax.bar(
                        x + width / 2,
                        top_wages,
                        width,
                        label = 'Highest Weekly Wages',
                        color = colors[0]
                      )

    average_wages = ax.bar(
                            x - width / 2,
                            averages,
                            width,
                            label = 'Average Weekly Wages',
                            color = colors[1]
                           )

    ax.set_xlabel(
                  'TOP SPENDING CLUBS',
                  fontname = 'Calibri',
                  fontsize = 15
                 )

    ax.set_ylabel(
                  'WEEKLY WAGES IN EUROS (in thousands)',
                  fontname = 'Calibri',
                  fontsize = 15
                 )

    plt.suptitle(
                 'HIGHEST vs AVERAGE WEEKLY WAGES IN FOOTBALL(SOCCER)',
                 fontname = 'Calibri',
                 fontsize = 18,
                 fontweight = 'bold'
                )

    plt.title(
              '*EA Sports FIFA 23',
              fontname = 'Calibri',
              fontsize = 8
             )

    ax.set_xticks(x, top_teams)
    ax.bar_label(top_wages)
    ax.bar_label(average_wages)

    plt.legend()
    plt.show()

team_wages = find_all_wages()
avg_wages = find_average_wages(team_wages)
top_wages = find_top_wages(team_wages)
display_top_team_wages(top_wages, avg_wages)