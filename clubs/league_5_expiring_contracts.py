

import pandas as pd
import matplotlib.pyplot as plt
from data import get_clean_data
from league_5 import all_teams

fifa_23 = get_clean_data()
league_5 = fifa_23[fifa_23['club'].isin(all_teams)]

def get_expiring_contracts(clubs: pd.DataFrame) -> dict[str:int]:

    team_contracts = {}

    for club in clubs['club']:
        team = clubs[clubs['club'] == club]
        contracts = team['contract until'].tolist().count('2023')
        team_contracts[club] = contracts 

    return team_contracts 

def get_top_expiring_contracts(contracts: dict[str:int]) -> pd.Series:

    return pd.Series(contracts).nlargest(n=5)

def display_top_expiring_cotracts(top_contracts: pd.Series) -> None:

    teams = top_contracts.index
    exp_contracts = top_contracts.values 
    colors = [
              '#F77E21', '#F77E21', '#F77E21',
              '#FCFFB2', '#C7F2A4'
              ]

    fig = plt.subplot()

    plt.barh(
            teams, 
            exp_contracts, 
            color=colors
            )

    plt.suptitle(
                 'EXPIRING CONTRACTS IN TOP 5 EUROPEAN LEAGUES',
                 fontname = 'Calibri',
                 fontsize = 18,
                 fontweight = 'bold'
                )

    plt.title(
              '*EA Sports FIFA 23',
              fontname = 'Calibri',
              fontsize = 8
             )

    plt.xlabel(
               'NUMBER OF EXPIRING CONTRACTS',
               fontname = 'Calibri',
               fontsize = 15  
              )

    plt.ylabel(
               'CLUBS',
               fontname = 'Calibri',
               fontsize = 15
              )

    for index, value in enumerate(exp_contracts):
        plt.text(
                 value, 
                 index, 
                 str(value), 
                 position=(value-0.5, index-0.05)
                 )
    plt.xticks([0, 5, 10, 15])
    plt.xlim(0, 19)
    plt.show()


all_contracts = get_expiring_contracts(league_5)
top_contracts = get_top_expiring_contracts(all_contracts)
display_top_expiring_cotracts(top_contracts)
