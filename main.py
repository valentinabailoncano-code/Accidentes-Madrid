import streamlit as st

st.set_page_config(
    page_title="Accidentes de Tráfico en Madrid",
    layout="wide",
    page_icon="🚦"
)

st.markdown("""
<style>
.big-title {
    font-size: 42px;
    font-weight: bold;
    color: #2E4053;
}
.subtitle {
    font-size: 18px;
    color: #555;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🚦 Análisis Estadístico de Accidentes de Tráfico en Madrid</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Proyecto académico individual por <strong>Valentina Bailon Cano</strong> – Máster en Data Science & IA en Evolve</p>', unsafe_allow_html=True)

st.image("images/evolve_logo.png", width=200)

st.markdown("""
Este proyecto analiza datos reales de accidentes en la ciudad de Madrid desde una perspectiva estadística y probabilística.  
Usa el menú lateral para navegar por las distintas secciones: descriptivos, simulaciones, pruebas, visualizaciones, etc.
""")

