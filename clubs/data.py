
from pathlib import Path 
import pandas as pd 

directory = Path(__file__).parents[1]
file = directory / 'fifa_2023_data.csv'
fifa_23 = pd.read_csv(file)

# fixing column names
fifa_23.rename(columns={
    'Value(in Euro)' : 'value',
    'Wage(in Euro)' : 'wage',
    'Club Name' : 'club', 
    'Club Jersey Number' : 'jersey'
}, inplace=True)

fifa_23.columns = [x.lower() for x in fifa_23]
fifa_23.drop_duplicates(inplace=True)

def get_clean_data() -> pd.DataFrame:

    fifa_23.drop(fifa_23[fifa_23['jersey'] == '-'].index, inplace=True)
    fifa_23['jersey'] = fifa_23['jersey'].astype(int)
    return fifa_23