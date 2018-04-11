import cv2

imagem = cv2.imread("frutas.jpeg")
valorPixel = imagem[150,150,0]
print(valorPixel)