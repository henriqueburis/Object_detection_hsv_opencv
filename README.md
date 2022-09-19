# Object_detection_opencv

By [Luiz H. Buris](http://)

## Introdução

O rastreamento de objetos é uma tarefa muito útil quando aplicado no mundo real. Realizar o rastreamento envolve a tarefa de identificar um objeto e após isso acompanhar sua trajetória. Existem diversas maneiras para identificar um objeto é utilizar a técnica, uma dela a Haar-like. Outra maneira, é simplesmente definir uma cor específica para identificar o objeto para rastrear.

O código abaixo realiza esta tarefa. O objetivo é identificar e acompanhar um objeto na tela. Perceba que o a cor azul pode ter várias tonalidades e é por isso que a função cv2.inRange() é tão importante. Essa função recebe uma cor variação de tonalidade de azuis e tudo que estiver entre essas variação de tonalidades será identificado como sendo parte do objeto observado. A função retorna uma imagem binarizada. Veja o exemplo abaixo:



