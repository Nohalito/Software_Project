import os
from datetime import datetime

DATA_DIR = "datasets/"
RAW_DATA_PATH = os.path.join(DATA_DIR, "raw/")
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, "processed/")

DATA_URL = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

START_YEAR = 2015 #1947 début BBA, 1950 début NBA, à partir de 1980 on a plus de colonnes, et 1982 pour que les colonnes soient remplies bien 
END_YEAR = datetime.today().year #mdr fait gaffe si tu prends un erreur trop large on a une erreur "trop de requetes"

PER_GAME_DF_FILENAME = f"player_stats_{START_YEAR}-{END_YEAR}.csv"


# Need to do the same for our future df 
# CITY_DF_FILENAME = "city_df.csv"
# CITY_FILENAME = "communes-france-2025.csv.gz"
# CITY_WITH_CLOSEST_STATIONS_DF_FILENAME = "city_with_closest_stations_df.csv"
# GOOD_STATIONS_FILENAME = "good_stations_df.csv"

# TEMP_FOLDER = "temp"
# DEFAULT_WEATHER_FILENAME = "Q_13_previous-1950-2023_RR-T-Vent.csv.gz"
# COMPLETION_RATE_THRESHOLD = 0.65
# DEFAULT_WEATHER_URL = "https://object.files.data.gouv.fr/meteofrance/data/synchro_ftp/BASE/QUOT/"