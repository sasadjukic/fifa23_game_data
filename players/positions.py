
import pandas as pd
from data import get_clean_data

fifa_23 = get_clean_data()

DEFENDERS = ['LB', 'LWB', 'LCB', 'CB', 'RCB', 'RWB', 'RB']
MIDFIELDERS = ['LM', 'LCM', 'CM', 'DM', 'CAM', 'RCM', 'RM']
ATTACKERS = ['RW', 'RF', 'CF', 'ST', 'LF', 'LW']

def find_defenders() -> pd.DataFrame:

    defenders = fifa_23[fifa_23['best position'].isin(DEFENDERS)]
    return defenders

def find_midfielders() -> pd.DataFrame:

    midfielders = fifa_23[fifa_23['best position'].isin(MIDFIELDERS)]
    return midfielders

def find_attackers() -> pd.DataFrame:

    attackers = fifa_23[fifa_23['best position'].isin(ATTACKERS)]
    return attackers

def find_keepers() -> pd.DataFrame:

    goalkeepers = fifa_23[fifa_23['best position'] == 'GK']
    return goalkeepers