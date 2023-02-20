

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from data import find_free_agents

free_agents = find_free_agents()

def find_average_free_agents() -> int:
    average_skill = int(round(free_agents['overall'].mean(), 0))
    return average_skill

def find_top_free_agents() -> pd.DataFrame:
    top_free_agents = free_agents[free_agents['overall'] > 76]
    return top_free_agents

def display_top_free_agents(top_free_agents: pd.DataFrame, avg_free_agents: int) -> None:

    free_agents = top_free_agents['known as'].tolist()
    skill = top_free_agents['overall'].tolist()
    average_skill = avg_free_agents
    colors = ['#8BF5FA', '#F9F54B']

    x = np.arange(len(free_agents))
    width = 0.35

    fig, ax = plt.subplots()
    
    top_players = ax.bar(
                          x + width/2,
                          skill,
                          width,
                          label = 'Top Free Agents Skill',
                          color = colors[0]
                        ) 

    avg_players = ax.bar(
                         x - width/2,
                         average_skill,
                         width,
                         label = 'Free Agents Average Skill',
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
                 'TOP FREE AGENTS OVERALL',
                 fontname = 'Calibri',
                 fontsize = 18,
                 fontweight = 'bold'
                )

    plt.title(
              '*EA Sports FIFA 23',
              fontname = 'Calibri',
              fontsize = 8
             )

    ax.set_xticks(x, free_agents)
    ax.bar_label(avg_players)
    ax.bar_label(top_players)
    plt.ylim(60, 85)

    plt.legend()
    plt.show()

avg_skill = find_average_free_agents()
top_fas = find_top_free_agents()
display_top_free_agents(top_fas, avg_skill)