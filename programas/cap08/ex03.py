import cv2
import numpy as np

imagemOriginal = cv2.imread("rolamento-ruido-externo.bmp", 0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
imagemProcessada = cv2.morphologyEx(imagemOriginal, cv2.MORPH_OPEN, elementoEstruturante)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()