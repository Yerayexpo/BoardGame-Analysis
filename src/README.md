# Análisis de Datos de Juegos de Mesa
Este proyecto se centra en el análisis de datos de juegos de mesa y utiliza varios modelos de aprendizaje automático para predecir el promedio de calificación de los juegos. Se emplearán modelos como LinearRegressor, KNeighbors, XGBRegressor y RandomForestRegressor para realizar estas predicciones.

## Descripción del Dataset
El conjunto de datos utilizado en este proyecto contiene la siguiente información sobre cada juego de mesa:

ID: Identificador único para cada juego de mesa en el DataFrame.
+ Name: Nombre del juego de mesa.
+ Year Published: Año en que se publicó el juego.
+ Min Players: Número mínimo de jugadores necesarios para poder jugar el juego.
+ Max Players: Número máximo de jugadores que pueden participar en el juego.
+ Play Time: Duración promedio de una partida del juego.
+ Min Age: Edad mínima recomendada para jugar el juego.
+ Users Rated: Número de usuarios que han calificado el juego en la plataforma de juegos de mesa BoardGameGeek.
+ Rating Average: Promedio de las calificaciones de los usuarios del juego en BoardGameGeek, en una escala de 1 a 10.
+ BGG Rank: Clasificación del juego según los usuarios de BoardGameGeek, basada en las calificaciones y el número de personas que han calificado el juego.
+ Complexity Average: Promedio de la complejidad del juego según los usuarios de BoardGameGeek, en una escala de 1 a 5.
+ Owned Users: Número de usuarios que poseen una copia del juego en BoardGameGeek.
+ Mechanics: Mecánicas de juego que se utilizan en el juego. Serán exploradas durante el análisis.
+ Domains: Géneros a los que pertenece el juego.
## Objetivo
El objetivo principal de este proyecto es utilizar los datos disponibles para construir modelos de regresión capaces de predecir el promedio de calificación de los juegos de mesa. Estos modelos se basarán en características como el número de jugadores, la duración promedio del juego, la edad mínima recomendada y otras variables relacionadas.

## Metodología
1. Exploración de datos: Se realizará un análisis exploratorio de los datos para comprender mejor la distribución, las relaciones y las características de los juegos de mesa en el conjunto de datos.

1. Preprocesamiento de datos: Se llevará a cabo una limpieza y transformación de los datos para prepararlos adecuadamente para el entrenamiento de los modelos de aprendizaje automático.

1. Construcción de modelos: Se implementarán varios modelos de regresión, incluyendo LinearRegressor, KNeighbors, XGBRegressor y RandomForestRegressor, utilizando las características relevantes del conjunto de datos.

1. Evaluación de modelos: Se evaluará el rendimiento de los modelos utilizando métricas adecuadas, como el error cuadrático medio (MSE) o el coeficiente de determinación (R^2), para determinar cuál de ellos proporciona las mejores predicciones.

1. Ajuste y optimización de modelos: Se realizarán ajustes y optimizaciones adicionales en los modelos seleccionados para mejorar su rendimiento, como la selección de características, la optimización de hiperparámetros o la aplicación de técnicas de validación cruzada.


1. Generación de predicciones: Una vez que los modelos estén entrenados y optimizados, se utilizarán para generar predicciones del promedio de calificación de los juegos de mesa en el conjunto de datos. Estas predicciones se compararán con los valores reales para evaluar la capacidad de los modelos para predecir de manera precisa.

1. Visualización de resultados: Se utilizarán técnicas de visualización de datos para representar gráficamente los resultados obtenidos. Esto incluirá gráficos de dispersión que comparan las predicciones con los valores reales, así como otras visualizaciones relevantes para comprender la distribución y las relaciones en los datos.

1. Conclusiones y recomendaciones: Se extraerán conclusiones basadas en los resultados obtenidos y se proporcionarán recomendaciones para futuras investigaciones o acciones relacionadas con el análisis de juegos de mesa y la predicción de calificaciones.

## Estructura del Repositorio
El repositorio de GitHub contendrá los siguientes archivos y carpetas:

+ README.md: El archivo que estás leyendo actualmente, que proporciona una descripción general del proyecto, los datos y la metodología.
+ notebooks: Esta carpeta contendrá los archivos de Jupyter Notebook utilizados para el análisis de datos, la construcción de modelos y la generación de predicciones.
+ data: Esta carpeta contendrá el archivo CSV que contiene los datos de los juegos de mesa utilizados en el proyecto.
+ results: Esta carpeta contendrá las visualizaciones generadas y los resultados de las predicciones realizadas.
+ requirements.txt: Un archivo de texto que enumera todas las dependencias del proyecto, lo cual permite a otros replicar el entorno de desarrollo.
## Requisitos
Para ejecutar el código en los cuadernos de Jupyter Notebook, se requiere tener instaladas las siguientes bibliotecas de Python:

+ NumPy
+ Pandas
+ Scikit-learn
+ XGBoost
+ Matplotlib
+ Seaborn
Puedes instalar estas bibliotecas mediante el uso de gestores de paquetes como pip. Se recomienda crear un entorno virtual de Python para evitar conflictos con las dependencias