# main.py

import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Análisis Estadístico", layout="wide", page_icon="📊")

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

# Sección de objetivo
st.markdown("### 🎯 Objetivo del Proyecto")
st.markdown("""
Este proyecto tiene como finalidad aplicar los conocimientos fundamentales de estadística y probabilidad para analizar una base de datos real sobre accidentes de tráfico en la ciudad de Madrid.  
A través de una aplicación interactiva en Streamlit, se exploran distintos enfoques analíticos combinando cálculo manual, simulaciones, distribuciones teóricas, inferencias estadísticas y visualización de datos.
""")

# Contenido
st.markdown("---")
st.markdown("### 📂 Contenido de la Aplicación")
st.markdown("""
- **Medidas Descriptivas:** Cálculo manual y automatizado de media, mediana, desviación típica, moda, etc.
- **Detección de Outliers:** Aplicación de métodos IQR y Z-score para identificar valores atípicos.
- **Simulaciones:** Ejemplos reales como accidentes bajo efecto del alcohol o condiciones extremas.
- **Distribuciones Teóricas:** Comparación con distribuciones como Normal, Binomial o Poisson.
- **Intervalos de Confianza:** Cálculo para medias, proporciones y diferencias entre grupos.
- **Pruebas de Hipótesis:** T-test, test de proporciones, ANOVA y más.
- **Correlaciones:** Análisis de dependencias entre variables (Pearson, Spearman, Kendall).
- **Análisis Exploratorio:** Visualizaciones globales y mapa 3D de accidentes por distrito y gravedad.

> 🗺️ **Nota:** La página final incluye un **mapa 3D interactivo** que puede tardar unos segundos en cargarse. Ten paciencia, ¡vale la pena!
""")

# Guía de navegación
st.markdown("---")
st.markdown("### 🧭 Cómo Navegar la App")
st.markdown("""
Usa el menú lateral para moverte entre las diferentes secciones del proyecto.  
Cada una está dedicada a una técnica estadística concreta y contiene visualizaciones interactivas para que puedas explorar los resultados por ti mismo/a.

- El orden está diseñado de forma pedagógica: empieza por las **medidas descriptivas** y termina con el **análisis global y visual**.
- Siéntete libre de interactuar con los filtros, sliders y gráficos para descubrir patrones interesantes en los datos.
""")

# Tecnologías
st.markdown("---")
st.markdown("### 🧪 Tecnologías Utilizadas")
st.markdown("Python · pandas · numpy · scipy · streamlit · plotly · pydeck · pyproj")

# Cierre
st.markdown("---")
st.markdown("##### Proyecto realizado en el marco del Máster en Data Science & Inteligencia Artificial de Evolve · 2025")
