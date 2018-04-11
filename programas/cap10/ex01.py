import cv2
import statistics

imgBinaria = cv2.imread("tampa-binaria.bmp", 0)
imgTonsDeCinza = cv2.imread("tampa-tons-de-cinza.jpeg", 0)

rolBinaria = imgBinaria.ravel()
rolTonsDeCinza = imgTonsDeCinza.ravel()

print(statistics.mode(rolBinaria))
print(statistics.mode(rolTonsDeCinza))