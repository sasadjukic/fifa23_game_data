
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
    defenders_avg = int(round(all_defenders['value'].mean(), 0))

    return defenders_avg

def find_midfielders_averages() -> int:
    all_midfielders = find_midfielders()
    midfielders_avg = int(round(all_midfielders['value'].mean(), 0))

    return midfielders_avg

def find_attackers_averages() -> int:
    all_attackers = find_attackers()
    attackers_avg = int(round(all_attackers['value'].mean(), 0))

    return attackers_avg

def find_keepers_averages() -> int:
    all_goalkeepers = find_keepers()
    goalkeepers_avg = int(round(all_goalkeepers['value'].mean(), 0))

    return goalkeepers_avg

def get_average_value_by_position(
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

    average_values = [
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
           average_values, 
           color=colors
           )

    ax.set_ylabel(
                  'AVERAGE PLAYER VALUES', 
                  fontsize=15, 
                  fontname='Calibri'
                 )

    ax.set_xlabel(
                  'POSITIONS', 
                  fontsize=15, 
                  fontname='Calibri'
                  )

    plt.suptitle(
                 'AVERAGE PLAYER VALUES BY POSTIONS', 
                 fontsize=18, 
                 fontname='Calibri', 
                 fontweight='bold'
                 )

    plt.title('*EA Sports FIFA 23', fontname='Calibri')
    plt.ylim(1_000_000, 4_000_000)

    for index, value in enumerate(average_values):
        plt.text(
                 index, 
                 value, 
                 str(value), 
                 fontsize=15, 
                 position=(index-0.1, value+50_000)
                )

    plt.show()

defenders_avg = find_defenders_averages()
midfielders_avg = find_midfielders_averages()
attackers_avg = find_attackers_averages()
keepers_avg = find_keepers_averages()
get_average_value_by_position(defenders_avg, midfielders_avg, attackers_avg, keepers_avg)