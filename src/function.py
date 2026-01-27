# Basic libraries
import os
import pandas as pd

# Set up path
import sys
sys.path.append('.')

# Configture
import config as c

def load_data(
    filename: str = c.PER_GAME_DF_FILENAME,
    path: str = c.PROCESSED_DATA_PATH,
) -> pd.DataFrame:
    """
    Load the processed dataframe from a .csv file.
    """

    #for k, v in list(zip(df.dtypes.index, df.dtypes)):
    #print(f"'{k}' : '{v}',")
    d = {'Rk' : 'float64',
        'Player' : 'object',
        'Age' : 'float64',
        'Team' : 'object',
        'Pos' : 'object',
        'G' : 'int32',
        'GS' : 'int32',
        'MP' : 'float64',
        'FG' : 'float64',
        'FGA' : 'float64',
        'FG%' : 'float64',
        '3P' : 'float64',
        '3PA' : 'float64',
        '3P%' : 'float64',
        '2P' : 'float64',
        '2PA' : 'float64',
        '2P%' : 'float64',
        'eFG%' : 'float64',
        'FT' : 'float64',
        'FTA' : 'float64',
        'FT%' : 'float64',
        'ORB' : 'float64',
        'DRB' : 'float64',
        'TRB' : 'float64',
        'AST' : 'float64',
        'STL' : 'float64',
        'BLK' : 'float64',
        'TOV' : 'float64',
        'PF' : 'float64',
        'PTS' : 'float64',
        'Awards' : 'object',
        'Year' : 'int64'
    }

    return pd.read_csv(os.path.join(path, filename), dtype=d)