import cv2
import numpy as np

imagem = cv2.imread("quadrado.bmp", 0)
momentos = cv2.moments(imagem)

print(momentos)