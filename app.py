import streamlit as st
from PIL import Image

st.title('Luces inteligentes con MQTT')

st.header("Este es uno de los usos que se le puede dar al protocolo MQTT")

image = Image.open('broccoli-8174625.jpg')

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

st.subheader("Uso de Botones")
if st.button('Presiona el Botón'):
  st.write('Gracias por presionar')
else:
  st.write('No has presionado aún')

st.subheader("Selectbox")
in_mod = st.selectbox(
  "Selecciona la modalidad",
  ("Audio","Visual","Háptico"),
)
if in_mod =="Audio":
  set_mod = "Reproducir audio"
elif in_mod == "Visual":
  set_mod = "Reproducir video"
elif in_mod == "Háptico":
  set_mod = "Activar Vibración"
st.write(" La acción es: ", set_mod)


with st.sidebar:
  st.subheader("Configura la modalidad")
  mod_radio = st.radio(
    "Escoge la modalidad a usar",
    ("Visual", "Auditiva", "Háptica")
  )

st.write('Hecho por Julian Andres Mazo')
