# pages/4_Distribuciones_Teoricas.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.stats import norm, poisson

st.set_page_config(page_title="Distribuciones Teóricas", layout="wide")
st.title("📊 Comparación con Distribuciones Teóricas")

@st.cache_data

def load_data():
    return pd.read_csv("data/datos_madrid.csv", encoding='latin1')

df = load_data()

# Edad
st.markdown("### 1. Edad vs Distribución Normal")
df = df[df["rango_edad"] != "Desconocido"]
df["edad"] = df["rango_edad"].str.extract("(\d+)")[0].astype(float)
edades = df["edad"].dropna()

mu = np.mean(edades)
sigma = np.std(edades)
x_vals = np.linspace(min(edades), max(edades), 100)
y_vals = norm.pdf(x_vals, mu, sigma)

fig = go.Figure()
fig.add_trace(go.Histogram(x=edades, histnorm='probability density', name='Datos reales', opacity=0.6))
fig.add_trace(go.Scatter(x=x_vals, y=y_vals, name='Distribución Normal', mode='lines'))
fig.update_layout(title="Distribución de Edad comparada con Normal",
                  xaxis_title="Edad", yaxis_title="Densidad")
st.plotly_chart(fig, use_container_width=True)

# Hora vs Poisson
st.markdown("### 2. Accidentes por Hora vs Distribución Poisson")
df["hora"] = df["hora"].str.extract(r'(\d{1,2})')[0].astype(float)
horas = df["hora"].dropna().astype(int)
hora_freq = horas.value_counts().sort_index()
media_hora = hora_freq.mean()

poisson_y = poisson.pmf(hora_freq.index, media_hora) * sum(hora_freq)

fig2 = go.Figure()
fig2.add_trace(go.Bar(x=hora_freq.index, y=hora_freq.values, name='Reales'))
fig2.add_trace(go.Scatter(x=hora_freq.index, y=poisson_y, mode='lines+markers', name='Poisson'))
fig2.update_layout(title="Accidentes por Hora vs Poisson",
                   xaxis_title="Hora", yaxis_title="Frecuencia")
st.plotly_chart(fig2, use_container_width=True)

# Alcohol binomial
st.markdown("### 3. Proporción de Alcohol vs Binomial")
df["positiva_alcohol"] = df["positiva_alcohol"].fillna("N")
df["alcohol"] = df["positiva_alcohol"].map(lambda x: 1 if x == "S" else 0)

p_emp = df["alcohol"].mean()
simulacion = np.random.binomial(n=1, p=p_emp, size=1000)

fig3 = go.Figure()
fig3.add_trace(go.Histogram(x=simulacion, nbinsx=2, name='Simulación Binomial'))
fig3.update_layout(title="Simulación Binomial - Alcohol",
                   xaxis_title="0 = No / 1 = Sí", yaxis_title="Frecuencia")
st.plotly_chart(fig3, use_container_width=True)

st.success("Las distribuciones reales muestran buen ajuste parcial con modelos teóricos, pero también desvíos interesantes que justifican el análisis exploratorio.")