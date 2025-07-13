# pages/2_Deteccion_Outliers.py

import streamlit as st
import pandas as pd
import plotly.express as px
from utils import estadistica_manual as em

st.title("Detección de Outliers - IQR y Z-score")

# Cargar datos
@st.cache_data

def load_data():
    return pd.read_csv("data/datos_madrid.csv", encoding='latin1')

df = load_data()

# Limpiar y transformar la edad
df = df[df["rango_edad"] != "Desconocido"]
df["edad"] = df["rango_edad"].str.extract("(\d+)")[0].dropna().astype(int)
edades = df["edad"].tolist()

st.markdown("""
Aplicamos dos métodos clásicos de detección de valores atípicos:
- **IQR (rango intercuartílico)**
- **Z-score**

Los outliers detectados se muestran también en los gráficos.
""")

# Detectar outliers
outliers_iqr = em.detectar_outliers_iqr(edades)
outliers_z = em.detectar_outliers_zscore(edades, umbral=2.5)

st.subheader("Resultados Numéricos")
st.write(f"Número total de registros: {len(edades)}")
st.write(f"Outliers por IQR: {len(outliers_iqr)}")
st.write(f"Outliers por Z-score (umbral 2.5): {len(outliers_z)}")

# Boxplot
st.subheader("Boxplot de Edad")
fig_box = px.box(df, y="edad", points="outliers", title="Boxplot con Plotly")
st.plotly_chart(fig_box, use_container_width=True)

# Histograma con outliers destacados
st.subheader("Histograma con Outliers (IQR) resaltados")

# Crear columna para marcar si es outlier
df["outlier_iqr"] = df["edad"].apply(lambda x: "Outlier" if x in outliers_iqr else "Normal")

fig_hist = px.histogram(df, x="edad", color="outlier_iqr",
                        barmode="overlay",
                        color_discrete_map={"Normal": "lightblue", "Outlier": "red"},
                        title="Distribución de Edad con Outliers IQR")
st.plotly_chart(fig_hist, use_container_width=True)

st.success("Los valores atípicos fueron identificados con ambos métodos y visualizados de forma clara.")
