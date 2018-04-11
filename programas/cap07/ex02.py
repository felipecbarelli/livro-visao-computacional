import cv2

imgOriginal = cv2.imread("estacionamento.jpeg", 0)
imgTratada = cv2.Laplacian(imgOriginal, cv2.CV_8U)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()