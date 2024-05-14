import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from gtts import gTTS
import io
import base64


Tampaknya menggunakan pygame atau pyaudio di lingkungan Streamlit Cloud bisa menyebabkan masalah karena keterbatasan lingkungan. Oleh karena itu, kita perlu menggunakan pendekatan alternatif yang tidak memerlukan inisialisasi mixer audio di sisi server.

Streamlit tidak mendukung pemutaran audio secara langsung dari server, namun Anda dapat mengintegrasikan pemutaran audio menggunakan elemen HTML. Misalnya, Anda dapat menggunakan gTTS untuk membuat file audio dan kemudian mengunggah file tersebut ke Streamlit untuk diputar menggunakan HTML.

Berikut adalah contoh bagaimana melakukannya:

Menggunakan gTTS untuk menghasilkan file audio.
Menggunakan elemen HTML untuk memutar file audio di Streamlit.
Berikut adalah kode yang dimodifikasi:

python
Salin kode
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from gtts import gTTS
import io
import base64

# Function to convert text to speech and generate audio file
def text_to_speech(text):
    tts = gTTS(text=text, lang='id')  # Using Indonesian language
    audio_bytes = io.BytesIO()
    tts.save("audio.mp3")
    return "audio.mp3"

# Function to play audio in streamlit using HTML
def play_audio(audio_file):
    audio_placeholder = st.empty()
    audio_placeholder.markdown(f"""
        <audio autoplay="true">
        <source src="data:audio/mp3;base64,{base64.b64encode(open(audio_file, "rb").read()).decode()}" type="audio/mp3">
        </audio>
        """, unsafe_allow_html=True)

# Menampilkan teks 
st.subheader("Visualisasi dari Data tips.csv")

# Text-to-speech untuk subheader
audio_file = text_to_speech("Visualisasi dari Data tips.csv")
play_audio(audio_file)

st.write("Dhavina Ocxa Dwiyantie")
st.write("21082010136")

# 1
# reading the database
data = pd.read_csv("https://raw.githubusercontent.com/dhavinaocxa/davis-2024/main/tips.csv")

st.subheader("")
st.subheader("Scatter Plot")
# Scatter plot with day against tip
fig, ax = plt.subplots()
scatter = ax.scatter(data['day'], data['tip'], c=data['size'], s=data['total_bill'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

plt.colorbar(scatter)

st.pyplot(fig)

st.subheader("")
st.subheader("Line Chart")
# 3
# plotting the scatter chart
fig = px.line(data, y='tip', color='sex')

# showing the plot
st.plotly_chart(fig)

st.subheader("")
st.subheader("Line Plot")
# 2
# draw lineplot
fig, ax = plt.subplots() 
sns.lineplot(x="sex", y="total_bill", data=data, ax=ax)

# showing the plot
st.pyplot(fig)
