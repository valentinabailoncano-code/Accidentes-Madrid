# pages/5_Intervalos_Confianza.py

import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.graph_objects as go

st.title("Intervalos de Confianza - Estimaciones con Incertidumbre")

@st.cache_data

def load_data():
    return pd.read_csv("data/datos_madrid.csv", encoding='latin1')

df = load_data()

# Procesamiento
st.markdown("""
Se construyen intervalos de confianza (IC) para diferentes parámetros poblacionales
utilizando los datos muestrales. Se aplican fórmulas clásicas de IC para medias y proporciones.
""")

df = df[df["rango_edad"] != "Desconocido"]
df["edad"] = df["rango_edad"].str.extract("(\d+)")[0].astype(float)
df["positiva_alcohol"] = df["positiva_alcohol"].fillna("N")
df["sexo"] = df["sexo"].fillna("Desconocido")

### 1. IC para media de edad (95%)
st.subheader("1. IC para la media de edad")
edades = df["edad"].dropna()
media = edades.mean()
std = edades.std()
n = len(edades)
error = stats.t.ppf(0.975, df=n-1) * std / np.sqrt(n)

st.write(f"Media muestral: {media:.2f} | IC 95%: [{media-error:.2f}, {media+error:.2f}]")

### 2. IC para proporción de positivos en alcohol
st.subheader("2. IC para proporción de positivos en alcohol")
positivos = (df["positiva_alcohol"] == "S").sum()
N = len(df)
p_hat = positivos / N
z = stats.norm.ppf(0.975)
error_p = z * np.sqrt(p_hat * (1 - p_hat) / N)

st.write(f"Proporción muestral: {p_hat:.4f} | IC 95%: [{p_hat - error_p:.4f}, {p_hat + error_p:.4f}]")

### 3. IC comparado entre dos distritos
st.subheader("3. IC de proporción de alcohol en dos distritos")
d1, d2 = st.selectbox("Distrito 1", df["distrito"].dropna().unique()), st.selectbox("Distrito 2", df["distrito"].dropna().unique())

def ic_proporcion(df, distrito):
    sub = df[df["distrito"] == distrito]
    n = len(sub)
    p = (sub["positiva_alcohol"] == "S").mean()
    err = z * np.sqrt(p * (1 - p) / n)
    return p, p - err, p + err

p1, l1, u1 = ic_proporcion(df, d1)
p2, l2, u2 = ic_proporcion(df, d2)

fig = go.Figure()
fig.add_trace(go.Scatter(x=[d1, d2], y=[p1, p2],
                         error_y=dict(type='data', array=[p1 - l1, p2 - l2], visible=True),
                         mode='markers+text', text=[f"{p1:.3f}", f"{p2:.3f}"], textposition='top center'))
fig.update_layout(title="Comparación de IC para alcohol entre dos distritos",
                  yaxis_title="Proporción estimada", xaxis_title="Distrito")
st.plotly_chart(fig, use_container_width=True)

### 4. IC de proporción de accidentes graves
st.subheader("4. IC para proporción de accidentes graves")
graves = df["lesividad"].fillna("").str.lower().str.contains("grave")
pg = graves.mean()
errg = z * np.sqrt(pg * (1 - pg) / len(df))
st.write(f"Proporción de accidentes graves: {pg:.4f} | IC 95%: [{pg - errg:.4f}, {pg + errg:.4f}]")

### 5. IC para media de edad por género
st.subheader("5. IC para media de edad por sexo")
sexo_sel = st.selectbox("Selecciona sexo", df["sexo"].unique())
subsexo = df[df["sexo"] == sexo_sel]["edad"]
ms = subsexo.mean()
ss = subsexo.std()
ns = len(subsexo)
errs = stats.t.ppf(0.975, df=ns-1) * ss / np.sqrt(ns)
st.write(f"Media: {ms:.2f} | IC 95%: [{ms - errs:.2f}, {ms + errs:.2f}]")

st.success("Intervalos de confianza calculados correctamente para distintos tipos de datos.")
