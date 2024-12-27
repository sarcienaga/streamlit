import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import plotly.graph_objects as go
#from bokeh.plotting import figure
#from bokeh.models import ColumnDataSource

gsheetid='1K3bKjgQQlUyq1eID8TruBGmejf6co0P2t8ZX99Q1Srk'
sheetid='0'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetid}&format'
#st.write('Monitor de Humedad')

# URL de las animaciones Lottie
lottie_url1 = "https://assets3.lottiefiles.com/packages/lf20_0apkn3k1.json"
lottie_url2 = "https://lottie.host/3a99854b-b914-4b58-94b8-d3f9c7ed1dac/QWCSox045L.json"

with st.container():
  # Subheader centrado usando HTML y CSS
  st.markdown(
      """
      <style>
        .centrar-texto {
            text-align: center;
        }
      </style>
      <h2 class="centrar-texto">Dashboard Smart Home con Python</h2>
      """,
      unsafe_allow_html=True
  )
  st_lottie(lottie_url1, height=100, key="coding1")
  
with st.container():
    #st.header("Objetivo")
    st.write(
      """
        Sensando valores desde un GPIO del ESP32 programado en Micropython, subirlos a la nube en tiempo real,
        a una planilla de Google Sheets. Publicar los mismos en una web programada en Python utilizando Streamlit Community Cloud.
      """
    )

@st.fragment(run_every=2)
def cargarDatos(url):
    # Cargar el DataFrame desde un archivo CSV
    df = pd.read_csv(url)

    # Asegúrate de que la columna 'Fecha' sea de tipo datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    # Obtener el último valor leído desde el DataFrame
    ultimo_valor = df['Humedad'].iloc[-1]
    
    # Crear un gráfico Basic Gauge con Plotly
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = ultimo_valor,  # Se puedes mostrar también un promedio -> value = df['tu_columna'].mean() 
        #title = {'text': "GPIO 36"},
        gauge = {
            'axis': {'range': [None, 4095]},  # Ajusta el rango según tus necesidades
            'steps': [
                {'range': [0, 200], 'color': "lightgray"},
                {'range': [200, 500], 'color': "gray"},
                {'range': [500, 1000], 'color': "blue"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 750  # Ajusta el valor del umbral según tus necesidades
            }
        }
    ))
    # Definir el ancho y el alto del gráfico
    fig.update_layout(width=300, height=300)
    # Publicar el gráfico en Streamlit
    st.plotly_chart(fig)

with st.container():
  #st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    cargarDatos(url)
  with right_column:
    # Centrar título en la columna y poner la animación de Lottie
    st.markdown(
      """
      <style>
        .centrar-texto {
            text-align: center;
        }
      </style>
      <h3 class="centrar-texto"><i>Ioting con Python</i></h3>
      """,
      unsafe_allow_html=True
   )
    st_lottie(lottie_url2, height=200, key="coding2")

    