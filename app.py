import os
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import time
import glob
import paho.mqtt.client as paho
import json
from gtts import gTTS
from googletrans import Translator
import streamlit as st
from time import sleep
from PIL import Image

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)


#MQTT Config
MQTT_BROKER = os.getenv("broker.mqttdashboard.com")
MQTT_PORT = int(os.getenv("1883"))
MQTT_TOPIC = "luzenvio"
MQTT_USER = os.getenv("")
MQTT_PW = os.getenv("")

client1= paho.Client("GIT-HUB")
client1.on_message = on_message


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
