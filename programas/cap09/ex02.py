import cv2
import numpy as np

imgOriginal = cv2.imread("comprimidos.jpeg", 0)
imgTratada = cv2.medianBlur(imgOriginal, 7)

imgBinarizada = cv2.adaptiveThreshold(imgTratada, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 5)

cv2.imshow("Imagem Original", imgOriginal)
cv2.imshow("Imagem Tratada", imgBinarizada)

cv2.waitKey(0)
cv2.destroyAllWindows()