 # Importing libraries
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import urllib
import matplotlib.image as mpimg
from scipy import stats
from tqdm import tqdm
import streamlit as st

# Sample data, replace this with your actual data
hour_df = pd.read_csv('df.csv')

# Streamlit app
st.set_page_config(page_title="Bike Rental Patterns")

# Create containers for each tab
tab1 = st.container()
tab2 = st.container()

# Aggregate the data to calculate the average number of rentals per season
seasonal_demand = hour_df.groupby('season')['total_count'].mean().reset_index()

# Map the season numbers to names for better readability
season_names = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
seasonal_demand['season'] = seasonal_demand['season'].map(season_names)


# Header
st.title("Based on Season")

# Plotting
plt.figure(figsize=(12, 6), facecolor='white')
plt.title('Average Bicycle Rentals per Season')
sns.barplot(x='season', y='total_count', data=seasonal_demand, palette='coolwarm')
plt.xlabel('Season')
plt.ylabel('Average Number of Rentals')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot using Streamlit
fig = plt.gcf()  # Get the current figure
st.pyplot(fig)

# Explanation
st.write("""
Permintaan persewaan sepeda bervariasi pada musim yang berbeda, dengan Musim Panas dan Musim Gugur menunjukkan rata-rata persewaan yang lebih tinggi dibandingkan Musim Dingin dan Musim Semi.
""")




# Header
st.title("Based on Weekdays and Weekends")


# Group the data by hour and working day status
hourly_rentals = hour_df.groupby(['hour', 'workingday'])['total_count'].mean().unstack()


# Selectbox to choose between "hr" and "workingday"
attribute_option = st.radio("Select Attribute", ["Hour", "Working Day"])


# Plottinh
fig, ax = plt.subplots(figsize=(12, 6), facecolor='white')
ax.plot(hourly_rentals[0], label='Weekend', linestyle='--', marker='o', color='blue')
ax.plot(hourly_rentals[1], label='Working Day', linestyle='-', marker='x', color='red')
ax.set_title('Average Bike Rentals per Hour')
ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Average Number of Rentals')
ax.set_xticks(range(0, 24))
ax.legend()
ax.grid(True)

# Display the plot using Streamlit
st.pyplot(fig)

# Explanation for "hr"

st.write("""
**- Selama hari kerja, terdapat puncak tertinggi dalam penyewaan sepeda pada pagi hari (sekitar pukul 08.00) dan sore hari (sekitar pukul 17.00-18.00), yang setara dengan waktu perjalanan pada umumnya.""")

st.write("""
**- Pada akhir pekan, polanya lebih tersebar dengan peningkatan sewa secara bertahap dari pagi hingga sore, yang mencapai puncaknya sekitar pukul 12.00 hingga 16.00, yang mengindikasikan penggunaan waktu senggang atau rekreasi.""")


















