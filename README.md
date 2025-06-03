# FruitVegetable-Classification

## Abstract 
La correcta identificación de frutas y verduras en buen estado frente a aquellas en estado de descomposición es crucial para reducir el desperdicio de alimentos, asegurar la inocuidad y mantener estándares de calidad en la agricultura y en toda la cadena de suministro. Este estudio se enfocó en el desarrollo de un modelo de clasificación de imágenes mediante redes neuronales convolucionales, utilizando un conjunto de datos obtenido de Kaggle que contiene imágenes de 14 tipos de frutas y verduras, tanto sanas como podridas. Se evaluó el desempeño de diferentes arquitecturas de redes neuronales profundas, incluyendo VGG16, con el objetivo de optimizar la precisión en la clasificación. Los resultados obtenidos muestran que el modelo propuesto puede ser una herramienta eficaz para aplicaciones automatizadas en sistemas de selección y control de calidad de productos agrícolas.

## Introducción 
Es de vital importancia mantener una buena salud, de la misma manera es necesario asegurar que los alimentos tengan la adecuada nutrición. Con este estudio se demuestra cómo detectar frutas y verduras sanas vs podridas. Dentro del estudio se evalúa un modelo de CNN llamado VGG16. Cada Set de Datos contiene dos tipos de datos: sanas y podridas que se clasifican por frutas y verduras, el set de datos tiene un total de 32,023 imágenes. De acuerdo con FAO, en el año 2021 se propone concienciar sobre los beneficios nutricionales y para la salud de las frutas y verduras y su contribución a una dieta y un estilo de vida equilibrados y saludables. Donde también se espera llamar la atención sobre la necesidad de reducir las pérdidas y desperdicios en el sector de las frutas y verduras (ONU, 2020) y, al mismo tiempo, mejorar los resultados medioambientales.  

Es por ello que es necesario adoptar medidas a nivel nacional para aumentar la producción y el consumo de frutas y verduras, al hacerlas más asequibles para los consumidores, generando beneficios económicos, sociales y ambientales al disminuir la pérdida de las mismas. La tecnología e innovación son necesarias en todas las etapas de la cadena de suministro, desde la producción hasta el consumo, para mejorar tanto la calidad como la producción. 

Este estudio propone el desarrollo de un modelo de clasificación de imágenes basado en redes neuronales convolucionales, utilizando Transfer Learning. Se describe la metodología empleada, los algoritmos utilizados, las características del conjunto de datos y, finalmente, los resultados obtenidos y sus respectivas conclusiones.


## Metodologías 
### Pre-Procesamiento de datos  
* Redimensionamiento: Todas las imágenes fueron redimensionadas a 224x224 píxeles para asegurar una entrada uniforme al modelo.
* Conversión de color: Se garantizó que todas las imágenes estuvieran en el formato RGB, convirtiendo aquellas que no lo estuvieran, para cumplir con el requerimiento del modelo base, ya que algunas de las imágenes tenían transperencias lo que provocaba que al momento de tener nuestro modelo.fit podía generar desbalances. 
* División de datos: El conjunto de datos fue dividido en tres subconjuntos: 70% para entrenamiento, 10% para validación y 20% para prueba. Esta división se realizó de forma aleatoria y equilibrada entre las clases (frutas/verduras sanas y podridas), ya que el set de Datos sólo proporcionaba las imágenes, y se ha escogido el Principio de Parto donde el 80% se utiliza para entrenamiento y 20% para pruebas, sin embargo dentro del 80% de entrenamiento he dejado un 10% para poder validar antes de testear. 

### Generación de Datos 
Se utilizó ImageDataGenerator de TensorFlow para aplicar técnicas de aumento de datos como rotación, desplazamientos horizontales y verticales, y volteo horizontal. Esto ayudó a mejorar la generalización del modelo evitando sobreajuste, las transformaciones aplicadas incluyen: 
* Escalamiento: Se normalizaron los valores de píxeles a un rango de [0,1], utilizando rescale=1./255 dentro de ImageDataGenerator, gracias a esto se mejora la eficiencia del entrenamiento. 
* Rotation_range de 20 grados, para permitir que se apliquen rotaciones aleatorias de hasta 20 grados durante el entrenamiento se ha utilizado estos datos por la investigación que se ha realizado a través de papers pero sin alterar la identidad visual de las imágenes. 
* Width y height shift range de hasta un 20%, para simular posiciones ligeramente distintas de los objetos dentro del marco.
* Horizontal_flip verdadero para que el modelo no se sesga hacia una orientación específica y pueda aprender patrones más generales.
Para el caso de train, val y test generator se fija un target_size de 224x224, un batch size de 32 y cómo class_mode='categorical', en la mayoría de los papers que se han tomado como referencia se toma una entrada para redimensionar las imágenes garantizando que se tenga una entrada uniforme al modelo, para el batch size una mayor eficiencia y finalmente se ha escogido un modo de clasificación multiclase.

