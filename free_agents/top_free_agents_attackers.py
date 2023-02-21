

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from data import find_free_agents

free_agents = find_free_agents()

ATTACK = ['RW', 'RF', 'CF', 'ST', 'LF', 'LW']
attackers = free_agents[free_agents['best position'].isin(ATTACK)]

def find_average_attackers_fa() -> int:
    average_skill_fa_attackers = int(round(attackers['overall'].median(), 0))
    return average_skill_fa_attackers

def find_top_free_agents_attackers() -> pd.DataFrame:

    best_attackers = attackers[attackers['overall'] >= 70]
    return best_attackers

def display_top_attackers_fa(attackers: pd.DataFrame, avg_skill: int) -> None:

    players = attackers['known as'].tolist()
    top_skill = attackers['overall'].tolist()
    averages = avg_skill
    colors = ['#D61355', '#F9F54B']

    width = 0.35
    x = np.arange(len(players))

    fig, ax = plt.subplots()

    top_attackers = ax.bar(
                           x + width/2,
                           top_skill,
                           width,
                           label = 'Top Attacking Free Agents',
                           color = colors[0]
                          )

    avg_attackers = ax.bar(
                           x - width/2,
                           averages,
                           width,
                           label = 'Average Attacking Free Agents',
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
                 'TOP ATTACKING FREE AGENTS',
                 fontname = 'Calibri',
                 fontsize = 18,
                 fontweight = 'bold'
                )

    plt.title(
              '*EA Sports FIFA 23',
              fontname = 'Calibri',
              fontsize = 8
             )

    ax.set_xticks(x, players)
    ax.set_yticks([60, 65, 70, 75, 80])
    ax.bar_label(avg_attackers)
    ax.bar_label(top_attackers)
    plt.ylim(60, 80)

    plt.legend()
    plt.show()

average_att_skill = find_average_attackers_fa()
top_attacker = find_top_free_agents_attackers()
display_top_attackers_fa(top_attacker, average_att_skill)
