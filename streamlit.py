import pandas as pd
import csv
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import streamlit as sl

import streamlit as st

sl.set_page_config(
    page_title="UFO Sightings",
    page_icon=":alien:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': 'https://github.com/srisreedhar/UFO_Sightings'
    }
)

ufo = pd.read_csv(r'D:\Projects\Git\UFO_Sightings\data\ufo_rowlevel_data.csv')


sl.dataframe(ufo)

# with st.sidebar:
#     add_radio = st.radio(
#         "Select a Filter",
#         ("State", "Shape","Country")
#     )

sl.sidebar.header("Select an Option to Filter the Data:")
State = sl.sidebar.multiselect(
    "Select a State:", 
    options = ufo["State"].unique(),
    default = ufo["State"].unique()
)
Shape = sl.sidebar.multiselect(
    "Select the Shape of the UFO:", 
    options = ufo["Shape"].unique(),
    default = ufo["Shape"].unique()
)
Country = sl.sidebar.multiselect(
    "Select the Country:", 
    options = ufo["Country"].unique(),
    default = ufo["Country"].unique()
)












