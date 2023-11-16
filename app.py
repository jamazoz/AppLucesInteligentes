import streamlit as st
import paho.mqtt.client as mqtt
from time import sleep
from PIL import Image

#MQTT Config
MQTT_BROKER = os.getenv("broker.mqttdashboard.com")
MQTT_PORT = int(os.getenv("1883"))
MQTT_TOPIC = "luzenvio"
MQTT_USER = os.getenv("")
MQTT_PW = os.getenv("")


st.title('Luces inteligentes con MQTT')

st.header("Este es uno de los usos que se le puede dar al protocolo MQTT")

image = Image.open('CasaInteligente.jpg')

st.image(image, caption= 'Casa int')

st.checkbox('Acepto que mis datos sean usados para mejorar la experiencia de la aplicación')

col1, col2 = st.columns(2)

with col1:
  st.subheader("Encender las luces")
  if st.button('Presiona el Botón'):
    st.write('Gracias por presionar')

with col2:
  st.subheader("Apagar las luces")
  if st.button('Presiona el Botón para apagar'):
    st.write('Gracias por presionar')

st.write('Hecho por Julian Andres Mazo')
