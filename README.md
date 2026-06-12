# Análisis Histórico de Bitcoin 📊

## Descripción
Proyecto de análisis de datos aplicado al mercado financiero, utilizando 
datos históricos de Bitcoin obtenidos de Yahoo Finance. El objetivo es 
analizar el comportamiento histórico de Bitcoin para comprender sus 
tendencias, volatilidad y características del mercado.

Este proyecto fue desarrollado como parte de mi portfolio para la 
Tecnicatura en Ciencia de Datos.

## Dashboard interactivo 🚀

Podés ver el dashboard en vivo sin instalar nada:

👉 [Ver dashboard](https://bitcoin-analysis-santiago.streamlit.app)

## Preguntas que responde el análisis
- ¿Cómo evolucionó el precio de Bitcoin a lo largo de los años?
- ¿Cuáles fueron los períodos de mayor volatilidad?
- ¿Cuál fue el rendimiento anual de Bitcoin?
- ¿Qué relación existe entre volumen de operaciones y movimiento del precio?
- ¿En qué meses o años el mercado fue más estable o más volátil?

## Tecnologías utilizadas
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebooks

## Estructura del proyecto
```
BITCOIN-ANALYSIS/
├── data/
│   ├── bitcoin_2025-06-08.csv       # Datos crudos descargados de Yahoo Finance
│   └── bitcoin_limpio.csv           # Datos limpios listos para análisis
├── notebooks/
│   ├── 01_obtencion_datos.ipynb     # Descarga de datos con yfinance
│   ├── 02_limpieza.ipynb            # Limpieza y preparación del dataset
│   ├── 03_eda.ipynb                 # Análisis exploratorio de datos
│   ├── 04_visualizaciones.ipynb     # Visualizaciones
│   └── 05_conclusiones.ipynb        # Conclusiones y glosario
├── README.md
└── requirements.txt
```

## Cómo ejecutar el proyecto
1. Clonar el repositorio
2. Instalar las dependencias con `pip install -r requirements.txt`
3. Ejecutar los notebooks en orden desde el 01 al 05

## Principales conclusiones
- Bitcoin pasó de un precio promedio de $272 USD en 2015 a $101.641 USD en 2025
- Los años más volátiles fueron 2017, 2018 y 2021 con más del 4% de volatilidad diaria
- El mejor año en rendimiento fue 2017 con un 1318%, seguido de fuertes caídas en 2018
- El volumen operado no es un predictor del movimiento del precio (correlación de -0.02)
- Los meses más volátiles son enero, febrero y marzo, mientras que los más estables son agosto, septiembre y octubre

## Fuente de datos
Datos históricos de Bitcoin obtenidos de Yahoo Finance a través de la 
librería yfinance. Los datos cubren el período desde 2015 hasta la actualidad 
y se actualizan diariamente.

## Autor
Santiago Scozziero
Estudiante de la Tecnicatura en Ciencia de Datos