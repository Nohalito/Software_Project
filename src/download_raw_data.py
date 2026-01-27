# Base import
import pandas as pd
import numpy as np

#Repo management
import os
import sys
sys.path.append('.') 

# Configture
import config as c


def download_raw_data():
    """
    No raw data to download atm, maybe one day?
    """
    if os.path.exists(c.RAW_DATA_PATH) is False:
        os.makedirs(c.RAW_DATA_PATH)

if __name__ == "__main__":
    download_raw_data()