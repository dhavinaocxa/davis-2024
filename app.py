import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Menampilkan teks 
st.subheader("VISUALISASI DATA")
st.write("Dhavina Ocxa Dwiyantie (21082010136)")

st.subheader("")
st.subheader("Scatter Plot")
# 1
# reading the database
data = pd.read_csv("https://raw.githubusercontent.com/dhavinaocxa/davis-2024/main/tips.csv")

# Scatter plot with day against tip
fig, ax = plt.subplots()
scatter = ax.scatter(data['day'], data['tip'])

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

# showing the plot
st.pyplot(fig)

st.subheader("")
st.subheader("Line Plot")
# 2
# draw lineplot
fig, ax = plt.subplots() 
sns.lineplot(x="sex", y="total_bill", data=data, ax=ax)

# showing the plot
st.pyplot(fig)

st.subheader("")
st.subheader("Line Chart")
# 3
# plotting the scatter chart
fig = px.line(data, y='tip', color='sex')

# showing the plot
st.plotly_chart(fig)
