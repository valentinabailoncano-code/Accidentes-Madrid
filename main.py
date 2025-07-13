# main.py

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Proyecto Estadístico - Valentina Bailon",
    layout="wide",
    page_icon="📊"
)

# Oculta el menú lateral por defecto
hide_menu = """
    <style>
    [data-testid="stSidebar"] {display: none;}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

# Banner superior
col1, col2 = st.columns([1, 5])
with col1:
    st.image("images/evolve_logo.png", width=100)
with col2:
    st.markdown("""
        <h1 style='margin-bottom: 0;'>📊 Análisis Estadístico de Accidentes de Tráfico en Madrid</h1>
        <p style='font-size:18px; color:gray; margin-top: 0;'>Un proyecto académico individual de <strong>Valentina Bailon Cano</strong> · Máster en Data Science & IA · Evolve</p>
    """, unsafe_allow_html=True)

st.markdown("---")

# Descripción extendida
st.markdown("""
### 🎯 Objetivo del Proyecto

Este proyecto tiene como finalidad aplicar los conocimientos fundamentales de estadística y probabilidad para analizar una base de datos real sobre accidentes de tráfico en la ciudad de Madrid. A través de una aplicación interactiva en Streamlit, se exploran distintos enfoques analíticos combinando cálculo manual, simulaciones, distribuciones teóricas, inferencias estadísticas y visualización de datos.


### 📂 Contenido de la Aplicación

- Medidas descriptivas manuales y con librerías
- Detección de outliers mediante IQR y Z-score
- Simulaciones de eventos reales como accidentes con alcohol
- Comparación con distribuciones teóricas (Normal, Binomial, Poisson)
- Construcción de intervalos de confianza para medias y proporciones
- Pruebas de hipótesis (T-test, Chi-cuadrado, ANOVA)
- Correlaciones (Pearson, Spearman, Kendall)
- Análisis exploratorio final con mapa interactivo y filtros dinámicos


### 🛠️ Tecnologías Utilizadas

- Python · pandas · numpy · scipy · plotly · streamlit · pydeck · pyproj
- Visual Studio Code · Git · GitHub


### 📌 Cómo Navegar

Puedes explorar todas las secciones del proyecto a través del menú lateral izquierdo.
Si estás en Streamlit Cloud y no ves el menú, utiliza el icono de la flecha 📂 para abrirlo.

---

💡 *Este proyecto está diseñado para demostrar el dominio estadístico, analítico y visual en un entorno real y profesional.*
""")
