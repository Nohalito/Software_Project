Softwares_Project
====================

This is our group project of the Softwares class from our M2 EDS track
Made by Boimond Nhoha and Maffre Cacamille

# 1°/ How to use our code :

Here's the guideline that will allow you to use all of our deliverable, notebook & application (We tried to provide a clear guide even though we used the deplorable technology that window is...) :

- Open any terminal that can allow you to run git
- Clone this project : `git clone https://github.com/Nohalito/Softwares_Project.git`

# 2°/ Topic presentation :
## 2.1°/ NBA Player stats :

- <a href = 'https://www.basketball-reference.com/leagues/NBA_2024_per_game.html'>Basketball</a> => shout out to this guy : <a href = 'https://github.com/Andy-Pham-72/Web-Scraping-with-BeautifulSoup-and-Pandas/tree/master'>Andy-Pham-72</a>

## 2.2°/ Other topic we looked for before :

- <a href = 'https://www.hltv.org/stats/players'>CSGO</a>
- <a href = 'https://www.over.gg/stats'>Overwatch</a>

# 3°/ Repository structure :

```
Softwares_Project/
├── .gitignore
├── Dockerfile                          # Dockerfile to run our project 
├── README.md                           # Rea. D. Me, the will of **D**ocumentation
├── config.py                           # Config, contain global variable
├── project_M2_software_2025-2026.pdf   # Teacher instruzione
├── repo_tree.ipynb
├── requirements.txt                    # All python libraries
├── app
│   └── app.py                          # Streamlit app
├── datasets
│   └── processed                       # Dataset folder
│       └── player_stats_2015-2026.csv
├── hazard_zone_(test)                  # All of our coding test (irrelevant but funny)
│   ├── app_test.ipynb
│   └── data_collection.ipynb
├── notebooks                           # Notebooks used to perform EDA
│   └── super_awesome_EDA.ipynb
└── src
    ├── __init__.py
    ├── download_data.py                # Download processed data function
    ├── download_raw_data.py            # Download raw data function
    └── function.py
```