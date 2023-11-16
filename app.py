import streamlit as st
from PIL import Image

st.title('Mi primera Aplicación')

st.header("En este espacio comienzo a desarrollar mis aplicaciones para Interfaces Multimodales")
st.write('Carlos Benitez')
image = Image.open('broccoli-8174625.jpg')

st.image(image, caption= 'Interfaces Multimodales')

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto!')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que modalidad es la principal de tu interfaz", ('Visual','Auditiva','Táctil'))
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'Auditiva':
    st.write('La audición es fundamental para tu interfaz')
  if modo == 'Táctil':
    st.write('El tacto es fundamental para tu interfaz')

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
