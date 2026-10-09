# 🚗 Traffic Analytics - Dashboard & Toma de Decisiones

Herramienta interactiva desarrollada en Python y Streamlit para la predicción en tiempo real del volumen de tráfico vehicular, integrada con un modelo de Machine Learning (Random Forest) enfocado en el apoyo a la toma de decisiones en gestión vial.

---

## 📌 Descripción del Proyecto

El sistema analiza variables temporales (hora del día, día de la semana, mes) y meteorológicas (temperatura, lluvia, nieve, cobertura de nubes) para estimar el flujo de vehículos e identificar patrones de congestión.

### 🎯 Funcionalidades Principales
- **Predicción en Tiempo Real:** Cálculo instantáneo del volumen de tráfico con alertas dinámicas.
- **Soporte a la Toma de Decisiones (T.D.):**
  - Visualización del nivel de importancia de cada variable según el modelo Random Forest.
  - Evaluación continua del rendimiento del modelo con métricas estándar.

---

## 📊 Métricas del Modelo de Machine Learning

El modelo evaluado (Random Forest Regressor) obtuvo los siguientes resultados en las pruebas de validación:

| Métrica | Valor | Descripción |
| :--- | :---: | :--- |
| **Coeficiente de Determinación ($R^2$)** | **0.9524** | Explica el **95.24%** de la variabilidad del tráfico. |
| **Error Absoluto Medio (MAE)** | **228.66** | Desviación promedio reducida respecto a los valores reales. |
| **Error Cuadrático Medio (RMSE)** | **426.29** | Sensibilidad ante desviaciones atípicas. |

---

## 📁 Estructura del Repositorio

- `app.py`: Código principal de la aplicación web en Streamlit.
- `modelo_traffic_analytics.joblib`: Modelo Random Forest entrenado y serializado.
- `DataBase-trafic analitic.csv`: Dataset procesado de volumen de tráfico y clima.
- `metricas_modelo.csv`: Reporte detallado de métricas de desempeño.
- `resultados_prediccion.csv`: Predicciones generadas en fase de prueba.
- `grafica_trafico_por_hora.png`: Gráfica descriptiva del comportamiento temporal del tráfico.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Librerías principales:** Streamlit, Pandas, NumPy, Scikit-learn, Joblib, Matplotlib / Seaborn
- **Despliegue/Túnel:** Cloudflare Tunnel (`cloudflared`) / Google Colab
