import streamlit as st
from PIL import Image

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
  if st.button('Presiona el Botón'):
    st.write('Gracias por presionar')

st.write('Hecho por Julian Andres Mazo')
