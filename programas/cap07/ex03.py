import cv2

imgOriginal = cv2.imread("lua.jpeg", 0)
imgFiltrada = cv2.Laplacian(imgOriginal, cv2.CV_8U)
imgRealcada = cv2.subtract(imgOriginal, imgFiltrada)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Filtrada", imgFiltrada)
cv2.imshow("Realcada", imgRealcada)

cv2.waitKey(0)
cv2.destroyAllWindows()