# pages/3_Simulaciones_Probabilidad.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random

st.title("Simulaciones de Probabilidad - Análisis Estocástico")

@st.cache_data

def load_data():
    return pd.read_csv("data/datos_madrid.csv", encoding='latin1')

df = load_data()

# Limpiar datos relevantes
df["positiva_alcohol"] = df["positiva_alcohol"].fillna("N")
df = df[df["rango_edad"] != "Desconocido"]
df["edad"] = df["rango_edad"].str.extract("(\d+)")[0].astype(float)
df["lesividad"] = df["lesividad"].fillna("No registrada")
df["fecha"] = pd.to_datetime(df["fecha"], errors='coerce')
df["dia_semana"] = df["fecha"].dt.day_name()

st.markdown("""
A continuación se presentan **5 simulaciones realistas** sobre accidentes de tráfico en Madrid.
Las simulaciones permiten estimar probabilidades mediante modelos de conteo, binomiales, Poisson y escenarios aleatorios.
""")

### Ejemplo 1
st.subheader("1. Probabilidad de 3 o más accidentes con alcohol en un día")

df_dias = df.groupby("fecha")["positiva_alcohol"].apply(lambda x: (x == "S").sum())
mean_alcohol_day = df_dias.mean()

simulaciones = [sum(np.random.rand(int(mean_alcohol_day*2)) < (mean_alcohol_day/10)) for _ in range(1000)]
mayores_3 = sum(1 for x in simulaciones if x >= 3)

st.write(f"Promedio real de accidentes con alcohol por día: {mean_alcohol_day:.2f}")
st.write(f"Probabilidad estimada (simulada) de ≥3 en un día: {mayores_3/1000:.3f}")
fig1 = px.histogram(simulaciones, nbins=15, title="Distribución simulada de accidentes con alcohol por día")
st.plotly_chart(fig1, use_container_width=True)

### Ejemplo 2
st.subheader("2. Simulación de 1000 días de accidentes graves")
graves = df["lesividad"].str.lower().str.contains("grave").sum()
total = len(df)
p_grave = graves / total

dias = 1000
simulacion_graves = [sum(np.random.rand(100) < p_grave) for _ in range(dias)]
fig2 = px.histogram(simulacion_graves, nbins=30, title="Accidentes graves simulados en 1000 días (100 por día)")
st.plotly_chart(fig2, use_container_width=True)
st.write(f"Probabilidad estimada de accidente grave: {p_grave:.4f}")

### Ejemplo 3
st.subheader("3. Modelo Poisson - Accidentes por distrito/hora")
distrito = st.selectbox("Selecciona un distrito para simular", df["distrito"].dropna().unique())
count_distrito = df[df["distrito"] == distrito].shape[0]
df_distrito = df[df["distrito"] == distrito]
horas = df_distrito["hora"].str.extract(r'(\d{1,2})')[0].dropna().astype(int)
prom_por_hora = horas.value_counts().mean()

simulacion_poisson = np.random.poisson(prom_por_hora, size=500)
fig3 = px.histogram(simulacion_poisson, nbins=20, title=f"Modelo Poisson: Accidentes por hora en {distrito}")
st.plotly_chart(fig3, use_container_width=True)
st.write(f"Media empírica por hora: {prom_por_hora:.2f}")

### Ejemplo 4
st.subheader("4. Probabilidad de heridos si el conductor tiene <25 años")
df_jovenes = df[df["edad"] < 25]
heridos_jovenes = df_jovenes["lesividad"].str.lower().str.contains("herido").sum()
p_joven_herido = heridos_jovenes / len(df_jovenes)

st.write(f"Probabilidad estimada de heridos en <25 años: {p_joven_herido:.3f}")
sim_heridos = [random.random() < p_joven_herido for _ in range(200)]
fig4 = px.histogram(sim_heridos, title="Simulación de 200 jóvenes y heridos (True = hubo herido)")
st.plotly_chart(fig4, use_container_width=True)

### Ejemplo 5
st.subheader("5. Evento compuesto: accidente en viernes + alcohol + con herido")
df_evento = df[
    (df["dia_semana"] == "Friday") &
    (df["positiva_alcohol"] == "S") &
    (df["lesividad"].str.lower().str.contains("herido"))
]
p_evento = len(df_evento) / len(df)
st.write(f"Probabilidad conjunta (viernes + alcohol + herido): {p_evento:.5f}")

sim_evento = np.random.binomial(1, p_evento, size=1000)
fig5 = px.histogram(sim_evento, title="Simulación de evento compuesto (ocurre o no en 1000 intentos)")
st.plotly_chart(fig5, use_container_width=True)

st.success("Se han realizado 5 simulaciones basadas en datos reales para explorar comportamientos probabilísticos de los accidentes.")
