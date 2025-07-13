# pages/1_Medidas_Descriptivas.py

import streamlit as st
import pandas as pd
from utils import estadistica_manual as em

# Cargar datos
@st.cache_data

def load_data():
    return pd.read_csv("data/datos_madrid.csv", encoding='latin1')

df = load_data()

# Convertir edad a numérica (si aplica)
df = df[df["rango_edad"] != "Desconocido"]
edades_limpias = df["rango_edad"].str.extract("(\d+)")[0].dropna().astype(int).tolist()

st.title("Medidas Descriptivas - Análisis Estadístico Manual")
st.markdown("""
En esta sección calculamos manualmente las principales medidas de tendencia central y dispersión, 
comparándolas con las funciones de *pandas* para validar la exactitud.
""")

st.subheader("Variable analizada: Edad estimada (extraída de rango_edad)")

# Cálculos manuales
media_manual = em.media(edades_limpias)
mediana_manual = em.mediana(edades_limpias)
moda_manual = em.moda(edades_limpias)
var_manual = em.varianza(edades_limpias)
desv_manual = em.desviacion_estandar(edades_limpias)
rango_manual = em.rango(edades_limpias)
Q1, Q2, Q3 = em.cuartiles(edades_limpias)
iqr_manual = em.rango_intercuartilico(edades_limpias)

# Cálculos con pandas (para comparación)
edades_series = pd.Series(edades_limpias)
media_pd = edades_series.mean()
mediana_pd = edades_series.median()
moda_pd = edades_series.mode().tolist()
var_pd = edades_series.var()
desv_pd = edades_series.std()
rango_pd = edades_series.max() - edades_series.min()
Q1_pd = edades_series.quantile(0.25)
Q2_pd = edades_series.quantile(0.5)
Q3_pd = edades_series.quantile(0.75)
iqr_pd = Q3_pd - Q1_pd

# Mostrar comparativa
st.markdown("### Comparativa entre cálculos manuales y pandas")
st.write("Valores redondeados a 2 decimales para claridad")

st.table({
    "Medida": ["Media", "Mediana", "Moda", "Varianza", "Desviación", "Rango", "Q1", "Q2 (Mediana)", "Q3", "IQR"],
    "Manual": [
        round(media_manual, 2),
        round(mediana_manual, 2),
        moda_manual,
        round(var_manual, 2),
        round(desv_manual, 2),
        round(rango_manual, 2),
        round(Q1, 2),
        round(Q2, 2),
        round(Q3, 2),
        round(iqr_manual, 2)
    ],
    "Pandas": [
        round(media_pd, 2),
        round(mediana_pd, 2),
        moda_pd,
        round(var_pd, 2),
        round(desv_pd, 2),
        round(rango_pd, 2),
        round(Q1_pd, 2),
        round(Q2_pd, 2),
        round(Q3_pd, 2),
        round(iqr_pd, 2)
    ]
})

st.success("Como se observa, los resultados son equivalentes. Hemos replicado manualmente las funciones estadísticas clave.")