### Arquitectura del modelo 
Es posible usar un CNN que ya ha sido entrenado dentro de un dataset extenso y re-entrenar el modelo con un muestra mucho más pequeña a este proceso se le conoce como Transfer Learning. En Transfer Learning, el modelo pre-entrenado es utilizado, ya que es capaz de reconocer características de una imagen, por otra parte el output del nuevo modelo debe de ser adaptado para la nueva clasificación. Dentro del modelo se utilizó la arquitectura VGG16, arquitectura que fue creada por ImageNet.com, escogí esta arquitectura porque puede resolver problemas con una alta complejidad dentro de clasificación de imágenes ya que se está trabajando con imágenes de formato RGB, es una arquitectura apropiada para la investigación. La arquitectura de este modelo consiste en:
* include_top=False: Elimina las capas de clasificación originales del modelo (usadas en ImageNet), ya que se desea entrenar para nuevas clases.
* input_shape=(224, 224, 3): Define la forma esperada de las imágenes de entrada (224x224 píxeles, 3 canales RGB).

Un Modelo Secuencial que se destaca por: 
* GlobalAveragePooling2D: esta capa reduce cada mapa de características a un único valor lo que ayuda a reducir el número de parámetros y evitar sobreajuste. 
* Una capa densa intermedia de 256 con una activación ReLu, que permite al modelo aprender relaciones específicas entre las que son extraídas por VGG16.
* Una capa de salida con activación softmax, que se ha escogido y utilizado esta activación por tener una clasificación multiclase. 

Para compilar el modelo se utilizan los siguientes parámetros: 
* categorical_crossentropy: Se usa para problemas de clasificación multiclase.
* AdamW(1e-4): Se usa una tasa de aprendizaje de 1e-4.
* Accuracy: para monitorear la precisión durante entrenamiento y validación.
Dichas especificaciones del modelo se han investigado y tomado de las investigaciones y soluciones que se han desarrollado en otros Papers. 

### Evaluación del modelo
Para la evaluación del modelo se tomarán cuenta los valores de Accuracy, precision y recall tres criterios utilizados para evaluar un modelo de clasificación. Asimismo la Matriz de Confusión han sido utilizados para evaluar el modelo. 
* Accuracy:  0.7223
* Recall:    0.5398
* F1 Score:  0.5696

#### Matriz de Confusión 

