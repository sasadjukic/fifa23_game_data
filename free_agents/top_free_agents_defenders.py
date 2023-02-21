

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from data import find_free_agents

free_agents = find_free_agents()

DEFENSE = ['LB', 'LWB', 'LCB', 'CB', 'RCB', 'RWB', 'RB'] 
defenders = free_agents[free_agents['best position'].isin(DEFENSE)]

def find_average_defenders_fa() -> int:
    average_skill_fa_defenders = int(round(defenders['overall'].median(), 0))
    return average_skill_fa_defenders

def find_top_defenders() -> pd.DataFrame:
    best_defenders = defenders[defenders['overall'] > 74]
    return best_defenders

def display_top_defending_fa(defenders: pd.DataFrame, avg_skill: int) -> None:

    top_players = defenders['known as'].tolist()
    top_skill = defenders['overall'].tolist()
    averages = avg_skill 
    colors = ['#20262E', '#F9F54B']

    x = np.arange(len(top_players))
    width = 0.35

    fig, ax = plt.subplots()

    top_defenders = ax.bar(
                           x + width/2,
                           top_skill,
                           width,
                           label = 'Top Defending Free Agents',
                           color = colors[0]
                          )

    avg_defenders = ax.bar(
                           x - width/2,
                           averages,
                           width,
                           label = 'Average Defending Free Agents',
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
                 'TOP DEFENDING FREE AGENTS',
                 fontname='Calibri',
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
    ax.bar_label(top_defenders)
    ax.bar_label(avg_defenders)
    plt.ylim(60, 80)

    plt.legend()
    plt.show()

averages = find_average_defenders_fa()
top_defenders = find_top_defenders()
display_top_defending_fa(top_defenders, averages)
