

from pathlib import Path 
import pandas as pd 

directory = Path(__file__).parents[1]
file = directory / 'fifa_2023_data.csv'
fifa_23 = pd.read_csv(file)

# fixing column names
fifa_23.rename(columns={
    'Club Name' : 'club',
}, inplace=True)

fifa_23.columns = [x.lower() for x in fifa_23]
fifa_23.drop_duplicates(inplace=True)

def find_free_agents() -> pd.DataFrame:
    
    free_agents = fifa_23[fifa_23['club'] == 'Free agent']
    return free_agents