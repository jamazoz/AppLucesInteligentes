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
broker = "broker.mqttdashboard.com"
port = 1883
MQTT_TOPIC = "luzenvio"

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
    client1.on_publish = on_publish                            
    client1.connect(broker,port)  
    mensaje= "ON"
    ret= client1.publish("luzcasa", mensaje)  
    st.write('Gracias por presionar')

with col2:
  st.subheader("Apagar las luces")
  if st.button('Presiona el Botón para apagar'):
    client1.on_publish = on_publish                            
    client1.connect(broker,port)  
    mensaje= "OFF"
    ret= client1.publish("luzcasa", mensaje)
    st.write('Gracias por presionar')

#Codigo copiado rec. texto 
st.write("Toca el Botón y habla ")

stt_button = Button(label=" Inicio ", width=200)

stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
 
    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_TEXT" in result:
        st.write(result.get("GET_TEXT"))
        client1.on_publish = on_publish                            
        client1.connect(broker,port)  
        message =json.dumps({"Act1":result.get("GET_TEXT").strip()})
        ret= client1.publish("voice_ctrl", message)

    
    try:
        os.mkdir("temp")
    except:
        pass

st.write('Hecho por Julian Andres Mazo')
