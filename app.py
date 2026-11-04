import streamlit as st
import pandas as pd 
import plotly.express as px

st.set_page_config(
    page_title="Análise de veículos",
    layout="wide"
)

st.title("Análise de anúncios de veículos")

df = pd.read_csv("vehicles_us_clean.csv")

st.header("Exploração dos dados")

if st.button("Mostrar histograma da quilometragem"):
    fig_hist = px.histogram(
        df,
        x="odometer",
        title="Distribuição da quilometragem dos veículos",
        nbins=50
    )
    st.plotly_chart(fig_hist, width="stretch")

if st.button("Mostrar gráfico de dispersão"):
    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        title="Relação entre quilometragem e preço dos veículos"
    )
    st.plotly_chart(fig_scatter, width="stretch")