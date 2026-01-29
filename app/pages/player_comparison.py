# Basic libraries
import pandas as pd

# Streamlit app
import streamlit as st

# Visualization library
import plotly.express as px

# Syntax
import re

# Path managment
import os
import sys
sys.path.append('.')
sys.path.append('./.src')

# Custom libraries
import config as c
import function as f

# Download the data already prepared
if not os.path.exists(c.DATA_DIR):
    download_data()

# Roses are red
# Streamlit is lit
# With this treasure I summon
# Lebron James application

# Design on paper
# Final touch with big nerdy studying arc

# ----------------------------
# => Page config
# ----------------------------
st.set_page_config(
    page_title="NBA Player Explorer",
    layout="wide",
)

st.title("🏀 NBA Player pokemon match")

# Dataset :
df = f.load_data()
df = df.sort_values(["Player", "Year"])

# ----------------------------------------
# => Sidebar filters :
# ----------------------------------------
st.sidebar.header("Filter Player")

# Filter df on player_1
default_player_1 = "LeBron James"

player_1 = st.sidebar.selectbox(
    "Select your 1st pokemon",
    df["Player"].unique(),
    index=list(df["Player"].unique()).index(default_player_1) if default_player_1 in df["Player"].unique() else 0
)

player_df_1 = df[df["Player"] == player_1]

# Manage players that went to multiple team
regex = r'[0-9]TM' # iswtg <3 on re
multi_team_1 = (
    player_df_1.groupby(['Player', 'Year'])['Team']
      .transform('nunique') > 1
)
player_df_evolution_1 = player_df_1[
    (multi_team_1 & (player_df_1['Team'].str.contains(regex))) |
    (~multi_team_1)
].copy()

# Filter sub df on season stats
season_1 = st.sidebar.selectbox(
    "Select Season of your 1st pokemon",
    player_df_1["Year"].unique()
)

season_df_1 = player_df_1[player_df_1["Year"] == season_1]

# Filter df on player_2
default_player_2 = "Stephen Curry"

player_2 = st.sidebar.selectbox(
    "Select 2nd pokemon",
    df["Player"].unique(),
    index=list(df["Player"].unique()).index(default_player_2) if default_player_2 in df["Player"].unique() else 0
)

player_df_2 = df[df["Player"] == player_2]

# Manage players that went to multiple team
regex = r'[0-9]TM' # iswtg <3 on re
multi_team_2 = (
    player_df_2.groupby(['Player', 'Year'])['Team']
      .transform('nunique') > 1
)
player_df_evolution_2 = player_df_2[
    (multi_team_2 & (player_df_2['Team'].str.contains(regex))) |
    (~multi_team_2)
].copy()

# Filter sub df on season stats
season_2 = st.sidebar.selectbox(
    "Select Season of pookie n°2",
    player_df_2["Year"].unique()
)

season_df_2 = player_df_2[player_df_2["Year"] == season_2]

# Dataframe concat : 

player_df_evolution = pd.concat([player_df_evolution_1, player_df_evolution_2])
season_df = pd.concat([season_df_1, season_df_2])

# Inspiration : https://www.sports-reference.com/stathead/basketball/vs/kevin-durant-vs-dominique-wilkins

# ----------------------------
# => Player Header
# ----------------------------
col1, col2 = st.columns(2)

# Player 1 info
with col1:
    st.subheader(f"{player_1} - {season_1}")
    st.caption(
        f"Team: {season_df_1['Team'].values[0]} | "
        f"Position: {season_df_1['Pos'].values[0]} | "
        f"Age: {int(season_df_1['Age'].values[0])}"
    )

# Player 2 info
with col2:
    st.subheader(f"{player_2} - {season_2}")
    st.caption(
        f"Team: {season_df_2['Team'].values[0]} | "
        f"Position: {season_df_2['Pos'].values[0]} | "
        f"Age: {int(season_df_2['Age'].values[0])}"
    )

# ----------------------------
# => Season Breakdown
# ----------------------------
st.markdown("### 📊 Poke Stop")

cols_to_show = [
    "Year", "Player", "G",
    "PTS", "AST", "TRB",
    "FG%", "3P%", "FT%",
    "STL", "BLK", "Awards"
    ]

st.dataframe(
    season_df[cols_to_show]
    .reset_index(drop = True)
    .style.format('{:.3f}', subset = cols_to_show[-9:-1]) # https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format.html
    #.background_gradient(cmap = 'flag',subset = cols_to_show[-11:]), # https://matplotlib.org/stable/users/explain/colors/colormaps.html
    .highlight_max(color = 'midnightblue', axis = 0, subset = cols_to_show[-9:-1]), # https://pandas.pydata.org/docs/reference/style.html
    
    # Couldn't find any better way to implement the 'tooltip'
    column_config = {
        "G": "Games played",
        "MP": "Minutes played",
        "PTS": "Points scored",
        "AST": "Assists",
        "FG%": "Field goal %",
        "3P%": "3-point field goal %",
        "FT%": "Free throw %",
        "STL": "Steals",
        "BLK": "Blocks",
        "TRB": "Total rebounds",
    }
)

# ----------------------------
# => Career Trends
# ----------------------------
st.markdown("### 📈 Careers Trends")

trend_stat = st.selectbox(
    "Select Stat",
    ["PTS", "AST", "TRB", "FG%", "3P%", "TOV"]
)

fig_trend = px.line(
    player_df_evolution,
    x = "Year",
    y = trend_stat,
    color = "Player",
    markers=True,
)

fig_trend.update_layout(
    yaxis_title = trend_stat,
    legend_title_text = "Player"
)

st.plotly_chart(fig_trend)
