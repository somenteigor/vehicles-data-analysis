import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análise de anúncios de veículos')

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para a quilometragem dos veículos')

    fig = px.histogram(car_data, x='odometer')

    st.plotly_chart(fig, width="stretch")

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão entre quilometragem e preço')

    fig = px.scatter(car_data, x='odometer', y='price')

    st.plotly_chart(fig, width="stretch")
