

import pandas as pd 
import matplotlib.pyplot as plt
from positions import (
                        find_defenders,
                        find_midfielders,
                        find_attackers,
                        find_keepers
                       )

def find_defenders_averages() -> int:
    all_defenders = find_defenders()
    defenders_avg = int(round(all_defenders['wage'].mean(), 0))
    return defenders_avg

def find_midfielders_averages() -> int:
    all_midfielders = find_midfielders()
    midfielders_avg = int(round(all_midfielders['wage'].mean(), 0))
    return midfielders_avg

def find_attackers_averages() -> int:
    all_attackers = find_attackers()
    attackers_avg = int(round(all_attackers['wage'].mean(), 0))
    return attackers_avg

def find_keepers_averages() -> int:
    all_keepers = find_keepers()
    keepers_avg = int(round(all_keepers['wage'].mean(), 0))
    return keepers_avg

def get_average_wage_by_positions(
                                  defenders: int,
                                  midfielders: int,
                                  attackers: int,
                                  keepers: int
                                  ) -> None:

    positions = [
                 'GOALKEEPERS', 
                 'DEFENDERS', 
                 'MIDFIELDERS', 
                 'ATTACKERS'
                 ]

    average_wages = [
                     keepers, 
                     defenders, 
                     midfielders, 
                     attackers
                     ]

    colors = [
              '#FF6E31', 
              '#243763', 
              '#FFDB89', 
              '#EB455F'
              ]

    fig, ax = plt.subplots()

    ax.bar(
           positions, 
           average_wages, 
           color=colors
           )

    ax.set_ylabel(
                  'AVERAGE WEEKLY WAGES', 
                  fontsize=15, 
                  fontname='Calibri'
                  )

    ax.set_xlabel(
                  'POSITIONS', 
                  fontsize=15, 
                  fontname='Calibri'
                  )

    plt.suptitle(
                 'AVERAGE WEEKLY WAGES OF PLAYERS (BY POSITIONS) IN EUROS', 
                 fontsize=18, 
                 fontname='Calibri', 
                 fontweight='bold'
                 )

    plt.title('*EA Sports FIFA 23', fontname='Calibri')
    plt.ylim(0, 12_000)

    for index, value in enumerate(average_wages):
        plt.text(
                 index, 
                 value, 
                 str(value), 
                 fontsize=15, 
                 position=(index-0.1, value+100)
                 )

    plt.show()

defenders_avg = find_defenders_averages()
midfielders_avg = find_midfielders_averages()
attackers_avg = find_attackers_averages()
keepers_avg = find_keepers_averages()
get_average_wage_by_positions(defenders_avg, midfielders_avg, attackers_avg, keepers_avg)
