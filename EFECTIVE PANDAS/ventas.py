"""
Para hacer la previsión de ventas para los próximos 4 trimestres, podemos utilizar el método de suavizado exponencial simple, que es una técnica de análisis de series temporales que utiliza un promedio ponderado de los últimos datos observados para predecir el valor futuro de la serie.

Para implementar este método en Python, podemos utilizar la librería de ciencia de datos Pandas para leer los datos y calcular el promedio ponderado, y luego utilizar el módulo de pronósticos de la librería statsmodels para realizar la previsión.

A continuación se muestra un ejemplo de código en Python que puede utilizarse para hacer la previsión de ventas para los próximos 4 trimestres:
"""

# Importar librerias necesarias
import pandas as pd
import statsmodels.api as sm

# Leer datos
datos = pd.read_csv("datos_ventas.csv")

# Calcular promedio ponderado
datos['promedio_ponderado'] = datos['TOTAL'].ewm(alpha=0.3).mean()

# Hacer previsión de ventas para los próximos 4 trimestres
modelo = sm.tsa.ExponentialSmoothing(datos['TOTAL'])
prevision = modelo.fit().forecast(4)

# Mostrar resultados
print("Previsión de ventas para los próximos 4 trimestres:")
print(prevision)
