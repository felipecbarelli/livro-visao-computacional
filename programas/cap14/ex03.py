import cv2
import numpy as np

totalAnterior = 0
video = cv2.VideoCapture("contagem-de-objetos-480.mov")

while True:
  ret, frameRGB = video.read()
  frameCinza = cv2.cvtColor(frameRGB, cv2.COLOR_RGB2GRAY)
  tipo = cv2.THRESH_BINARY_INV
  ret, frameBinarizado = cv2.threshold(frameCinza, 200, 255, tipo)
  contornos, hierarquia = cv2.findContours(frameBinarizado, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  totalAtual = len(contornos)
  if totalAtual != totalAnterior:
    totalAnterior = totalAtual
    print totalAtual
  
  cv2.imshow("Video", frameRGB)
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

video.release()
cv2.destroyAllWindows()