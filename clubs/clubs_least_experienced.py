

import pandas as pd 
import matplotlib.pyplot as plt
from data import get_clean_data

fifa_23 = get_clean_data()

def find_teams_ages_players() -> dict[str:list]:

    teams = {}
    for i in fifa_23.index:
        club = fifa_23.loc[i, 'club']
        age = fifa_23.loc[i, 'age']
        if club not in teams:
            teams[club] = [age, 1]
        else:
            teams[club][0] += age 
            teams[club][1] += 1

    return teams

def get_teams_average_age(all_teams: dict[str: list]) -> dict[str:float]:

    teams_avg_age = {}
    for key, values in all_teams.items():
        teams_avg_age[key] = round(values[0] / values[1], 2)

    return teams_avg_age

def create_pandas_series(avg_age: dict[str:float]) -> pd.Series:
    
    series = pd.Series(avg_age).nsmallest(n=10)
    return series

def display_least_experienced_teams(experienced_teams: pd.Series) -> None:

    teams = experienced_teams.index.tolist()
    avg_age = experienced_teams.values.tolist()
    colors = [
              '#379237', '#86C8BC', '#86C8BC', 
              '#FFF6BD', '#FFF6BD', '#FFF6BD',
              '#FAAB78', '#FAAB78', '#FAAB78', 
              '#FAAB78'
              ]

    fig = plt.subplots()

    plt.barh(teams, avg_age, color = colors)

    plt.suptitle(
                 'LEAST EXPERIENCED TEAMS',
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

    plt.xlim(0, 23)
    plt.show()

teams = find_teams_ages_players()
average_age = get_teams_average_age(teams)
pd_series = create_pandas_series(average_age)
display_least_experienced_teams(pd_series)