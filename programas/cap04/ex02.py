import cv2

# Carregando imagem RGB e segmentando canais
imagem = cv2.imread("frutas.jpeg")
azul, verde, vermelho = cv2.split(imagem)

# Combinando os tres canais em uma unica imagem
imagem = cv2.merge((azul, verde, vermelho))
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()