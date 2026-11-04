import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Análise de veículos",
    layout="wide"
)

st.title("Análise de anúncios de veículos")

df = pd.read_csv("vehicles_us.csv")

st.write("Explore os dados dos anúncios de veículos por meio dos gráficos abaixo.")

if st.button("Mostrar histograma da quilometragem"):
    fig = px.histogram(
        df,
        x="odometer",
        nbins=50,
        title="Distribuição da quilometragem dos veículos"
    )
    st.plotly_chart(fig, width="stretch")

if st.button("Mostrar gráfico de dispersão"):
    fig = px.scatter(
        df,
        x="odometer",
        y="price",
        title="Relação entre quilometragem e preço",
        labels={
            "odometer": "Quilometragem",
            "price": "Preço"
        }
    )
    st.plotly_chart(fig, width="stretch")