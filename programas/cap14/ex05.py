import cv2
import numpy as np

video = cv2.VideoCapture("movimentacao-de-objetos-480.mov")

while True:
  ret, frameRGB = video.read()
  frameHSV = cv2.cvtColor(frameRGB, cv2.COLOR_BGR2HSV)
  tomClaro = np.array([160, 100, 100])
  tomEscuro = np.array([200, 255, 255])
  frameSegmentado = cv2.inRange(frameHSV, tomClaro, tomEscuro)

  elementoEstruturante = np.ones((10, 10), np.uint8)
  frameSegmentado = cv2.morphologyEx(frameSegmentado, cv2.MORPH_CLOSE, elementoEstruturante)
  contornos, hierarquia = cv2.findContours(frameSegmentado, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  if len(contornos) >= 1:
    objeto = contornos[0]
    momentos = cv2.moments(objeto)
    x = momentos["m10"] / momentos["m00"]
    y = momentos["m01"] / momentos["m00"]
    print("posicao: %d, %d" % (x, y))
    x, y, w, h = cv2.boundingRect(objeto)
    vertice1 = (x - 10, y - 10)
    vertice2 = (x + w + 10, y + h + 10)
    cv2.rectangle(frameRGB, vertice1, vertice2, (0, 255, 0), 2)

  cv2.imshow("Video RGB", frameRGB)
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

video.release()
cv2.destroyAllWindows()