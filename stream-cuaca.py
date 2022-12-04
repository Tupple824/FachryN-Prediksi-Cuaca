import pickle
import streamlit as st

# load save model
model = pickle.load(open('weather.sav', 'rb'))

# Judul Untuk Web
st.title('Data Mining Prediksi Cuaca')
st.text('Nama   : Fachry Nurfaidzi')
st.text('Nim    : 191351143')
st.text('Matkul : Business Intelligence')
st.text ('Precipitation =  Proses Mencairnya Awan Akibat Pengaruh Suhu Udara Yang Tinggi')

# Form Input
precipitation = st.number_input('Masukan Jumlah Presipitasi Dengan range 0 - 55.9)')

temp_max  = st.slider('Masukan Maksimal Temperatur(T-Max', -1.6, 35.6)

temp_min = st.slider('Masukan Minimal Temperatur(T-Min', -7.1, 18.3)

wind  = st.slider('Masukan Kecepatan Angin (Wind Speed', 0.4, 9.5)


# kode Prediksi
weather_diagnosis =''

#Button Prediksi
if st.button('Prediksi cuaca Hari Ini'):
    weather_prediction = model.predict([[precipitation,temp_max,temp_min,wind]])

    if(weather_prediction[0]==0):
        weather_diagnosis = ' Cuaca Hari Ini Akan Gerimis'
    elif(weather_prediction[0]==1):
        weather_diagnosis = 'Cuaca Hari Ini Akan Hujan'
    elif(weather_prediction[0]==2):
        weather_diagnosis = 'Cuaca Hari Ini Akan Panas'
    elif(weather_prediction[0]==3):
        weather_diagnosis = 'Cuaca Hari Ini Akan Turun Salju'
    else:
        weather_diagnosis = 'Cuaca Hari Ini Akan Bekabut'
st.success(weather_diagnosis)