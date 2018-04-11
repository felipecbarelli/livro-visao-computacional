import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagem = cv2.imread("folha-colorida.bmp")
azul, verde, vermelho = cv2.split(imagem)

grafico.hist(azul.ravel(), 256, [0,256])

grafico.figure();
grafico.hist(verde.ravel(), 256, [0,256])

grafico.figure();
grafico.hist(vermelho.ravel(), 256, [0,256])

grafico.show()