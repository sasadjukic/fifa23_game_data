

import pandas as pd 
import matplotlib.pyplot as plt
from data import get_clean_data

fifa_23 = get_clean_data()

def get_expiring_contracts() -> dict[str:int]:

    teams_contracts = {}
    for club in fifa_23['club']:
        team = fifa_23[fifa_23['club'] == club]
        contracts = team['contract until'].tolist().count('2023')
        teams_contracts[club] = contracts
    
    return teams_contracts

def get_top_expiring_contracts(contracts: dict[str:int]) -> pd.Series:
    
    return pd.Series(contracts).nlargest(n=5)

def display_top_expiring_cotracts(top_exp_cont: pd.Series) -> None:

    teams = top_exp_cont.index
    exp_contracts = top_exp_cont.values
    colors = [
              '#FC5404', '#FAAB78', '#FAAB78', 
              '#FFF6BD', '#FFF6BD'
              ]

    fig = plt.subplot()

    plt.barh(
            teams, 
            exp_contracts, 
            color=colors
            )

    plt.suptitle(
                 'CLUBS WITH MOST EXPIRING CONTRACTS',
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
                 position=(value-0.75, index-0.05)
                 )

    plt.show()
    

exp_contracts = get_expiring_contracts()
top_exp_contracts = get_top_expiring_contracts(exp_contracts)
display_top_expiring_cotracts(top_exp_contracts)