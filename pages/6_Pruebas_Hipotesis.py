# pages/6_Pruebas_Hipotesis.py

import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import plotly.express as px

st.title("Pruebas de Hipótesis - Contraste Estadístico")

@st.cache_data

def load_data():
    return pd.read_csv("data/datos_madrid.csv", encoding='latin1')

df = load_data()

# Preparación de variables comunes
df = df[df["rango_edad"] != "Desconocido"]
df["edad"] = df["rango_edad"].str.extract("(\d+)")[0].astype(float)
df["sexo"] = df["sexo"].fillna("Desconocido")
df["positiva_alcohol"] = df["positiva_alcohol"].fillna("N")
df["fecha"] = pd.to_datetime(df["fecha"], errors='coerce')
df["dia"] = df["fecha"].dt.dayofweek

### 1. T-test: Edad entre hombres y mujeres
st.subheader("1. ¿Difieren las edades medias entre hombres y mujeres?")
masc = df[df["sexo"] == "Hombre"]["edad"].dropna()
fem = df[df["sexo"] == "Mujer"]["edad"].dropna()
t_stat, p_val = stats.ttest_ind(masc, fem, equal_var=False)
st.write(f"H0: la edad media es igual | H1: son distintas")
st.write(f"T = {t_stat:.2f}, p = {p_val:.4f}")
st.success("" if p_val < 0.05 else "")

### 2. Proporciones: Alcohol fin de semana vs entre semana
st.subheader("2. ¿Hay más alcohol en fines de semana?")

df["fin_de_semana"] = df["dia"].isin([5,6])
fin = df[df["fin_de_semana"]]
lab = df[~df["fin_de_semana"]]
p1 = (fin["positiva_alcohol"] == "S").mean()
p2 = (lab["positiva_alcohol"] == "S").mean()
n1, n2 = len(fin), len(lab)

p_comb = (p1*n1 + p2*n2) / (n1+n2)
z = (p1 - p2) / np.sqrt(p_comb*(1-p_comb)*(1/n1 + 1/n2))
p_val2 = 2 * (1 - stats.norm.cdf(abs(z)))

st.write(f"H0: mismas proporciones | Z = {z:.2f}, p = {p_val2:.4f}")

### 3. Chi-cuadrado: tipo de vía vs gravedad
st.subheader("3. ¿Están asociadas tipo de vía y gravedad?")

ct = pd.crosstab(df["tipo_accidente"], df["lesividad"].fillna("Desconocido"))
chi2, p_val3, dof, expected = stats.chi2_contingency(ct)

st.write(f"H0: son independientes | Chi2 = {chi2:.1f}, p = {p_val3:.4f}")
st.dataframe(ct)

### 4. Prueba binomial: ¿es la proporción de alcohol > 5% esperada?

st.subheader("4. ¿Es significativa la proporción de alcohol?")
successes = (df["positiva_alcohol"] == "S").sum()
n_total = len(df)
expected_p = 0.05
p_val4 = stats.binom_test(successes, n_total, expected_p, alternative="greater")
st.write(f"H0: proporción = 0.05 | Observado = {successes}/{n_total}, p = {p_val4:.4f}")

### 5. ANOVA: edad media entre distritos
st.subheader("5. ¿Difiere la edad media entre distritos?")

distritos = df["distrito"].dropna().unique()
edades_por_distrito = [df[df["distrito"] == d]["edad"] for d in distritos if len(df[df["distrito"] == d]) > 30]
f_val, p_val5 = stats.f_oneway(*edades_por_distrito)

st.write(f"H0: misma media entre grupos | F = {f_val:.2f}, p = {p_val5:.4f}")

st.success("Las pruebas de hipótesis nos permiten validar patrones con rigor estadístico.")
