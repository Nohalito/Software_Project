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

# Dataset :
df = f.load_data()

# Roses are red
# Streamlit is lit
# With this treasure I summon
# Lebron James application
#st.title("NBA Player statistics 🏀")

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="NBA Player Explorer",
    layout="wide",
)

st.title("🏀 NBA Player Explorer")

# ----------------------------
# Load data
# ----------------------------
# df = pd.read_csv("your_data.csv")
# Assumes df already exists

# Ensure proper sorting
df = df.sort_values(["Player", "Year"])

# ----------------------------
# Sidebar filters
# ----------------------------
st.sidebar.header("Filter Player")

player = st.sidebar.selectbox(
    "Select Player",
    sorted(df["Player"].unique())
)

player_df = df[df["Player"] == player]

season = st.sidebar.selectbox(
    "Select Season",
    player_df["Year"].unique()
)

season_df = player_df[player_df["Year"] == season].iloc[0]

# ----------------------------
# Player Header
# ----------------------------
st.subheader(f"{player} — {season}")
st.caption(
    f"Team: {season_df['Team']} | Position: {season_df['Pos']} | Age: {int(season_df['Age'])}"
)

# ----------------------------
# Key Metrics
# ----------------------------
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("PTS", f"{season_df['PTS']:.1f}")
col2.metric("AST", f"{season_df['AST']:.1f}")
col3.metric("TRB", f"{season_df['TRB']:.1f}")
col4.metric("MP", f"{season_df['MP']:.1f}")
col5.metric("G", int(season_df["G"]))

# ----------------------------
# Shooting Efficiency
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

st.plotly_chart(fig_shooting)#, use_container_width=True)

# ----------------------------
# Season Trends
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

st.plotly_chart(fig_trend)#, use_container_width=True)

# ----------------------------
# Advanced Stats Table
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
    })#,
    #use_container_width=True
)

# ----------------------------
# Awards
# ----------------------------
if isinstance(season_df["Awards"], str) and season_df["Awards"].strip():
    st.success(f"🏆 Awards: {season_df['Awards']}")
