import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('Análisis interactivo de anuncios de autos en EE.UU.') # header

# Casilla para histograma
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Histograma: Distribución de kilometraje (odómetro)')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla para scatterplot
if st.checkbox('Mostrar gráfico de dispersión entre precio y año'):
    st.write('Gráfico de dispersión: Precio vs Año del modelo')
    fig_scatter = px.scatter(car_data, x='model_year', y='price', color='type', hover_data=['model'])
    st.plotly_chart(fig_scatter, use_container_width=True)
