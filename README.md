# Respuestas Tarea 3 del curso IE0405
Estudiante: Mauricio Céspedes Tenorio  

1. A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y.  
R\ Primero se leyó el archivo xy.csv con ayuda de <em>np.genfromtxt()</em>. Luego, se encuentraron las funciones de densidad marginal de X y Y al sumar todos los Y para cada valor de X y al sumar los X para cada Y respectivamente de los datos dados en el CSV. Al graficar estos valores, se observó una tendencia Gaussiana en ambas variables aleatorias, por lo que se creó una función Gaussiana que recibe como parámetros la variable aleatoria, la media (mu) y desviación estándar (sigma). Con ayuda del comando de SpiPy <em>curve_fit()</em>, se obtuvieron los parámetros <em>mu</em> y <em>sigma</em> de mejor ajuste para ambas PDF marginales. Las funciones fueron graficadas con ayuda de Matplotlib y se notó que no modelaban perfectamente los datos, pero esto es esperable al tener ruido. Las imágenes obtenidas se muestran a continuación:  
<p align="center">
  <img src="Gráficas_punto_1/curva_ajuste_X.png"/>
  <figcaption>Figura 1. Curva de mejor ajuste obtenida para la función de densidad marginal de X.</figcaption>
</p>  
<p align="center">
  <img src="Gráficas_punto_1/curva_ajuste_Y.png"/>  
  Figura 2. Curva de mejor ajuste obtenida para la función de densidad marginal de Y.
</p>  
2. Asumir independencia de X y Y, ¿cuál es entonces la función de densidad conjunta que modela los datos?  
R\ Al asumir independencia, se tiene que la función de densidad conjunta de X y Y está dada por la multiplicación de las funciones densidad marginales de X y Y. A partir de esto, se creó una función en Python que recibe como parámetros las <em>x</em> y <em>y</em> y devuelve la multiplicación de la función Gaussiana de cada una de ellas con la media y desviación estándar obtenidas en el punto 1 para cada una de las variables aleatorias. Se graficó una PDF conjunta de mejor ajuste en 3D para compararla con la discreta que se obtiene en el punto 4.  
<p align="center">
  <img src="Gráficas_punto_2/curva_ajuste_XY_a.png"/>
  <figcaption>Figura 3. Vista completa de la función de densidad conjunta modelada.</figcaption>
</p>  
<p align="center">
  <img src="Gráficas_punto_2/curva_ajuste_XY_b.png"/>
  <figcaption>Figura 4. Vista lateral 1 de la función de densidad conjunta modelada.</figcaption>
</p>  
<p align="center">
  <img src="Gráficas_punto_2/curva_ajuste_XY_c.png"/>
  <figcaption>Figura 5. Vista lateral 2 de la función de densidad conjunta modelada.</figcaption>
</p>  
