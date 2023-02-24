

import pandas as pd
import matplotlib.pyplot as plt 
from data import get_clean_data
from league_5 import all_teams

fifa_23 = get_clean_data()
league_5 = fifa_23[fifa_23['club'].isin(all_teams)]

def find_teams_ages_players(l5: pd.DataFrame) -> dict[str:list]:

    teams = {}
    for i in l5.index:
        club = fifa_23.loc[i, 'club']
        age = fifa_23.loc[i, 'age']
        if club not in teams:
            teams[club] = [age, 1]
        else:
            teams[club][0] += age 
            teams[club][1] += 1

    return teams

def get_teams_average_age(t5_ages: dict[str:list]) -> dict[str:float]:
    
    teams_avg_age = {}
    for key, values in t5_ages.items():
        teams_avg_age[key] = round(values[0] / values[1], 2)

    return teams_avg_age

def create_pandas_series(avg_age: dict[str:float]) -> pd.Series:
    
    series = pd.Series(avg_age).nsmallest(n=10)
    return series

def display_least_experienced_teams(l5_clubs: pd.Series) -> None:

    teams = l5_clubs.index.tolist()
    avg_age = l5_clubs.values.tolist()
    colors = [
              '#379237', '#86C8BC', '#86C8BC', 
              '#FFF6BD', '#FFF6BD', '#FFF6BD',
              '#FFF6BD', '#FAAB78', '#FAAB78', 
              '#FAAB78'
              ]

    fig = plt.subplots()

    plt.barh(teams, avg_age, color = colors)

    plt.suptitle(
                 'LEAST EXPERIENCED IN TOP 5 EUROPEAN LEAGUES',
                 fontsize = 18,
                 fontname = 'Calibri',
                 fontweight = 'bold'
                )

    plt.title(
              '*EA Sports FIFA 23',
              fontsize = 8,
              fontname = 'Calibri'
             )

    plt.xlabel(
               'AVERAGE AGE',
               fontsize = 15,
               fontname = 'Calibri'
              )

    plt.ylabel(
               'CLUBS',
               fontsize = 15,
               fontname = 'Calibri'
              )

    for index, value in enumerate(avg_age):
        plt.text(
                 value, 
                 index, 
                 str(value), 
                 position=(value-0.75, index-0.1)
                )

    plt.xlim(0, 25)
    plt.show()

all_ages = find_teams_ages_players(league_5)
avg_age = get_teams_average_age(all_ages)
pd_series = create_pandas_series(avg_age)
display_least_experienced_teams(pd_series)