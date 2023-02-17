

import pandas as pd 
import matplotlib.pyplot as plt
from data import get_clean_data 

fifa_23 = get_clean_data()

def find_most_popular_jerseys() -> pd.Series:

    return fifa_23['jersey'].value_counts().nlargest(n=10)

def get_most_popular_jerseys_chart(popular_jerseys: pd.Series) -> None:

    raw_numbers = popular_jerseys.index.tolist()
    players_wearing = popular_jerseys.values.tolist()
    jersey_numbers = [f'No.{x}' for x in raw_numbers]
    colors = [
              '#645CBB', '#FF6D28', '#579BB1', 
              '#939B62', '#FF7B54', '#00E7FF', 
              '#F6F7C1', '#537FE7', '#B9F3E4', 
              '#E5D1FA'
             ]

    fig, ax = plt.subplots()

    ax.barh(
            jersey_numbers, 
            players_wearing, 
            color=colors
            )

    ax.set_ylabel(
                  'JERSEY NUMBERS', 
                  fontname='Calibri', 
                  fontsize=15
                  )

    ax.set_xlabel(
                  'NUMBER OF PLAYERS WEARING', 
                  fontname='Calibri', 
                  fontsize=15
                  )

    plt.suptitle(
                 'MOST POPULAR JERSEYS IN FOOTBALL(SOCCER)', 
                 fontsize=18, 
                 fontname='Calibri', 
                 fontweight='bold'
                 ) 

    plt.title('*source EA Sports FIFA 23', fontname='Calibri')
    plt.xlim(530, 600)

    for index, value in enumerate(players_wearing):
        plt.text(value, index, str(value))

    plt.show()


jerseys = find_most_popular_jerseys()
get_most_popular_jerseys_chart(jerseys)

