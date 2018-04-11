import cv2

imagemFichasVermelhas = cv2.imread("fichas-vermelhas.bmp")
imagemFichasPretas = cv2.imread("fichas-pretas.bmp")

imagem = cv2.add(imagemFichasVermelhas, imagemFichasPretas)

cv2.imshow("Resultado", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()