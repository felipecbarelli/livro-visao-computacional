import cv2
import numpy as np

# Obtendo o ponto central e raio da circunferencia
(x,y), raio = cv2.minEnclosingCircle(objeto)

centro = (int(x), int(y))
raio = int(raio)

# Desenhando a circunferencia na imagem imagemRGB
cv2.circle(imagemRGB, centro, raio, (0, 255, 0), 2)

cv2.imshow("Circunferencia Envolvente", imagemRGB)

print(x, y, raio)

cv2.waitKey(0)
cv2.destroyAllWindows()