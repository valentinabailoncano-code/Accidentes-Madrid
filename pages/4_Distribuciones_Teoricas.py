# pages/4_Distribuciones_Teoricas.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import norm, poisson

st.title("Distribuciones Teóricas vs Distribuciones Reales")

@st.cache_data

def load_data():
    return pd.read_csv("data/datos_madrid.csv", encoding='latin1')

df = load_data()

# Preparar datos de edad
df = df[df["rango_edad"] != "Desconocido"]
df["edad"] = df["rango_edad"].str.extract("(\d+)")[0].astype(float)
edades = df["edad"].dropna().tolist()

# Preparar datos por hora
df["hora"] = df["hora"].str.extract(r'(\d{1,2})')[0].dropna()
df["hora"] = pd.to_numeric(df["hora"], errors='coerce')
horas = df["hora"].dropna().astype(int)

st.markdown("""
En esta sección comparamos distribuciones empíricas con modelos teóricos (normal, Poisson, binomial).
Esto permite validar si los datos reales siguen patrones estocásticos esperados.
""")

### Distribución de Edad vs Normal
st.subheader("1. Edad - Comparación con Distribución Normal")

mu = np.mean(edades)
sigma = np.std(edades)
x_vals = np.linspace(min(edades), max(edades), 100)
normal_vals = norm.pdf(x_vals, mu, sigma)

fig1 = go.Figure()
fig1.add_trace(go.Histogram(x=edades, histnorm='probability density', name='Datos Reales', opacity=0.6))
fig1.add_trace(go.Scatter(x=x_vals, y=normal_vals, mode='lines', name='Distribución Normal'))
fig1.update_layout(title="Edad vs Normal", xaxis_title="Edad", yaxis_title="Densidad")
st.plotly_chart(fig1, use_container_width=True)

### Poisson - Accidentes por Hora
st.subheader("2. Accidentes por Hora vs Distribución Poisson")
hora_counts = horas.value_counts().sort_index()
hora_mean = hora_counts.mean()

poisson_vals = poisson.pmf(k=hora_counts.index, mu=hora_mean)

fig2 = go.Figure()
fig2.add_trace(go.Bar(x=hora_counts.index, y=hora_counts.values, name="Reales"))
fig2.add_trace(go.Scatter(x=hora_counts.index, y=poisson_vals * sum(hora_counts.values),
                          mode='lines+markers', name="Poisson ajustada"))
fig2.update_layout(title="Accidentes por Hora vs Poisson", xaxis_title="Hora", yaxis_title="Frecuencia")
st.plotly_chart(fig2, use_container_width=True)

### Variable Binomial - Alcohol
st.subheader("3. Consumo de Alcohol - Ajuste Binomial")
df["positiva_alcohol"] = df["positiva_alcohol"].fillna("N")
df["alcohol"] = df["positiva_alcohol"].map(lambda x: 1 if x == "S" else 0)
total = len(df)
successes = df["alcohol"].sum()
p_alcohol = successes / total

sim_binomial = np.random.binomial(n=1, p=p_alcohol, size=1000)
fig3 = px.histogram(sim_binomial, nbins=2, title="Simulación Binomial - Alcohol (0 = No, 1 = Sí)")
st.plotly_chart(fig3, use_container_width=True)

st.write(f"Probabilidad empírica de positivo en alcohol: {p_alcohol:.4f}")

st.success("La comparación visual nos permite evaluar cuán bien se ajustan los datos reales a modelos clásicos.")
