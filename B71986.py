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
import numpy as np
from scipy.optimize import curve_fit

print("Respuestas de la Tarea #2 del curso IE0405 - Modelos Probabilísticos de Señales y Sistemas.")
print("Estudiante: Mauricio Céspedes Tenorio. Carné: B71986.")
#Extracción de datos del archivo datos.cvs en un dataframe (se especifica que el encabezado es la fila cero y el índice la columna 0):
array_csv = np.genfromtxt('xy.csv', delimiter=',')
#Se eliminan la fila 0 y columna 0, ya que contienen el header e index de los datos dados:
array_xy = np.delete(np.delete(array_csv, 0, 0), 0, 1)
#Se encuentra a PMF de X al sumar todos los Y para cada valor de X (se suman todos los valores para cada fila):
fX= np.sum(array_xy, axis=1)
#Se encuentra a PMF de Y al sumar todos los X para cada valor de Y (se suman todos los valores para cada columna):
fY= np.sum(array_xy, axis=0)

#Se observó al plotear fX y fY, que ambas se comportaban como una función Gaussiana, por lo que se definió la función:
def Gaussiana(x, mu, sigma):#Donde mu es la media y sigma la desviación estándar
    return (1/np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))
#Se encuentra la curva de mejor ajuste Gaussiana para X:
xs = np.linspace(5,15, num=11) #Se limitan las muestras de X a valores discretos entre 5 y 15, como se dio en el CSV
param_x, _ = curve_fit(Gaussiana, xs, fX)
#Se crea espacio lineal entre 5 y 15 con 30 puntos para graficar la curva de mejor ajuste obtenida:
x_fit = np.linspace(5,15,30)
plt.plot(x_fit, Gaussiana(x_fit, param_x[0], param_x[1]), 'r-', label="Modelo encontrado con ayuda de Scipy")
plt.plot(range(5,16),fX, 'b--', label='Función encontrada "a mano"')
plt.show()

#Se encuentra la curva de mejor ajuste Gaussiana para Y:
ys = np.linspace(5,25, num=21) #Se limitan las muestras de Y a valores discretos entre 5 y 25, como se dio en el CSV
param_y, _ = curve_fit(Gaussiana, ys, fY)
#Se crea espacio lineal entre 5 y 25 con 40 puntos para graficar la curva de mejor ajuste obtenida:
y_fit = np.linspace(5,25,40)
plt.plot(y_fit, Gaussiana(y_fit, param_y[0], param_y[1]), 'r-', label="Modelo encontrado con ayuda de Scipy")
plt.plot(range(5,26),fY, 'b--', label='Función encontrada "a mano"')
plt.show()

"""2. Asumir independencia de X y Y, ¿cuál es entonces la función de densidad conjunta que modela los datos? """
#Asumiendo independencia de X y Y, la función de densidad conjunta estaría dada por:
def fxy(x,y):
    return Gaussiana(x, param_x[0],param_x[1])*Gaussiana(y, param_y[0],param_y[1])

"""3.Hallar los valores de correlación, covarianza y coeficiente de correlación (Pearson) para los datos y explicar su significado."""
#Lectura del archivo xyp.csv:
array_xyp = np.genfromtxt('xyp.csv', delimiter=',', skip_header=1)
#Cálculo de correlación:
correlacion = 0
for fila in array_xyp:
    correlacion += fila[0]*fila[1]*fila[2]
#Se evalúa si la correlación es igual a E[X]*E[Y]. Si es cierto, se dice que X y Y no están correlacionadas.
if 0.95<=correlacion/(param_x[0]*param_y[0])<=1.05:
    print("La correlación obtenida tiene un valor de: "+"{:.3f}".format(correlacion)+" y E[X]*E[Y] es igual a: " +"{:.3f}".format(param_x[0]*param_y[0])+".\nComo son muy similares, se concluye que X y Y no están correlacionadas.")
else:
    print("El valor de la correlación no es cercano a la multiplicación E[X]*E[Y], por lo que no se puede afirmar que las variables X y Y no están correlacionadas.")

#Cálculo de covarianza:
covarianza = 0
#Se calcula recorriendo el array dado en xyp.csv, considerando que se calcula como la sumatoria de todos los x y y en la fórmula: (x-E[X])(x-E[Y])*fxy(x,y)
for fila in array_xyp:
    covarianza += (fila[0]-param_x[0])*(fila[1]-param_y[0])*fila[2]
#Se evalúa si la correlación es igual a E[X]*E[Y]. Si es cierto, se dice que X y Y no están correlacionadas.
if covarianza<=0.3:
    print("La covarianza obtenida tiene un valor de: "+"{:.3f}".format(covarianza)+", que es muy cercano a cero, por lo que se puede concluir que X y Y son independientes y no están correlacionadas.\nEsto corrobora la suposición inicial de independencia y lo encontrado en el punto anterior (la no correlación).")
else:
    print("El valor de la correlación no es cercano a cero, por lo que no se puede afirmar que las variables X y Y no están correlacionadas o sean independientes.")

#Cálculo del coeficiente de correlación de X y Y:
#Este coeficiente está definido por: ρ= C_{XY}/(sigma_X * sigma_Y), donde C_{XY} es la covarianza ya encontrada y ambos sigmas son las desviaciones estándar ya encontradas con la función Gaussiana.
#Como la covarianza es aproximadamente cero, este coeficiente también debe serlo.
coeficiente = covarianza/(param_x[1]*param_y[1])
print("El coeficiente de correlación tiene un valor de: "+"{:.3f}".format(coeficiente)+", que es aproximadamente cero, ya que la covarianza es muy cercana a cero.\nEste resultado arroja las mismas conclusiones que los de la covarianza: X y Y son independientes y no correlacionadas.")

"""4. Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D)."""
