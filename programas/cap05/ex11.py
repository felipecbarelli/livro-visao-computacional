import cv2
import numpy as np

imagemOriginal = cv2.imread("folha.jpeg", 0)
totalLinhas, totalColunas = imagemOriginal.shape

matriz = cv2.getRotationMatrix2D((totalColunas / 2, totalLinhas / 2), 90, 1)
imagemRotacionada = cv2.warpAffine(imagemOriginal, matriz, (totalColunas, totalLinhas))

cv2.imshow("Resultado", imagemRotacionada)

cv2.waitKey(0)
cv2.destroyAllWindows()