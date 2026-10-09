import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Traffic Analytics - Dashboard",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Traffic Analytics - Toma de Decisiones")
st.markdown("Herramienta interactiva para predecir el volumen de tráfico vehicular y analizar patrones temporales y meteorológicos.")

# ---------------------------------------------------------
# CARGA DEL MODELO
# ---------------------------------------------------------
@st.cache_resource
def cargar_modelo():
    return joblib.load("modelo_traffic_analytics.joblib")

try:
    modelo = cargar_modelo()
except Exception as e:
    st.error("Error al cargar el archivo del modelo (.joblib).")
    st.stop()

# ---------------------------------------------------------
# BARRA LATERAL: ENTRADA DE PARÁMETROS
# ---------------------------------------------------------
st.sidebar.header("⚙️ Parámetros de Entrada")

hora = st.sidebar.slider("Hora del día", 0, 23, 16)
dia_semana = st.sidebar.selectbox(
    "Día de la semana",
    options=[0, 1, 2, 3, 4, 5, 6],
    format_func=lambda x: ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"][x]
)
temperatura = st.sidebar.number_input("Temperatura (K)", value=288.15, step=0.5)
mes = st.sidebar.slider("Mes del año", 1, 12, 10)
nubes = st.sidebar.slider("Cobertura de nubes (%)", 0, 100, 40)
nieve = st.sidebar.number_input("Nieve en 1h (mm)", value=0.0, step=0.1)
lluvia = st.sidebar.number_input("Lluvia en 1h (mm)", value=0.0, step=0.1)

# Crear DataFrame con las columnas ingresadas
datos_dict = {
    "hour": hora,
    "day_of_week": dia_semana,
    "temp": temperatura,
    "month": mes,
    "clouds_all": nubes,
    "snow_1h": nieve,
    "rain_1h": lluvia
}

# Reordenar las columnas según el orden exacto del entrenamiento del modelo
if hasattr(modelo, "feature_names_in_"):
    columnas_ordenadas = list(modelo.feature_names_in_)
    datos_entrada = pd.DataFrame([datos_dict])[columnas_ordenadas]
else:
    datos_entrada = pd.DataFrame([datos_dict])

# ---------------------------------------------------------
# SECCIÓN 1: PREDICCIÓN EN TIEMPO REAL
# ---------------------------------------------------------
st.subheader("🔮 Predicción en Tiempo Real")

col1, col2 = st.columns([1, 2])

with col1:
    if st.button("Calcular Predicción", type="primary"):
        prediccion = modelo.predict(datos_entrada)[0]
        st.metric(
            label="Volumen de Tráfico Estimado",
            value=f"{int(prediccion):,} vehículos/hora"
        )
        
        if prediccion > 4500:
            st.warning("⚠️ **Tráfico Alto:** Se recomiendan medidas de gestión vial.")
        elif prediccion > 2000:
            st.info("ℹ️ **Tráfico Moderado:** Flujo vehicular constante.")
        else:
            st.success("✅ **Tráfico Bajo:** Flujo libre.")

with col2:
    st.write("**Datos ingresados:**")
    st.dataframe(datos_entrada, use_container_width=True)

st.divider()

# ---------------------------------------------------------
# SECCIÓN 2: TOMA DE DECISIONES Y MÉTRICAS (T.D.)
# ---------------------------------------------------------
st.subheader("📊 Apoyo a la Toma de Decisiones (T.D.)")

tab1, tab2 = st.tabs(["Importancia de Variables", "Rendimiento del Modelo"])

with tab1:
    st.markdown("#### Importancia de Características según Random Forest")
    
    # Obtener nombres e importancias
    nombres_features = getattr(modelo, "feature_names_in_", datos_entrada.columns)
    importancias = pd.Series(
        modelo.feature_importances_,
        index=nombres_features
    ).sort_values(ascending=True)

    fig, ax = plt.subplots(figsize=(8, 4))
    importancias.plot(kind="barh", ax=ax, color="#1f77b4")
    ax.set_title("Importancia Predictiva por Variable")
    ax.set_xlabel("Importancia Estimada")
    st.pyplot(fig)

with tab2:
    st.markdown("#### Métricas de Evaluación de la Versión Actual")
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Coeficiente $R^2$", "0.9524")
    col_m2.metric("MAE (Error Absoluto Medio)", "228.66")
    col_m3.metric("RMSE (Error Cuadrático Medio)", "426.29")
