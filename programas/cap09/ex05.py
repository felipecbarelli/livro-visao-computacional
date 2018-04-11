import cv2
import numpy as np
 
imgRGB = cv2.imread("cubo-magico.jpeg")
imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)

tomClaro = np.array([160, 100, 100])
tomEscuro = np.array([200, 255, 255])

imgSegmentada = cv2.inRange(imgHSV, tomClaro, tomEscuro)

cv2.imshow("Original", imgRGB) 
cv2.imshow("Segmentada", imgSegmentada)

cv2.waitKey(0)
cv2.destroyAllWindows()