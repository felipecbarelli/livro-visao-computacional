import cv2

imagemFichasVermelhas = cv2.imread("fichas-vermelhas.bmp")
imagemFichasPretas = cv2.imread("fichas-pretas.bmp")

imagem = cv2.addWeighted(imagemFichasPretas, 0.2, imagemFichasVermelhas, 1.0, 0)

cv2.imshow("Resultado", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()