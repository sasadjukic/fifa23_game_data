

import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
from data import find_free_agents

free_agents = find_free_agents()
goalkeepers = free_agents[free_agents['best position'] == 'GK']

def find_average_keepers() -> int:
    average_skill_fa_goalkeepers = int(round(goalkeepers['overall'].median(), 0))
    return average_skill_fa_goalkeepers

def find_top_keepers() -> pd.DataFrame:
    best_keepers = goalkeepers[goalkeepers['overall'] > 75]
    return best_keepers

def display_top_keepers(keepers: pd.DataFrame, avg_skill: int) -> None:

    top_players = keepers['known as'].tolist()
    top_skill = keepers['overall'].tolist()
    averages = avg_skill
    colors = ['#00425A', '#F9F54B']

    x = np.arange(len(top_players)) 
    width = 0.35

    fig, ax = plt.subplots()

    top_keepers = ax.bar(
                         x + width/2,
                         top_skill,
                         width,
                         label = 'Top Goalkeeping Free Agents',
                         color = colors[0]
                        )

    avg_keepers = ax.bar(
                         x - width/2,
                         averages,
                         width,
                         label = 'Average Goalkeeping Free Agents',
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
                 'TOP GOALKEEPING FREE AGENTS',
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
    ax.set_yticks([60, 65, 70, 75, 80, 85])
    ax.bar_label(avg_keepers)
    ax.bar_label(top_keepers)
    plt.ylim(60, 85)

    plt.legend()
    plt.show()

avg_keepers = find_average_keepers()
top_keepers = find_top_keepers()
display_top_keepers(top_keepers, avg_keepers)
