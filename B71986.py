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
#Extracción de datos del archivo datos.cvs en un dataframe (se especifica que no hay encabezado en el archivo):
df_xy = pd.read_csv('xy.csv',header= 0, index_col=0)
series_x = df_xy.sum(axis = 1)
df_x = pd.DataFrame(data={'P':series_x.values}, index=series_x.index)
series_y = df_xy.sum(axis = 0)
df_y = pd.DataFrame(data={'P':series_y.values}, index=series_y.index)
print(df_y)
print(df_x)
