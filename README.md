# Object_detection_opencv

By [Luiz H. Buris](http://)

## Introdução

O rastreamento de objetos é uma tarefa muito útil quando aplicado no mundo real. Realizar o rastreamento envolve a tarefa de identificar um objeto e após isso acompanhar sua trajetória. Existem diversas maneiras para identificar um objeto é utilizar a técnica, uma dela a Haar-like. Outra maneira, é simplesmente definir uma cor específica para identificar o objeto para rastrear.

O código abaixo realiza esta tarefa. O objetivo é identificar e acompanhar um objeto na tela. Utilizamos o cv2.COLOR_BGR2HSV para converter da escala RGB (ou BGR) para HSV, o HSV foi inventado no ano de 1974, por Alvy Ray Smith. É tem a caracterizada por ser uma transformação não-linear do sistema de cores RGB, é um sistema de cores formadas pelas componentes hue (matiz), saturation (saturação) e value (valor ou brilho), a variação de cor ou tonalidade é definida pelo canal H, assim sendo possível ajustar o brilho de uma única cor, alterando um dos canais, e logo em seguida v2.medianBlur(frame_hsv ,7) para aplicar um filtro de mediana para remoção de alguns ruídos, perceba que a cor rosa mais forte com tonalidade roxa é a zona de interesse e pode ter várias tonalidades e é por isso que a função cv2.inRange() é tão importante. Essa função recebe uma variação de tonalidade de roxas e tudo que estiver entre essas variação de tonalidades será identificado como sendo parte do objeto observado. A função retorna uma imagem binarizada. Veja o exemplo abaixo:

![](https://github.com/henriqueburis/Object_detection_hsv_opencv/blob/main/fig/exemplo.PNG)


## Code organization

- `opencv_hsv.py`: .



## Train
you can now carry out "run" the python scrypt with the following command:

```sh
python3 opencv_hsv.py 

```
