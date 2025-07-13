# pages/7_Correlaciones.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr, kendalltau

st.title("Correlaciones entre Variables - Pearson, Spearman, Kendall")

@st.cache_data

def load_data():
    return pd.read_csv("data/datos_madrid.csv", encoding='latin1')

df = load_data()

# Limpieza y codificación para correlación
st.markdown("""
Para calcular correlaciones es necesario convertir variables categóricas a numéricas.

- `lesividad` se codifica de 0 (leve) a 3 (muy grave)
- `positiva_alcohol` se convierte a 1 (positivo) y 0 (negativo)
- Se calcula edad como número desde el rango
""")

# Edad
valid_age = df[df["rango_edad"] != "Desconocido"]
valid_age["edad"] = valid_age["rango_edad"].str.extract("(\d+)")[0].astype(float)

# Alcohol
valid_age["alcohol"] = valid_age["positiva_alcohol"].fillna("N").map(lambda x: 1 if x == "S" else 0)

# Lesividad codificada
def codificar_lesividad(texto):
    if pd.isna(texto): return 0
    texto = texto.lower()
    if "leve" in texto: return 1
    elif "grave" in texto: return 2
    elif "muerto" in texto: return 3
    else: return 0

valid_age["lesividad_cod"] = valid_age["lesividad"].apply(codificar_lesividad)

# Variables para comparar
edad = valid_age["edad"]
lesividad = valid_age["lesividad_cod"]
alcohol = valid_age["alcohol"]

st.subheader("1. Pearson: Edad vs Gravedad (lesividad codificada)")
r1, p1 = pearsonr(edad, lesividad)
st.write(f"Coeficiente de Pearson: {r1:.3f}, p-valor: {p1:.4f}")

st.subheader("2. Spearman: Edad vs Gravedad")
r2, p2 = spearmanr(edad, lesividad)
st.write(f"Spearman rho: {r2:.3f}, p-valor: {p2:.4f}")

st.subheader("3. Kendall: Alcohol vs Lesividad")
r3, p3 = kendalltau(alcohol, lesividad)
st.write(f"Kendall tau: {r3:.3f}, p-valor: {p3:.4f}")

# Matriz de correlación
st.subheader("4. Matriz de Correlación")
variables = valid_age[["edad", "lesividad_cod", "alcohol"]]
corr_matrix = variables.corr(method="pearson")
fig_corr = px.imshow(corr_matrix, text_auto=True, color_continuous_scale="RdBu", title="Matriz de Correlación (Pearson)")
st.plotly_chart(fig_corr, use_container_width=True)

st.success("Las correlaciones permiten evaluar asociaciones lineales o no lineales entre variables relevantes del dataset.")
