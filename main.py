# main.py

import streamlit as st
from PIL import Image

# Oculta el sidebar de Streamlit
st.set_page_config(page_title="Análisis Estadístico", layout="wide", page_icon="📊")
st.markdown("""
    <style>
    [data-testid="stSidebar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# Logo y encabezado superior
col1, col2 = st.columns([1, 5])
with col1:
    st.image("images/evolve_logo.png", width=100)
with col2:
    st.markdown("""
        <h1 style='margin-bottom: 0;'>📊 Análisis Estadístico de Accidentes de Tráfico en Madrid</h1>
        <p style='font-size:18px; color:gray; margin-top: 0;'>Un proyecto académico individual de <strong>Valentina Bailon Cano</strong> · Máster en Data Science & IA · Evolve</p>
    """, unsafe_allow_html=True)

st.markdown("---")

# Menú de navegación personalizado
menu = st.selectbox("Selecciona una sección:", (
    "Inicio",
    "Medidas Descriptivas",
    "Detección de Outliers",
    "Simulaciones",
    "Distribuciones Teóricas",
    "Intervalos de Confianza",
    "Pruebas de Hipótesis",
    "Correlaciones",
    "Análisis Exploratorio"
))

if menu == "Inicio":
    st.markdown("""
### 🎯 Objetivo del Proyecto

Este proyecto tiene como finalidad aplicar los conocimientos fundamentales de estadística y probabilidad para analizar una base de datos real sobre accidentes de tráfico en la ciudad de Madrid. A través de una aplicación interactiva en Streamlit, se exploran distintos enfoques analíticos combinando cálculo manual, simulaciones, distribuciones teóricas, inferencias estadísticas y visualización de datos.

---

### 📂 Contenido de la Aplicación
- Medidas descriptivas manuales y con librerías
- Detección de outliers mediante IQR y Z-score
- Simulaciones de eventos reales como accidentes con alcohol
- Comparación con distribuciones teóricas (Normal, Binomial, Poisson)
- Construcción de intervalos de confianza
- Pruebas de hipótesis (T-test, proporciones, ANOVA)
- Correlaciones (Pearson, Spearman, Kendall)
- Análisis exploratorio final con mapa interactivo

---

### 🛠️ Tecnologías Utilizadas

Python · pandas · numpy · scipy · streamlit · plotly · pydeck · pyproj
    """)

elif menu == "Medidas Descriptivas":
    import pages.1_Medidas_Descriptivas as mod
    mod

elif menu == "Detección de Outliers":
    import pages.2_Deteccion_Outliers as mod
    mod

elif menu == "Simulaciones":
    import pages.3_Simulaciones_Probabilidad as mod
    mod

elif menu == "Distribuciones Teóricas":
    import pages.4_Distribuciones_Teoricas as mod
    mod

elif menu == "Intervalos de Confianza":
    import pages.5_Intervalos_Confianza as mod
    mod

elif menu == "Pruebas de Hipótesis":
    import pages.6_Pruebas_Hipotesis as mod
    mod

elif menu == "Correlaciones":
    import pages.7_Correlaciones as mod
    mod

elif menu == "Análisis Exploratorio":
    import pages.8_Analisis_Exploratorio as mod
    mod
