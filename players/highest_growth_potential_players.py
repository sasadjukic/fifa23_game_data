

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data import get_clean_data 

fifa_23 = get_clean_data()

def add_column_to_db() -> None:

    '''create a new column 'growth_potential' to store data'''

    for potential in fifa_23:
        pot = fifa_23['potential']-fifa_23['overall']
        fifa_23['growth_potential'] = pot

def find_highest_growth_players() -> dict[str:int]:

    hg_players = {}
    for g in fifa_23.index:
        player = fifa_23.loc[g, 'known as']
        growth = fifa_23.loc[g, 'growth_potential']
        hg_players[player] = growth

    return hg_players

def find_average_players_potential() -> int:

    potential_avg = int(round(fifa_23['growth_potential'].mean(), 0))
    return potential_avg

def display_hgp_players(
                        hgp_players: dict[str:int], 
                        avg_pot: int
                        ) -> None:

    players = [k for k, v in hgp_players.items() if v >= 25]
    values = [v for k, v in hgp_players.items() if v >= 25]
    avg_potential = [avg_pot for x in players]
    colors = ['#645CBB', '#D61355']
 
    width = 0.35
    x = np.arange(len(players))

    fig, ax = plt.subplots()

    hg_players = ax.bar(
                        x + width/2,
                        values,
                        width,
                        label = 'Top Player Growth',
                        color = colors[1]
                    )

    avg_players = ax.bar( 
                 x - width/2,
                 avg_potential,
                 width,
                 label = 'Average Player Growth',
                 color = colors[0]
                )

    ax.set_ylabel(
                  'POTENTIAL PLAYER GROWTH',
                  fontname='Calibri', 
                  fontsize=15
                  )

    ax.set_xlabel(
                  'PLAYERS WITH THE HIGHEST POTENTIAL', 
                  fontname='Calibri',
                  fontsize=15
                  )

    plt.suptitle(
                 'PLAYERS WITH THE HIGHEST POTENTIAL GROWTH', 
                 fontname='Calibri', 
                 fontsize=18, 
                 fontweight='bold'
                 )

    plt.title(
              '*current skill subtracted from their potential', 
              fontname='Calibri'
              )

    ax.set_xticks(x, players)
    ax.bar_label(avg_players)
    ax.bar_label(hg_players)
    plt.ylim(0, 30)

    ax.legend()
    plt.show()


add_column_to_db()
hg_players = find_highest_growth_players()
avg_potential = find_average_players_potential()
display_hgp_players(hg_players, avg_potential)
