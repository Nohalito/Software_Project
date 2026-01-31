Software_Project
====================

This is our group project of the Softwares class from our M2 EDS track
Author : 

- **Boimond Noa**
- **Dennis Yann**
- **Maffre Camille**

# 1°/ How to Run the App

Here's the guideline that will allow you to use all of our deliverable, notebook & application (We tried to provide a clear guide even though we used the deplorable technology that you despise, window 😱...) :

## 1.1°/ Install Docker :

No one is spared here, make sure you have **Docker** installed on your computer. If not, follow this <a href = "https://docs.docker.com/get-started/introduction/get-docker-desktop/">tutorial</a> to download and install it from the official Docker website. Then take some note from this super guys : <a href = "https://github.com/virgilus/docker/tree/main">Virgilus</a> to follow the rest of this READ_ME.

## 1.2°/ Clone the Repository :

Clone this repository on your quantic computer :

- `git clone https://github.com/Nohalito/Software_Project.git`
- `cd Softwares_Project`

## 1.3°/ Build the Docker Image :

Next, build the Docker image using the provided Dockerfile :

- `docker build -t NBA-LEBRRROOOOON .`

## 1.4°/ Run the Application :

Once the image is built, you can run the Docker container like this :

- `docker run -p 8501:8501 NBA-LEBRRROOOOON`

This will both download the processed data and 'Expose' the Streamlit app on the (vieux) port 8501. Our app is now at your disposal (either opened automatically or open your webbroswer at "http://localhost:8501").

# 2°/ Topic presentation :
## 2.1°/ Topic inspiration :

To choose our topic, we started with the initial idea of analyzing player stat from whatever sport with an interesting dataset to download.

As such we had topics like this :

- <a href = 'https://www.hltv.org/stats/players'>CSGO Player</a>
- <a href = 'https://www.over.gg/stats'>Overwatch Player</a>
- <a href = 'https://www.nhl.com/stats/'>NHL Player</a>

All followed similar format, for each season, they would present the player performance over it with statistic like winrate, point scored and so on...

But what truly made us choose the NBA topic was someone else github : <a href = 'https://github.com/Andy-Pham-72/Web-Scraping-with-BeautifulSoup-and-Pandas/tree/master'>**Andy-Pham-72**</a>.
While exploring webscrapping tutorial, we encountered his repository, and the target of his repository. The NBA player statistics.

## 2.1°/ NBA Player stats :

The datasets we extracted came from the season page <a href = "https://www.basketball-reference.com/leagues/NBA_2023.html">(Ex : 2023)</a>, from there, we could find all season official ranking for the top player.

After extracting 10 years worth of data, our dataset format was the following : 

|Rank|Player|Games played|...|Lot of different stat|...|Points scored per game|season|
|---|---|---|---|---|---|---|---|
|1st|LEBRONNN JAMESS|999|$\cdots$|$\cdots$|$\cdots$|69|2015|
|2nd|Stephen Curry|13|$\cdots$|$\cdots$|$\cdots$|29|2015|
|$\vdots$|$\vdots$|$\vdots$|$\vdots$|$\vdots$|$\vdots$|$\vdots$|
|1st|Lebron James Jr|999|$\cdots$|$\cdots$|$\cdots$|69|2025|
|2nd|Michael Jackson|20|$\cdots$|$\cdots$|$\cdots$|heehee|2025|
|$\vdots$|$\vdots$|$\vdots$|$\vdots$|$\vdots$|$\vdots$|$\vdots$|

# 3°/ Repository structure :

```
Software_Project/
├── .gitignore
├── Dockerfile                          # Dockerfile to run our project 
├── README.md                           # Rea. D. Me, the will of Documentation
├── config.py                           # Config, contain global variable
├── project_M2_software_2025-2026.pdf   # Teacher instruzione
├── repo_tree.ipynb
├── requirements.txt                    # All python libraries
├── app
│   ├── app.py                          # Streamlit app
│   ├── assets.py                       # Assets folder
│   │   ├── img_1.png
│   │   ├── ...                       
│   │   └── img_n.jpg
│   └── pages.py                        # Streamlit app pages
│       ├── gallery.py
│       ├── player_comparison.py                       
│       └── player_stat.py
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
    └── function.py
```

# References : 

List of cool fellow we took inspirations from :

- <a href = "https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/">Emoji list</a>
- Lot of cool person from <a href = "https://docs.streamlit.io/">Streamlit</a>
- The third coming of <a href = "https://github.com/virgilus">Linux Jesus</a>
- <a href = 'https://github.com/Andy-Pham-72/Web-Scraping-with-BeautifulSoup-and-Pandas/tree/master'>Andy-Pham-72</a>
- <a href = "https://matplotlib.org/stable/users/explain/colors/colormaps.html">Python color map 🌈</a>
<!-- - <a href = ""></a>-->
- <a href = "https://www.youtube.com/shorts/PU_zFsvy0Go">Emmanuel Macron</a> 😎