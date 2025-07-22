# 📊 Análisis Estadístico de Accidentes de Tráfico en Madrid

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.42-orange?logo=streamlit)
![Estado](https://img.shields.io/badge/Proyecto-Terminado-success?style=flat-square)

Este proyecto fue desarrollado por **Valentina Bailon Cano** como parte del **Máster en Data Science & Inteligencia Artificial** en **Evolve**.

---

## 📌 Tabla de Contenidos

- 🎯 Objetivo Académico
- 🧭 Contenido de la Aplicación
- 📐 Rigor Académico
- 🛠️ Tecnologías utilizadas
- 📂 Estructura del Proyecto
- ▶️ Cómo ejecutar localmente
- 💻 Guía rápida: Git Bash vs Visual Studio Code
- 👩‍💻 Autora
- 🧠 Conclusión

---

## 🎯 Objetivo Académico

Aplicar de forma práctica los fundamentos de estadística y probabilidad sobre un conjunto de datos reales de accidentes de tráfico ocurridos en la ciudad de Madrid.  
Se combinan técnicas manuales, simulaciones, pruebas estadísticas y visualizaciones interactivas mediante Streamlit, con enfoque académico riguroso y presentación profesional.

---

## 🧭 Contenido de la Aplicación

La app está dividida en secciones accesibles desde el menú lateral:

1. **Medidas descriptivas** (manuales vs pandas)  
2. **Detección de outliers** (IQR y Z-score)  
3. **Simulaciones** de probabilidad realista (alcohol, edad, gravedad…)  
4. **Distribuciones teóricas** comparadas con datos reales (Normal, Poisson, Binomial)  
5. **Intervalos de confianza** para medias y proporciones  
6. **Pruebas de hipótesis** (T-test, proporciones, Chi², ANOVA)  
7. **Correlaciones** (Pearson, Spearman, Kendall)  
8. **Análisis exploratorio final** con mapa interactivo, filtros y KPIs

---

## 📐 Rigor Académico

Cada sección fue construida con el objetivo de demostrar dominio metodológico y comprensión estadística aplicada.  
Incluye:

- Códigos comentados y validados  
- Simulaciones realistas (distribuciones truncadas, valores extremos)  
- Justificación teórica de cada técnica aplicada  
- Visualizaciones claras y adaptadas a un entorno de enseñanza profesional

---

## 🛠️ Tecnologías utilizadas

- Python 3.12  
- Streamlit 1.42  
- Plotly  
- pandas · numpy · scipy  
- pydeck (mapas 3D) · pyproj (coordenadas UTM)  
- Visual Studio Code · GitHub

📄 Dependencias completas en `requirements.txt`

---

## 📂 Estructura del Proyecto

```
├── images/              # Logos y capturas
├── data/                # Datos originales (accidentes Madrid)
├── main.py              # Script principal de Streamlit
├── pages/               # Subpáginas estadísticas
├── utils/               # Funciones auxiliares (si aplica)
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación del proyecto
```

---

## ▶️ Cómo ejecutar localmente

### 1. Clona el repositorio

```bash
git clone https://github.com/valentinabailoncano-code/Accidentes_madrid.git
cd Accidentes_madrid
```

### 2. Crea un entorno virtual (opcional pero recomendable)

#### En **Visual Studio Code** o CMD de Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### En **macOS/Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta la app de Streamlit

```bash
streamlit run main.py
```

---

## 💻 Guía rápida: Git Bash vs Visual Studio Code

### ✅ Desde **Git Bash**

```bash
git clone https://github.com/valentinabailoncano-code/Accidentes_madrid.git
cd Accidentes_madrid
pip install -r requirements.txt

# ⚠️ Git Bash no reconoce bien 'streamlit'
# Abre CMD o Visual Studio Code para este último paso:
streamlit run main.py
```

### ✅ Desde **Visual Studio Code**

```bash
python -m venv venv
venv\Scripts\activate       # En Windows
# o
source venv/bin/activate    # En macOS/Linux

pip install -r requirements.txt
streamlit run main.py
```

## 👩‍💻 Autora

**Valentina Bailon Cano**  
Máster en Data Science & Inteligencia Artificial – EVOLVE  
🔗 [LinkedIn](https://www.linkedin.com/in/valentina-bailon-2653b22b7)  
📍 Madrid, España

---

## 🧠 Conclusión

Este proyecto busca ser una herramienta académica útil tanto para estudiantes como docentes de estadística aplicada, mostrando cómo los conceptos teóricos pueden implementarse con precisión sobre datos del mundo real.