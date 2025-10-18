# archivo: dashboard_clima.py

import streamlit as st
import requests
from datetime import datetime

st.title("🌤️ Clima en tiempo real")
st.write("Consulta el clima actual en cualquier ciudad")

# Entrada del usuario
ciudad = st.text_input("Ingresa una ciudad", "Bogotá")

if ciudad:
    # Geocodificar ciudad con Open-Meteo
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad}&count=1&language=es&format=json"
    geo_resp = requests.get(geo_url).json()

    if 'results' in geo_resp:
        lat = geo_resp['results'][0]['latitude']
        lon = geo_resp['results'][0]['longitude']

        # Obtener clima actual
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&current_weather=true&timezone=America/Bogota"
        )
        clima = requests.get(weather_url).json()

        datos = clima['current_weather']
        st.metric("🌡 Temperatura", f"{datos['temperature']}°C")
        st.metric("💨 Viento", f"{datos['windspeed']} km/h")
        st.write("📅 Fecha:", datetime.now().strftime("%d-%m-%Y %H:%M"))
    else:
        st.error("No se encontró la ciudad.")

