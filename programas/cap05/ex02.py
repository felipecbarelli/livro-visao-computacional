import cv2

imagem = cv2.imread("frutas.jpeg")
imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
valorPixel = imagem[150,150]
print(valorPixel)