import cv2
import numpy as np

imagemOriginal = cv2.imread("engrenagem-binaria.bmp", 0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
imagemProcessada = cv2.erode(imagemOriginal, elementoEstruturante, iterations = 1)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()