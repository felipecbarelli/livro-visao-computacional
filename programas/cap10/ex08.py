import cv2
import numpy as np

# Obtendo a elipse
ellipse = cv2.fitEllipse(objeto)

# Desenhando a elipse na imagem imagemRGB
cv2.ellipse(imagemRGB, ellipse, (0, 255, 0), 2)
cv2.imshow("Elipse ajustada", imagemRGB)

print(ellipse)

cv2.waitKey(0)
cv2.destroyAllWindows()