

import pandas as pd
import  numpy as np 
import matplotlib.pyplot as plt
from data import find_free_agents

free_agents = find_free_agents()

MIDFIELD = ['LM', 'LCM', 'CM', 'DM', 'CAM', 'RCM', 'RM']
midfielders = free_agents[free_agents['best position'].isin(MIDFIELD)]

def find_average_midfield() -> int:
    average_skill_fa_midfielders = int(round(midfielders['overall'].median(), 0))
    return average_skill_fa_midfielders

def find_top_midfield() -> pd.DataFrame:
    best_midfielders = midfielders[midfielders['overall'] > 74]
    return best_midfielders

def display_top_midfielders(midfielders: pd.DataFrame, avg_skill: int)  -> None:

    top_players = midfielders['known as'].tolist()
    top_skill = midfielders['overall'].tolist()
    averages = avg_skill
    colors = ['#645CBB', '#F9F54B']

    x = np.arange(len(top_players))
    width = 0.35

    fig, ax = plt.subplots()

    top_midfield = ax.bar(
                          x + width/2,
                          top_skill,
                          width,
                          label = 'Top Midfield Free Agents',
                          color = colors[0]
                         )

    avg_midfield = ax.bar(
                          x - width/2,
                          averages,
                          width,
                          label = 'Average Midfield Free Agents',
                          color = colors[1]
                         )

    ax.set_ylabel(
                  'SKILL LEVEL',    
                  fontname = 'Calibri',
                  fontsize = 15
                 )

    ax.set_xlabel(
                  'FREE AGENTS',
                  fontname = 'Calibri',
                  fontsize = 15
                 )

    plt.suptitle(
                 'TOP MIDFIELD FREE AGENTS',
                 fontname = 'Calibri',
                 fontsize = 18,
                 fontweight = 'bold'
                )

    plt.title(
              '*EA Sports FIFA 23',
              fontname = 'Calibri',
              fontsize = 8
             )

    ax.set_xticks(x, top_players)
    ax.set_yticks([60, 65, 70, 75, 80])
    ax.bar_label(top_midfield)
    ax.bar_label(avg_midfield)
    plt.ylim(60, 80)

    plt.legend()
    plt.show()

average_skills = find_average_midfield() 
top_midfielders = find_top_midfield()
display_top_midfielders(top_midfielders, average_skills)