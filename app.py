import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("tips.csv")

# plotting the scatter chart
fig = px.scatter(data, x="day", y="tip", color='sex')

# adding title to the scatter chart
plt.title("Scatter Chart")

# showing the plot
st.pyplot(fig)
