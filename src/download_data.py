# Base import
from datetime import datetime
import pandas as pd
#import numpy as np

#Repo management
import os
import shutil
import sys
sys.path.append('..')
# sys.path.append('../datasets')
# sys.path.append('../notebooks')

from Softwares_Project import config as c

def download_data(annee_debut:int ,annee_fin:int):
    """
    Downloads the basket file from this website: https://www.basketball-reference.com
    pfiou pfiou dribble dribble pass AND OHHHHHHHH KOBE MADE ANOTHER 3 POINT DAMN

    from now we only store data of player in average per game for years specified in the config file (we store it in the datasets/processed path)
    """
    df = pd.DataFrame()
    for i in range(annee_debut, annee_fin+1):

        url = f'https://www.basketball-reference.com/leagues/NBA_{i}_per_game.html'

        df_temp = pd.read_html(url, header = 0)[0] # This request output a list of dataframe read from the url, let's select the correct one : r[0] => Regular Season /// r[1] => playoffs
        df_temp['Year'] = i #adding the corresponding year

        # The last rows contains average of all players => useless
        # df.loc[df['Rk'].isna()] => return an empty row
        df_temp = df_temp.drop(df_temp.tail(1).index)

        # The columns G and GS are float, even though all number are int
        # df.dtypes
        try:
            df_temp['G'] = df_temp['G'].astype('int32')
            df_temp['GS'] = df_temp['GS'].astype('int32')
            print("toutes les colonnes ont été converties.")
        except KeyError, pd.errors.IntCastingNaNError:
            print("Certaines colonnes n'existent pas, le reste a été converti.")

        # Truth be told, the NaN
        # So let's just set them up to 0, the ranking argument is the points scored 'PTS', so it shouldn't be a problem for our futur uses. 
        # missing.index => ctrl + c & ctrl + v
        # df[['FG%', '3P%', '2P%', 'eFG%', 'FT%']] = df[['FG%', '3P%', '2P%', 'eFG%', 'FT%']].fillna(0.0)
        # that's what we would have done if we didn't read the data, but anyways the only missing % is when it's equal to 0.0 so it's also working in theory
        #for some other years, others informations are missing, there is the filling part for every possible blank
        def calc_percentage (numerator:str,denominator:str):
            """
            The most basic division possible, rounding the result 3 number after the decimal
            """
            return df_temp[numerator]/df_temp[denominator].round(3)

        transfo = {
            'FG%': calc_percentage("FG","FGA").fillna(0), #on fillna car pandas laisse du na quand tu fais une division impossible et il te préviens pas cet enculé histoire que tu perde 1h30 dessus
            '3P%': calc_percentage("3P","3PA").fillna(0), #du coup ça rempli d'abord tout ce que ça peut remplir et après ça met des 0 quand le calcul était pas possible (divison par 0)
            '2P%': calc_percentage("2P","2PA").fillna(0), #https://fr.pornhub.com c'est cadeau
            'FT%': calc_percentage("FT","FTA").fillna(0),
            'Awards': 'No Awards'
            }

        for key,values in transfo.items():
            try:
                df_temp[key] = df_temp[key].fillna(values)
                print(f"La colonne {key} a été remplie avec succès.")
            except KeyError:
                print(f"La colonne {key} n'existe pas sur cette année là.")

        #special treatment for eFG%:
        df_temp['eFG%'] = round(((df_temp['PTS']-df_temp['FT'])/2)/df_temp['FGA'],3).fillna(0) #bc i cannot find how the calcul was made on the website so i use mine, the fillna(0) is for same reason as before


        pd.concat([df,df_temp], ignore_index = True) #ajoute la nouvelle année traitée
        print(i, ' : ',len(df))



    if os.path.exists(os.path.join(c.PROCESSED_DATA_PATH, c.PER_GAME_DF_FILENAME)): #supprime le csv s'il existe déjà
        shutil.rmtree(os.path.join(c.PROCESSED_DATA_PATH, c.PER_GAME_DF_FILENAME))
    elif os.path.exists(c.PROCESSED_DATA_PATH) is False: #créé le fichier
        os.makedirs(c.PROCESSED_DATA_PATH)
    df.to_csv(c.PROCESSED_DATA_PATH + c.PER_GAME_DF_FILENAME) #je suis pas sur de celle là j'ai essayé la docu de https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
    






if __name__ == "__main__":
    download_data(c.START_YEAR,c.END_YEAR)   


