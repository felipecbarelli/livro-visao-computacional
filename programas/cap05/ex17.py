import cv2

imagemFichaPosicao1 = cv2.imread("ficha-posicao-1.bmp")
imagemFichaPosicao2 = cv2.imread("ficha-posicao-2.bmp")

imagem = cv2.subtract(imagemFichaPosicao1, imagemFichaPosicao2)

cv2.imshow("Resultado", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()