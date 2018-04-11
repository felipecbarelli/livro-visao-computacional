import cv2

imagem = cv2.imread("frutas.jpeg")
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

matiz, saturacao, valor = cv2.split(imagem)

cv2.imshow("Canal H", matiz)
cv2.imshow("Canal S", saturacao)
cv2.imshow("Canal V", valor)

imagem = cv2.merge((matiz, saturacao, valor))
imagem = cv2.cvtColor(imagem, cv2.COLOR_HSV2BGR)

cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()