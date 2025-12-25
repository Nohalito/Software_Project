# Basic libraries
import pandas as pd

# Streamlit app
import streamlit as st

# Visualization library
import plotly.express as px

# Path managment
import os
import sys
sys.path.append('.')
sys.path.append('./src')

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
#st.title("NBA Player statistics 🏀")

# ----------------------------
# => Page config
# ----------------------------
st.set_page_config(
    page_title="🏀 NBA Player Explorer",
    layout="wide",
)

st.title("🏀 NBA Player Explorer")

# Dataset :
df = f.load_data()
df = df.sort_values(["Player", "Year"])

# ----------------------------------------
# => Sidebar filters :
# 1°/ Select a player
# 2°/ Select a year he played
# 3°/ Select a team he played in (optional)
# ----------------------------------------
st.sidebar.header("Filter Player")

# 1°/ Search bar + scrolling list :
# 1st the user tingle with the search bar :
search_term = st.sidebar.text_input("Search Player")

# 2nd we filter the player list based on the search term
if search_term:
    filtered_players = [player for player in df["Player"].unique() if search_term.lower() in player.lower()]
else:
    filtered_players = sorted(df["Player"].unique())

# 3rd we show the updated list of player corresponding to the term
player = st.sidebar.selectbox(
    "Select Player",
    filtered_players
)

player_df = df[df["Player"] == player]

# 2°/ Scrolling list for season
season = st.sidebar.selectbox(
    "Select Season",
    player_df["Year"].unique()
)

season_df = player_df[player_df["Year"] == season].iloc[0]

# ----------------------------
# => Player Header
# ----------------------------
st.subheader(f"{player} — {season}")
st.caption(
    f"Team: {season_df['Team']} | Position: {season_df['Pos']} | Age: {int(season_df['Age'])}"
)

# ----------------------------
# => Key Metrics
# ----------------------------
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("PTS", f"{season_df['PTS']:.1f}")
col2.metric("AST", f"{season_df['AST']:.1f}")
col3.metric("TRB", f"{season_df['TRB']:.1f}")
col4.metric("MP", f"{season_df['MP']:.1f}")
col5.metric("G", int(season_df["G"]))

# ----------------------------
# => Shooting Efficiency
# ----------------------------
st.markdown("### 🎯 Shooting Efficiency")

shooting_df = pd.DataFrame({
    "Shot Type": ["FG%", "3P%", "2P%", "FT%"],
    "Percentage": [
        season_df["FG%"] * 100,
        season_df["3P%"] * 100,
        season_df["2P%"] * 100,
        season_df["FT%"] * 100,
    ]
})

fig_shooting = px.bar(
    shooting_df,
    x="Shot Type",
    y="Percentage",
    text="Percentage",
    range_y=[0, 100],
)

fig_shooting.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
fig_shooting.update_layout(yaxis_title="%", showlegend=False)

st.plotly_chart(fig_shooting)

# ----------------------------
# => Season Trends
# ----------------------------
st.markdown("### 📈 Career Trends")

trend_stat = st.selectbox(
    "Select Stat",
    ["PTS", "AST", "TRB", "FG%", "3P%", "TOV"]
)

fig_trend = px.line(
    player_df,
    x="Year",
    y=trend_stat,
    markers=True,
)

st.plotly_chart(fig_trend)

# ----------------------------
# => Advanced Stats Table
# ----------------------------
st.markdown("### 📊 Season Breakdown")

cols_to_show = [
    "Year", "Team", "G", "MP",
    "PTS", "AST", "TRB",
    "FG%", "3P%", "FT%",
    "STL", "BLK", "TOV"
]

st.dataframe(
    player_df[cols_to_show].style.format({
        "FG%": "{:.3f}",
        "3P%": "{:.3f}",
        "FT%": "{:.3f}",
    })
)

# ----------------------------
# => Awards
# ----------------------------
if isinstance(season_df["Awards"], str) and season_df["Awards"].strip():
    st.success(f"🏆 Awards: {season_df['Awards']}")
