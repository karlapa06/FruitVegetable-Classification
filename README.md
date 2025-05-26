# FruitVegetable-Classification

## Abstract 
La correcta identificación de frutas y verduras en buen estado frente a aquellas en estado de descomposición es crucial para reducir el desperdicio de alimentos, asegurar la inocuidad y mantener estándares de calidad en la agricultura y en toda la cadena de suministro. Este estudio se enfocó en el desarrollo de un modelo de clasificación de imágenes mediante redes neuronales convolucionales, utilizando un conjunto de datos obtenido de Kaggle que contiene imágenes de 14 tipos de frutas y verduras, tanto sanas como podridas. Se evaluó el desempeño de diferentes arquitecturas de redes neuronales profundas, incluyendo EfficientNetV2B0, con el objetivo de optimizar la precisión en la clasificación. Los resultados obtenidos muestran que el modelo propuesto puede ser una herramienta eficaz para aplicaciones automatizadas en sistemas de selección y control de calidad de productos agrícolas.

## Introducción 
Es de vital importancia mantener una buena salud, de la misma manera es necesario asegurar que los alimentos tengan la adecuada nutrición. Con este estudio se demuestra como detectar frutas y verduras sanas vs podridas. Dentro del estudio se evalua un modelo de CNN como EfficientNetV2B0. Cada Set de Datos contiene dos tipos de datos: sanas y podridas que se clasifican por frutas y verdudas, el set de datos tiene un total de 32,023 imagénes. En el siguiente paper se demuestra la metodología que se ha utilizado, como los algoritmos, el dataset, parametros y finalmente la parte de resultados como de conclusiones. 

## Metodologias 
### Pre-Procesamiento de datos  
* Redimensionamiento: Todas las imágenes fueron redimensionadas a 224x224 píxeles para asegurar una entrada uniforme al modelo EfficientNetV2B0.
* Conversión de color: Se garantizó que todas las imágenes estuvieran en el formato RGB, convirtiendo aquellas que no lo estuvieran, para cumplir con el requerimiento del modelo base, ya que algunas de las imágenes tenía transperencias lo que provocaba que al momento de tener nuestro modelo.fit podía generar desbalances. 
* División de datos: El conjunto de datos fue dividido en tres subconjuntos: 70% para entrenamiento, 10% para validación y 20% para prueba. Esta división se realizó de forma aleatoria y equilibrada entre las clases (frutas/verduras sanas y podridas), ya que el set de Datos solo proporcionaba las imágenes, y se ha escogido el Principio de Parto donde el 80% se utiliza para entrenamiento y 20% para pruebas, sin embargo dentro del 80% de entrenamiento he dejado un 10% para poder validar antes de testear. 
* Escalamiento: Se normalizaron los valores de píxeles a un rango de [0,1], utilizando rescale=1.255 dentro de ImageDataGenerator, gracias a esto se mejora la eficiencia del entrenamiento. 

### Generación de Datos 
Se utilizó ImageDataGenerator de TensorFlow para aplicar técnicas de aumento de datos como rotación, desplazamientos horizontales y verticales, y volteo horizontal. Esto ayudó a mejorar la generalización del modelo evitando sobreajuste, las transformaciones aplicadas incluyen: 
* Rotation_range de 20 grados, para permitir que se apliquen rotaciones aleatorias de hasta 20 grados durante el entrenamiento se ha utilizado estos datos por la investigación que se ha realizado a través de papers pero sin alterar la identidad visual de las imágenes. 
* Width y height shifth range de hasta un 20%, para simular posiciones ligeramente distintas de los objetos dentro del marco.
* Horizontal_flip verdaderon para que el modelo no se sesga hacia una orientación específica y puede aprender patrones más generales.
Para el caso de train, val y test generator se fija un target_size de 224x224, un batch size de 32 y como class_mode='categorical', en la mayoría de los papers que se han tomado como referencia se toma una entrada para redimensionar las imágenes garantizando que se tenga una entrada uniforme al modelo, para el batch size una mayor eficiencia y finalmente se ha escogido un modo de clasificación multiclase.

### Arquitectura del modelo 
Dentro del modelo se utilizó la arquitectura EfficientNetV2B0, una red neuronal convolucional profunda de última generación desarrollada por Google. Esta arquitectura fue diseñada para ser eficiente tanto en precisión como en velocidad de entrenamiento, lo que la hace ideal para tareas de clasificación de imágenes con grandes cantidades de datos, como es el caso de frutas y verduras sanas vs podridas, que ha sido utilizada en distintos casos de investigación para este caso en particular. EfficientNetV2B0 es la versión más pequeña y rápida de la familia EfficientNetV2. Está optimizada para entrenarse más rápido que sus versiones anteriores y logra una alta precisión utilizando menos parámetros y recursos computacionales. A mayor descripción: 
* include_top=False: Elimina las capas de clasificación originales del modelo (usadas en ImageNet), ya que se desea entrenar para nuevas clases.
* input_shape=(224, 224, 3): Define la forma esperada de las imágenes de entrada (224x224 píxeles, 3 canales RGB).
* pooling='avg': Aplica un Global Average Pooling automáticamente al final del modelo base, que reduce cada mapa de características a un solo valor (resumen de cada filtro).
* include_preprocessing=True: Incluye la normalización de entrada que EfficientNetV2B0 requiere, como parte del grafo del modelo.
* categorical_crossentropy: Se usa para problemas de clasificación multiclase.
* AdamW(1e-4): Se usa una tasa de aprendizaje de 1e-4.
* Accuracy: para monitorear la precisión durante entrenamiento y validación.
Dichas especificaciones del modelo se han investigado y tomado de las investigaciones y soluciones que se han desarrollado en otros Papers. 


### Evaluación del modelo
Para la evaluación del modelo se tomaran cuenta los valores de Accuracy, precision y recall tres criterios utilizados para evaluar un modelo de clasificación. Asimismo la Matriz de Confusión han sido utilizados para evaluar el modelo. 
* Accuracy: 83.80%
* Precision: 82.98%
* Recall: 79.95%
* F1 Score: 79.89%

Matriz de Confusión 
<img width="586" alt="Captura de pantalla 2025-05-25 a la(s) 11 40 13 p m" src="https://github.com/user-attachments/assets/601585a8-56ee-4326-8cae-22e854374306" />

En la evaluación del modelo se puede observar que 
## Conclusiones 

## Referencias 
S. Aksoy, P. Demircioglu y I. Bogrekci, "Evaluating pretrained CNNs for distinguishing fresh vs rotten fruits and vegetables," Journal of Applied Horticulture, vol. 26, no. 3, pp. 361–366, 2024. [En línea]. Disponible: https://doi.org/10.37855/jah.2024.v26i03.69
M. S. Miah, T. Tasnuva, M. Islam, et al., "An Advanced Method of Identification Fresh and Rotten Fruits using Different Convolutional Neural Networks," 2021 International Conference on Computer Communications and Networks Technology (ICCCNT), July 2021, doi: 10.1109/ICCCNT51525.2021.9580117. Link: https://www.researchgate.net/publication/355895633_An_Advanced_Method_of_Identification_Fresh_and_Rotten_Fruits_using_Different_Convolutional_Neural_Networks 
