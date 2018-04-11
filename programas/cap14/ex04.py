import cv2
import numpy as np

video = cv2.VideoCapture("movimentacao-de-objetos-480.mov")

while True:
  ret, frameRGB = video.read()
  frameCinza = cv2.cvtColor(frameRGB, cv2.COLOR_RGB2GRAY)
  tipo = cv2.THRESH_BINARY_INV
  ret, frameBinarizado = cv2.threshold(frameCinza, 200, 255, tipo)

  contornos, hierarquia = cv2.findContours(frameBinarizado, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  if len(contornos) == 2:
    momentosC1 = cv2.moments(contornos[0])
    momentosC2 = cv2.moments(contornos[1])
    C1x = momentosC1["m10"] / momentosC1["m00"]
    C1y = momentosC1["m01"] / momentosC1["m00"]
    C2x = momentosC2["m10"] / momentosC2["m00"]
    C2y = momentosC2["m01"] / momentosC2["m00"]
    
    distancia = int(np.sqrt(((C2x - C1x)**2) + ((C2y - C1y)**2)))
    print distancia

  cv2.imshow("Video", frameRGB)
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

video.release()
cv2.destroyAllWindows()