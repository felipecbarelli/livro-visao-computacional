import cv2

import numpy as np
from matplotlib import pyplot as grafico

imagem = cv2.imread("folha-binaria.bmp", 0)
grafico.hist(imagem.ravel(), 256, [0,256])
grafico.show()