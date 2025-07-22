import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
from pyproj import Transformer

st.set_page_config(page_title="Análisis Exploratorio", layout="wide")
st.title("🗺️ Análisis Exploratorio Final - Accidentes en Madrid")

# =======================
# Carga y transformación
# =======================

@st.cache_data
def load_data():
    return pd.read_csv("data/datos_madrid.csv", encoding='latin1')

# Transformador de coordenadas: UTM → LatLon
transformer = Transformer.from_crs("epsg:25830", "epsg:4326", always_xy=True)

def utm_to_latlon(x, y):
    lon, lat = transformer.transform(x, y)
    return lon, lat

df = load_data()

# =======================
# Limpieza de datos
# =======================
df = df[df["coordenada_x_utm"] > 0]
df["positiva_alcohol"] = df["positiva_alcohol"].fillna("N")
df["lesividad"] = df["lesividad"].fillna("No registrada")
df["fecha"] = pd.to_datetime(df["fecha"], errors='coerce')
df["hora"] = df["hora"].str.extract(r'(\d{1,2})')[0].astype(float)
df["dia_semana"] = df["fecha"].dt.day_name()
df["rango_edad"] = df["rango_edad"].fillna("Desconocido")
df["edad"] = df["rango_edad"].str.extract("(\d+)")[0].astype(float)

# =======================
# Filtros laterales
# =======================
st.sidebar.title("🔍 Filtros")
tipo_acc = st.sidebar.multiselect("Tipo de Accidente", df["tipo_accidente"].dropna().unique(), default=df["tipo_accidente"].dropna().unique())
alcohol = st.sidebar.selectbox("Con Alcohol", ["Todos", "S", "N"])
lesiv = st.sidebar.selectbox("Gravedad", ["Todas"] + sorted(df["lesividad"].unique()))

filtered_df = df[df["tipo_accidente"].isin(tipo_acc)]
if alcohol != "Todos":
    filtered_df = filtered_df[filtered_df["positiva_alcohol"] == alcohol]
if lesiv != "Todas":
    filtered_df = filtered_df[filtered_df["lesividad"] == lesiv]

if filtered_df.empty:
    st.warning("⚠️ No se encontraron datos con los filtros seleccionados. Ajusta los filtros para visualizar resultados.")
    st.stop()

# =======================
# Indicadores
# =======================
st.markdown("### 📊 Indicadores Generales")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Accidentes", len(filtered_df))
with col2:
    st.metric("% Alcohol", f"{(filtered_df['positiva_alcohol'] == 'S').mean()*100:.1f}%")
with col3:
    st.metric("% Heridos", f"{filtered_df['lesividad'].str.contains('herido', case=False).mean()*100:.1f}%")
with col4:
    st.metric("Edad Media", f"{filtered_df['edad'].mean():.1f} años")

# =======================
# Mapa
# =======================
st.markdown("### 🌍 Mapa de Accidentes")

with st.spinner("Cargando mapa 3D con coordenadas geográficas..."):
    # Conversión de coordenadas UTM → LatLon
    def safe_utm_to_latlon(row):
        try:
            lon, lat = utm_to_latlon(row["coordenada_x_utm"], row["coordenada_y_utm"])
            return pd.Series([lon, lat])
        except:
            return pd.Series([np.nan, np.nan])

    latlon_coords = filtered_df.apply(safe_utm_to_latlon, axis=1)

    if latlon_coords.shape[1] == 2:
        latlon_coords.columns = ["lon", "lat"]
        filtered_df = pd.concat([filtered_df.reset_index(drop=True), latlon_coords], axis=1)
        filtered_df = filtered_df.dropna(subset=["lat", "lon"])
    else:
        st.warning("⚠️ No se pudieron convertir las coordenadas con los filtros actuales.")
        st.stop()


    # Crear capa Pydeck
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=filtered_df,
        get_position='[lon, lat]',
        get_radius=70,
        get_color='[200, 30, 0, 160]',
        pickable=True
    )

    view = pdk.ViewState(latitude=40.4168, longitude=-3.7038, zoom=10)

    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view,
        tooltip={"text": "{tipo_accidente}\n{lesividad}"}
    ))

# =======================
# Gráficos
# =======================
st.markdown("### 📈 Distribuciones")

colg1, colg2 = st.columns(2)
with colg1:
    fig1 = px.histogram(filtered_df, x="hora", nbins=24, title="Accidentes por Hora")
    st.plotly_chart(fig1, use_container_width=True)
with colg2:
    fig2 = px.histogram(filtered_df, x="dia_semana", title="Accidentes por Día de la Semana")
    st.plotly_chart(fig2, use_container_width=True)

colg3, colg4 = st.columns(2)
with colg3:
    fig3 = px.histogram(filtered_df, x="distrito", title="Accidentes por Distrito")
    st.plotly_chart(fig3, use_container_width=True)
with colg4:
    fig4 = px.histogram(filtered_df, x="tipo_accidente", title="Accidentes por Tipo")
    st.plotly_chart(fig4, use_container_width=True)

# Mensaje final
st.success("✅ Análisis completado. Utiliza los filtros para explorar distintos escenarios y extraer insights clave.")
