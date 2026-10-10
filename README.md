# 🚦 Dashboard de Analítica y Predicción de Tráfico Vehicular

> **Evaluación de Seguimiento — Ingeniería de Software**  
> **Corporación Universitaria Lasallista (Unilasallista)**  
> **Año:** 2026

---

## 📋 Descripción del Proyecto
Este proyecto implementa una solución integral de analítica y predicción de flujo vehicular basada en ciencia de datos y Machine Learning. Utilizando un dataset histórico de tráfico (proveniente de Kaggle), el sistema procesa variables temporales y meteorológicas para estimar la congestión vial, apoyando la toma de decisiones en la ingeniería de movilidad urbana. Además, incorpora una **Skill personalizada de Google Gemini** para actuar como un agente consultor inteligente.

---

## 🛠️ Entregables del Proyecto (100% Completados)

Los 6 componentes desarrollados para cumplir con la rúbrica de evaluación son:

1. **Infografía Conceptual:**  
   Diseño académico estructurado en pilares técnicos, disponible en el archivo [`INFOGRAFIA.md`](./INFOGRAFIA.md).

2. **Video Explicativo:**  
   Resumen ejecutivo y síntesis técnica generada con **NotebookLM**.  
   👉 [Ver Video Explicativo en Google Drive](https://drive.google.com/file/d/1cBl6Fj1JRUACxWD8KfC4MtSJinLEaY28/view?usp=sharing)

3. **Landing Page Interactiva:**  
   Desplegada y alojada en producción mediante Netlify:  
   👉 [https://traffic-analytics-dashboard.netlify.app](https://traffic-analytics-dashboard.netlify.app)

4. **Repositorio y Código Fuente:**  
   Proyecto publicado oficialmente en GitHub con todo el código, assets y documentación:  
   👉 [https://github.com/d9566585-cloud/traffic-analytics-dashboard](https://github.com/d9566585-cloud/traffic-analytics-dashboard)  
   👉 [Ver Cuaderno de Entrenamiento en Google Colab](https://colab.research.google.com/drive/1YgRNCG17hA6JIhaFNJ1F7y2TAnTYe1KC?usp=sharing)

5. **Gemini Skill:**  
   Implementación de agente consultor orientado a IA conversacional para interpretación de métricas del dataset de Kaggle:  
   👉 [`skills/traffic_analyst_skill.md`](./skills/traffic_analyst_skill.md)

6. **Documentación del Desarrollo:**  
   Metodología, pipeline de datos, arquitectura y resultados detallados en las secciones siguientes de este documento.

---

## 📖 Documentación del Desarrollo (Punto 6)

### 1. Pipeline de Datos y Procesamiento
* **Fuente:** Dataset de Kaggle (`DataBase-trafic analitic.csv`).
* **Variables de Entrada (Features):** Hora del día, día de la semana, temperatura (°C), precipitación/lluvia y nubosidad.
* **Variable Objetivo (Target):** Volumen/Flujo vehicular estimado.
* **Preprocesamiento:** Limpieza de valores nulos, codificación de variables categóricas temporales y normalización mediante Scikit-learn en Google Colab.

### 2. Modelo de Machine Learning (`RandomForestRegressor`)
Se eligió el algoritmo de ensamble **Random Forest Regressor** debido a su capacidad para modelar relaciones no lineales complejas entre el clima y el tráfico vehicular sin sufrir sobreajuste.

#### 📊 Métricas Oficiales de Desempeño:
* **Coeficiente de Determinación ($R^2$):** `0.9524` *(El modelo explica el 95.24% de la variabilidad del tráfico)*.
* **Error Absoluto Medio (MAE):** `228.66`
* **Raíz del Error Cuadrático Medio (RMSE):** `426.29`

### 3. Arquitectura del Sistema y Despliegue
* **Frontend / UI:** Landing page responsiva (`index.html`) diseñada con componentes de interfaz modernos.
* **CI/CD & Hosting:** Despliegue automatizado continuo mediante integración GitHub ↔ Netlify.
* **Entorno de Experimentación:** Google Colab para entrenamiento y validación de modelos.
* **Agente IA:** Definición de System Prompt y contexto delimitado para integración con Google Gemini.

---

## 🤖 Integración de la Skill de Gemini

La Skill personalizada (`traffic-analytics-coach`) transforma a Gemini en un consultor técnico capaz de:
1. Traducir el significado de métricas complejas ($R^2 = 0.9524$, MAE = 228.66) a lenguaje natural para ingenieros de tránsito.
2. Identificar franjas horarias críticas con mayor probabilidad de congestión.
3. Sugerir pautas preventivas de gestión vial sujetas a validación operativa.
