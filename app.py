import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Menampilkan teks 
st.subheader("VISUALISASI DATA")
st.write("Dhavina Ocxa Dwiyantie (21082010136)")

# 1
# reading the database
data = pd.read_csv("https://raw.githubusercontent.com/dhavinaocxa/davis-2024/main/tips.csv")

# Scatter plot with day against tip
fig, ax = plt.subplots()
scatter = ax.scatter(data['day'], data['tip'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

# showing the plot
st.pyplot(fig)

# 2
# draw lineplot
sns.lineplot(x="sex", y="total_bill", data=data)

# setting the title using Matplotlib
plt.title('Line Plot')

# showing the plot
st.pyplot()

# 3
# plotting the scatter chart
fig = px.line(data, y='tip', color='sex')

# showing the plot
st.plotly_chart(fig)