![matriz1](https://github.com/user-attachments/assets/d9016500-317d-42e9-bda0-e18f3880a998)


Con el primer modelo que se desarrolló se puede observar que se obtiene un valor de Accuracy de 72%, y si observamos la matriz de confusión no existen tantos datos que se salgan de la clase que debe de predecir el modelo. Sin embargo, es necesario hacer modificaciones en el modelo para que se pueda obtener un mayor resultado. 

### Mejora del modelo propuesto 
A pesar de que el primer modelo ha obtenido un accuracy alto, se han encontrado mejoras significativas para que funcione mejor al agregar nuevas capas y dropout: 
* Dos capas densas grandes con 4096 neuronas y activación ReLU
* Dropout (0.5) para prevenir sobreajuste, desconectando aleatoriamente la mitad de las neuronas durante el entrenamiento.
* Se agregan varias capas densas adicionales para permitir al modelo aprender representaciones más complejas y específicas del conjunto de datos de frutas y verduras sanas vs podridas.
* El número de neuronas va decreciendo, lo que actúa como una forma de compresión progresiva de características, ayudando a reducir el sobreajuste y a mejorar la generalización.

El modelo mejorado, al tener capas más densas y mayor número de neuronas permite que se tenga una mayor capacidad de representar patrones que pueden llegar a ser complejos en los datos. Al implementar Dropout evita el sobre ajuste y al tener una arquitectura con capas más profundas y progresivas permite que las características aprendidas por VGG16 se transformen gradualmente en decisiones de clasificación más refinadas. 

En los resultados de este modelo se han obtenido valores de Accuracy, F1 Score y recall tres criterios utilizados para evaluar un modelo de clasificación. Asimismo la Matriz de Confusión han sido utilizados para evaluar el modelo y poder compararlo con el primer modelo que se desarrollo. 
* Accuracy:  0.6790
* Recall:    0.4303
* F1 Score:  0.4140

#### Matriz de Confusión 2ndo Modelo
![matriz2](https://github.com/user-attachments/assets/87f8dc16-d2d5-493f-aedc-4f618521aabc)


### Resultados:
Aunque el modelo mejorado fue diseñado con una arquitectura más profunda y mayor capacidad para aprender representaciones complejas, no logró superar al modelo base en términos de precisión ni desempeño general. Esto se debe principalmente a que requirió mayor tiempo de entrenamiento o ajuste de hiperparámetros, lo cual no se aplicó completamente en esta etapa. Por su parte, el modelo base, con una estructura más simple, demostró ser más efectivo con menos recursos, logrando mejores métricas de clasificación. La elección entre ambos depende del contexto: el modelo base es ideal para soluciones rápidas, eficientes y con buen rendimiento, mientras que el modelo mejorado tiene potencial para ofrecer mayor precisión si se entrena adecuadamente y se aplica fine-tuning.

## Conclusiones 
En esta investigación se implementaron dos versiones del modelo basadas en la arquitectura preentrenada VGG16, aplicando la técnica de Transfer Learning para la clasificación de frutas y verduras en estado sano y podrido.

El primer modelo, de estructura simple con una sola capa densa de 256 neuronas, obtuvo un accuracy de 72.23%, con métricas de recall 0.5398 y F1-score 0.5696. Estos resultados demuestran que incluso con una arquitectura ligera es posible obtener una precisión razonable, especialmente cuando se cuenta con un buen preprocesamiento de datos y un modelo base robusto como VGG16.

El segundo modelo, una versión mejorada con múltiples capas densas (4096 → 1028 → 512 → 256) y técnicas de regularización como Dropout, fue diseñado para capturar representaciones más complejas y específicas del conjunto de datos. Sin embargo, sus métricas de evaluación (accuracy 67.90%, recall 0.4303, F1-score 0.4140) indican que no alcanzó el rendimiento esperado. Esto sugiere que, a pesar de su mayor capacidad, al modelo le faltó mayor tiempo de entrenamiento y un ajuste más fino de hiperparámetros, como el número de épocas, el aprendizaje progresivo (unfreezing de capas de VGG16), o estrategias más agresivas de regularización/adaptación de tasa de aprendizaje.


## Referencias 
S. Aksoy, P. Demircioglu y I. Bogrekci, "Evaluating pretrained CNNs for distinguishing fresh vs rotten fruits and vegetables," Journal of Applied Horticulture, vol. 26, no. 3, pp. 361–366, 2024. [En línea]. Disponible: https://doi.org/10.37855/jah.2024.v26i03.69
M. S. Miah, T. Tasnuva, M. Islam, et al., "An Advanced Method of Identification Fresh and Rotten Fruits using Different Convolutional Neural Networks," 2021 International Conference on Computer Communications and Networks Technology (ICCCNT), July 2021, doi: 10.1109/ICCCNT51525.2021.9580117. Link: https://www.researchgate.net/publication/355895633_An_Advanced_Method_of_Identification_Fresh_and_Rotten_Fruits_using_Different_Convolutional_Neural_Networks 
FAO (2020) Frutas y verduras – esenciales en tu dieta. EBooks. https://doi.org/10.4060/cb2395es
L. Fischer-Brandies, L. Müller, J. J. Riegger and R. Buettner, "Fresh or Rotten? Enhancing Rotten Fruit Detection With Deep Learning and Gaussian Filtering," in IEEE Access, vol. 13, pp. 31857-31869, 2025, doi: 10.1109/ACCESS.2025.3542612. Link: https://ieeexplore.ieee.org/abstract/document/10891620/authors 

