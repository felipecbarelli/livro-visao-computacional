import cv2
import numpy as np

# carrega a imagem do objeto com dois furos
imagem = cv2.imread("circulo-perfurado-2.bmp", 0)

tipo = cv2.THRESH_BINARY
ret, imgBinarizada = cv2.threshold(imagem, 127, 255, tipo)

modo = cv2.RETR_TREE;
metodo = cv2.CHAIN_APPROX_SIMPLE;
contornos, hierarquia = cv2.findContours(imgBinarizada, modo, metodo)

# obtem o total de contornos e subtrai um
furos = len(contornos) - 1

print(furos)

cv2.waitKey(0)
cv2.destroyAllWindows()