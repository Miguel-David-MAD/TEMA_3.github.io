import pandas as pd
import streamlit as st
import plotly.express as px

st.title('WalMart USA App')

DATA_URL = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

df = load_data()

st.header('Gráficas')
st.write('Mostrar información de la base de datos de WalMart USA representada en diferentes tipos de gráficas.')

fig1 = px.bar(df, x='Sub-Category', color='Segment', title='Gráfico de barras de subcategorías más compradas subcategorizado en sus segmentos', color_discrete_sequence=px.colors.qualitative.D3_r).update_traces(dict(marker_line_width=0))
st.write(fig1)

fig2 = px.pie(df, 'Region', title='Gráfico de pastel de regiones que compran productos', color_discrete_sequence=px.colors.qualitative.Bold)
st.write(fig2)

fig3 = px.histogram(df, x='Profit', color='Ship Mode', title='Gráfico de histograma de las ganancias de las ventas categorizadas por el modo de envío', nbins=200)
st.write(fig3)