import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagemOriginal = cv2.imread("containers.jpg", 0)
imagemClara = cv2.add(imagemOriginal, 40)
imagemEscura = cv2.add(imagemOriginal, -40)

cv2.imshow("Imagem Original", imagemOriginal)
cv2.imshow("Imagem Clara", imagemClara)
cv2.imshow("Imagem Escura", imagemEscura)

grafico.hist(imagemOriginal.ravel(), 256, [0,256])

grafico.figure();
grafico.hist(imagemClara.ravel(), 256, [0,256])

grafico.figure();
grafico.hist(imagemEscura.ravel(), 256, [0,256])

grafico.show()

cv2.waitKey(0)
cv2.destroyAllWindows()