# -*- coding: utf-8 -*-
"""
Tarea #3. IE0405 - Modelos Probabilísticos de Señales y Sistemas.
Empezada el Miércoles 17 de Junio 17:14 2020

@author: Mauricio Céspedes Tenorio.
Carné: B71986
"""
#Librerías
import matplotlib.pyplot as plt
import pandas as pd
from numpy import linspace, sqrt, arange, sqrt, exp, pi, max
from scipy.stats import rayleigh, norm

print("Respuestas de la Tarea #2 del curso IE0405 - Modelos Probabilísticos de Señales y Sistemas.")
print("Estudiante: Mauricio Céspedes Tenorio. Carné: B71986.")
#Extracción de datos del archivo datos.cvs en un dataframe (se especifica que el encabezado es la fila cero y el índice la columna 0):
df_xy = pd.read_csv('xy.csv',header= 0, index_col=0)

#Se extrae la frecuencia relativa para X (probabilidad de X). Con el siguiente comando, para cada fila (valores de X), se suman todas las probabilidades de Y:
series_x = df_xy.sum(axis = 1)
df_x = pd.DataFrame(data={'P':series_x.values}, index=series_x.index)
#Se obtiene un array de Numpy que contenga la frecuencia relativa
array_x = series_x.values

#Se extrae la frecuencia relativa para Y (probabilidad de Y). Con el siguiente comando, para cada columna (valores de Y), se suman todas las probabilidades de X:
series_y = df_xy.sum(axis = 0)
df_y = pd.DataFrame(data={'P':series_y.values}, index=series_y.index)
print(df_y)
array_y = series_y.values
#plt.hist(array_y,25,(array_y.min(),array_y.max()),density=True)
plt.plot(range(5,26),array_y)
plt.show()
plt.plot(range(5,16),array_x)
plt.show()
