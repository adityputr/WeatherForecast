import streamlit as st
import pandas as pd
import joblib

# Memuat model dari file .sav
model = joblib.load('weather_predict_model.sav')

# Judul aplikasi
st.title('Prediksi Cuaca: 🌨️ atau 🌤️?')

# Input dari pengguna
temperature = st.number_input('Enter Temperature (°C)', min_value=-50.0, max_value=50.0, value=18.0)
humidity = st.number_input('Enter Humidity (%)', min_value=0, max_value=100, value=80)
wind_speed = st.number_input('Enter Wind Speed (km/h)', min_value=0, max_value=200, value=10)
cloud_cover = st.number_input('Enter Cloud Cover (%)', min_value=0, max_value=100, value=50)
pressure = st.number_input('Enter Pressure (hPa)', min_value=800.0, max_value=1100.0, value=1010.0)

# Mengubah input menjadi DataFrame agar sesuai dengan fitur model
input_data = pd.DataFrame([[temperature, humidity, wind_speed, cloud_cover, pressure]],
                          columns=['Temperature', 'Humidity', 'Wind_Speed', 'Cloud_Cover', 'Pressure'])

# Prediksi berdasarkan input
prediction = model.predict(input_data)

# Menampilkan hasil prediksi dengan tampilan besar dan center
if prediction[0] == 1:
    result_text = "🌨️ Rain 🌨️"
    color = "blue"
else:
    result_text = "🌤️ No Rain 🌤️"
    color = "green"

st.markdown(
    f"""
    <div style="text-align: center; margin-top: 50px;">
        <h1 style="font-size: 60px; color: {color};">{result_text}</h1>
    </div>
    """,
    unsafe_allow_html=True
)
