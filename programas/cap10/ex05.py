import cv2
import numpy as np

imagem = cv2.imread("engrenagem-1.bmp", 0)
momentos = cv2.moments(imagem)
momentosDeHu = cv2.HuMoments(momentos)

print(momentosDeHu)

# Aplicando a transformação logarítmica
print(-np.sign(momentosDeHu) * np.log10(np.abs(momentosDeHu)))