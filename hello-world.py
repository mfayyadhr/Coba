import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

# Load cleaned data
all_df = pd.read_csv("all_data.csv")

# plot number of daily orders (2021)
 
st.header('Air Quality Dashboard :dash:')
st.subheader("Worst Air Quality by Air Pollutants")
 
fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(21, 14))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x='PM2.5', y='station', data=all_df.sort_values(by="PM2.5", ascending=False), palette=colors, ax=ax[0, 0])
ax[0, 0].set_ylabel(None)
ax[0, 0].set_xlabel(None)
ax[0, 0].set_title("Worst Air Quality by PM2.5", loc="center", fontsize=15)
ax[0, 0].tick_params(axis ='y', labelsize=12)

sns.barplot(x='SO2', y='station', data=all_df.sort_values(by="SO2", ascending=False), palette=colors, ax=ax[1, 0])
ax[1, 0].set_ylabel(None)
ax[1, 0].set_xlabel(None)
ax[1, 0].set_title("Worst Air Quality by SO2", loc="center", fontsize=15)
ax[1, 0].tick_params(axis ='y', labelsize=12)

sns.barplot(x='CO', y='station', data=all_df.sort_values(by="CO", ascending=False), palette=colors, ax=ax[2, 0])
ax[2, 0].set_ylabel(None)
ax[2, 0].set_xlabel(None)
ax[2, 0].set_title("Worst Air Quality by CO", loc="center", fontsize=15)
ax[2, 0].tick_params(axis ='y', labelsize=12)

sns.barplot(x="PM10", y='station', data=all_df.sort_values(by="PM10", ascending=False), palette=colors, ax=ax[0, 1])
ax[0, 1].set_ylabel(None)
ax[0, 1].set_xlabel(None)
ax[0, 1].invert_xaxis()
ax[0, 1].yaxis.set_label_position("right")
ax[0, 1].yaxis.tick_right()
ax[0, 1].set_title("Worst Air Quality by PM10", loc="center", fontsize=15)
ax[0, 1].tick_params(axis='y', labelsize=12)

sns.barplot(x="NO2", y='station', data=all_df.sort_values(by="NO2", ascending=False), palette=colors, ax=ax[1, 1])
ax[1, 1].set_ylabel(None)
ax[1, 1].set_xlabel(None)
ax[1, 1].invert_xaxis()
ax[1, 1].yaxis.set_label_position("right")
ax[1, 1].yaxis.tick_right()
ax[1, 1].set_title("Worst Air Quality by NO2", loc="center", fontsize=15)
ax[1, 1].tick_params(axis='y', labelsize=12)

sns.barplot(x="O3", y='station', data=all_df.sort_values(by="O3", ascending=False), palette=colors, ax=ax[2, 1])
ax[2, 1].set_ylabel(None)
ax[2, 1].set_xlabel(None)
ax[2, 1].invert_xaxis()
ax[2, 1].yaxis.set_label_position("right")
ax[2, 1].yaxis.tick_right()
ax[2, 1].set_title("Worst Air Quality by O3", loc="center", fontsize=15)
ax[2, 1].tick_params(axis='y', labelsize=12)
 
st.pyplot(fig)

st.caption('Copyright © Muhammad Fayyadh Rifqi 2024')
