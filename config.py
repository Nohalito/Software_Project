import os
from datetime import datetime

DATA_DIR = "datasets/"
RAW_DATA_PATH = os.path.join(DATA_DIR, "raw/")
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, "processed/")

DATA_URL = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

#1947 début BBA, 1950 début NBA, à partir de 1980 on a plus de colonnes, et 1982 pour que les colonnes soient remplies bien 
START_YEAR = 2015
END_YEAR = 2025 
# END_YEAR = datetime.today().year

PER_GAME_DF_FILENAME = f"player_stats_{START_YEAR}-{END_YEAR}.csv"