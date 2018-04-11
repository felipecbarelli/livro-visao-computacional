import cv2
import numpy as np

imagem = cv2.imread("graos-de-cafe.jpeg", 0)

metodo = cv2.THRESH_BINARY_INV
ret, imgBinarizada = cv2.threshold(imagem, 135, 255, metodo)

e = np.ones((3, 3), np.uint8)
imgTratada = cv2.morphologyEx(imgBinarizada, cv2.MORPH_CLOSE, e)
imgTratada = cv2.erode(imgTratada, e, iterations = 2)

imgSegmentada = cv2.Canny(imgTratada, 100, 200)

cv2.imshow("Binarizada", imgBinarizada)
cv2.imshow("Tratada", imgTratada)
cv2.imshow("Segmentada", imgSegmentada)

cv2.waitKey(0)
cv2.destroyAllWindows()