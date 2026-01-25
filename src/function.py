# Basic libraries
import os
import pandas as pd

# Set up path
import sys
sys.path.append('.')

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

#def compute_number_of_frost_days_per_year(df: pd.DataFrame) -> pd.DataFrame:
#    """Compute the number of frost days per year from the weather DataFrame.
#    Make sure the DataFrame contains 'date' and 'tmin' columns and that the
#    dataframe has been filtered beforehand, in you want to compute on a single station.
#    """
#    frost_days_per_year = df.groupby('year')['frost_day'].sum().reset_index()
#    # Convert year to int to avoid decimal display in charts
#    frost_days_per_year['year'] = frost_days_per_year['year'].astype(int)
#    return frost_days_per_year
#
#def compute_mean_number_of_frost_days(df: pd.DataFrame) -> float:
#    """Compute the average number of frost days per year from a DataFrame containing 'frost_day' and 'year' columns.
#    Make sure your dataframe has been filtered beforehand, if you want to compute on a single station."""
#    frost_days_per_year = df.groupby('year')['frost_day'].sum()
#    return frost_days_per_year.mean()
#
#def compute_frost_days_percentage_per_day(df: pd.DataFrame) -> pd.DataFrame:
#    """Compute the percentage of frost days for each day of the year over all years.
#    Returns a DataFrame with day_of_year as index for proper chronological ordering in charts.
#    """
#    # Add day of year for proper ordering
#    df_temp = df.copy()
#    df_temp['day_of_year'] = df_temp['date'].dt.dayofyear
#    
#    # Group by day of year and calculate frost day percentage
#    frost_by_day = df_temp.groupby('day_of_year').agg({
#        'frost_day': lambda x: (x.sum() / len(x)) * 100,
#        'month': 'first',
#        'day': 'first'
#    }).reset_index()
#
#    # Create the DD/MM format for display
#    frost_by_day['date_str'] = frost_by_day['day'].astype(str).str.zfill(2) + '/' + frost_by_day['month'].astype(str).str.zfill(2)
#
#    # Use day_of_year as index to preserve chronological order
#    frost_by_day = frost_by_day.set_index('day_of_year')[['frost_day']].rename(columns={'frost_day': 'Frost Days (%)'})
#
#    return frost_by_day