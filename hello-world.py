import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

# def create_daily_orders_df(df):
#     daily_orders_df = df.resample(rule='D', on='order_date').agg({
#         "order_id": "nunique",
#         "total_price": "sum"
#     })
#     daily_orders_df = daily_orders_df.reset_index()
#     daily_orders_df.rename(columns={
#         "order_id": "order_count",
#         "total_price": "revenue"
#     }, inplace=True)
    
#     return daily_orders_df

# def create_sum_order_items_df(df):
#     sum_order_items_df = df.groupby("product_name").quantity_x.sum().sort_values(ascending=False).reset_index()
#     return sum_order_items_df

# def create_bygender_df(df):
#     bygender_df = df.groupby(by="gender").customer_id.nunique().reset_index()
#     bygender_df.rename(columns={
#         "customer_id": "customer_count"
#     }, inplace=True)
    
#     return bygender_df

# def create_byage_df(df):
#     byage_df = df.groupby(by="age_group").customer_id.nunique().reset_index()
#     byage_df.rename(columns={
#         "customer_id": "customer_count"
#     }, inplace=True)
#     byage_df['age_group'] = pd.Categorical(byage_df['age_group'], ["Youth", "Adults", "Seniors"])
    
#     return byage_df

# def create_bystate_df(df):
#     bystate_df = df.groupby(by="state").customer_id.nunique().reset_index()
#     bystate_df.rename(columns={
#         "customer_id": "customer_count"
#     }, inplace=True)
    
#     return bystate_df

# def create_rfm_df(df):
#     rfm_df = df.groupby(by="customer_id", as_index=False).agg({
#         "order_date": "max", #mengambil tanggal order terakhir
#         "order_id": "nunique",
#         "total_price": "sum"
#     })
#     rfm_df.columns = ["customer_id", "max_order_timestamp", "frequency", "monetary"]
    
#     rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date
#     recent_date = df["order_date"].dt.date.max()
#     rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)
#     rfm_df.drop("max_order_timestamp", axis=1, inplace=True)
    
#     return rfm_df

# Load cleaned data
# all_df = pd.read_csv("all_data.csv")

# datetime_columns = ["order_date", "delivery_date"]
# all_df.sort_values(by="order_date", inplace=True)
# all_df.reset_index(inplace=True)

# for column in datetime_columns:
#     all_df[column] = pd.to_datetime(all_df[column])

# Filter data
# min_date = all_df["order_date"].min()
# max_date = all_df["order_date"].max()

# with st.sidebar:
#     # Menambahkan logo perusahaan
#     st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
#     # Mengambil start_date & end_date dari date_input
#     start_date, end_date = st.date_input(
#         label='Rentang Waktu',min_value=min_date,
#         max_value=max_date,
#         value=[min_date, max_date]
#     )

# main_df = all_df[(all_df["order_date"] >= str(start_date)) & 
#                 (all_df["order_date"] <= str(end_date))]

# st.dataframe(main_df)

# # Menyiapkan berbagai dataframe
# daily_orders_df = create_daily_orders_df(main_df)
# sum_order_items_df = create_sum_order_items_df(main_df)
# bygender_df = create_bygender_df(main_df)
# byage_df = create_byage_df(main_df)
# bystate_df = create_bystate_df(main_df)
# rfm_df = create_rfm_df(main_df)


# plot number of daily orders (2021)
 
st.header('Air Quality Dashboard :dash:')
st.subheader("Worst Air Quality by Air Pollutants")
 
# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
 
# colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
# sns.barplot(x="quantity_x", y="product_name", data=sum_order_items_df.head(5), palette=colors, ax=ax[0])
# ax[0].set_ylabel(None)
# ax[0].set_xlabel("Number of Sales", fontsize=30)
# ax[0].set_title("Best Performing Product", loc="center", fontsize=50)
# ax[0].tick_params(axis='y', labelsize=35)
# ax[0].tick_params(axis='x', labelsize=30)
 
# sns.barplot(x="quantity_x", y="product_name", data=sum_order_items_df.sort_values(by="quantity_x", ascending=True).head(5), palette=colors, ax=ax[1])
# ax[1].set_ylabel(None)
# ax[1].set_xlabel("Number of Sales", fontsize=30)
# ax[1].invert_xaxis()
# ax[1].yaxis.set_label_position("right")
# ax[1].yaxis.tick_right()
# ax[1].set_title("Worst Performing Product", loc="center", fontsize=50)
# ax[1].tick_params(axis='y', labelsize=35)
# ax[1].tick_params(axis='x', labelsize=30)
 
# st.pyplot(fig)

st.caption('Copyright © Dicoding 2023')
