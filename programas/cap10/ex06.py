import cv2
import numpy as np

imagemRGB = cv2.imread("puzzle.bmp")
imagemTonsDeCinza = cv2.imread("puzzle.bmp", 0)

tipo = cv2.THRESH_BINARY
ret, imgBinarizada = cv2.threshold(imagemTonsDeCinza, 127, 255, tipo)

modo = cv2.RETR_TREE;
metodo = cv2.CHAIN_APPROX_SIMPLE;

contornos, hierarquia = cv2.findContours(imgBinarizada, modo, metodo)

objeto = contornos[0]

# Obtendo os vertices do retangulo
x, y, w, h = cv2.boundingRect(objeto)

# Desenhando o retangulo na imagem imagemRGB
cv2.rectangle(imagemRGB, (x,y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Retangulo Envolvente", imagemRGB)
print(x, y, w, h)

cv2.waitKey(0)
cv2.destroyAllWindows()