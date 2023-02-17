

import pandas as pd 
import matplotlib.pyplot as plt
from data import get_clean_data

fifa_23 = get_clean_data()

def find_most_popular_jerseys()  -> pd.Series:

    popular_jerseys = fifa_23['jersey'].value_counts().nlargest(n=10).index.tolist()
    return popular_jerseys

def find_wages_for_jerseys(popular_jerseys: pd.Series) -> dict[int:int]:

    jersey_wage = {}
    for jersey in popular_jerseys:
        number = fifa_23[fifa_23['jersey'] == jersey]
        wages = number['wage']
        jersey_wage[jersey] = int(round(sum(wages)/len(wages), 0))

    return jersey_wage

def display_average_wage_by_jerseys(j_w: dict[int:int]) -> None:

    jerseys = [f'No.{k}' for k in j_w.keys()]
    wages = [v for v in j_w.values()]
    colors = [
              '#645CBB', '#FF6D28', '#579BB1', 
              '#939B62', '#FF7B54', '#00E7FF', 
              '#F6F7C1', '#537FE7', '#B9F3E4', 
              '#E5D1FA'
            ]
    fig, ax = plt.subplots()

    ax.barh(
            jerseys, 
            wages, 
            color=colors
            )

    ax.set_ylabel(
                  'JERSEY NUMBERS', 
                  fontname='Calibri', 
                  fontsize=15
                  )

    ax.set_xlabel(
                  'AVERAGE WEEKLY WAGES (Euros)', 
                  fontname='Calibri', 
                  fontsize=15
                  )

    plt.suptitle(
                 'AVERAGE WEEKLY WAGES (BY JERSEY NUMBER) IN EUROS', 
                 fontsize=18, 
                 fontname='Calibri', 
                 fontweight='bold'
                 )

    plt.title('*EA Sports FIFA 23', fontname='Calibri')
    plt.xlim(0, 16_000)

    for index, values in enumerate(wages):
        plt.text(
                 values, 
                 index, 
                 str(values), 
                 position=(values-700, index-0.1), 
                 fontsize=12.5
                 )

    plt.show()

jerseys = find_most_popular_jerseys()
jerseys_wages = find_wages_for_jerseys(jerseys)
display_average_wage_by_jerseys(jerseys_wages)
