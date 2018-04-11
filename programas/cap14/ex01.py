import cv2
import numpy as np

indiceFrame = totalVerticesAnterior = 0
valoresMedidos = np.zeros(7)
video = cv2.VideoCapture("formas-geometricas-480.mov")

while True:
  ret, frameRGB = video.read()
  frameCinza = cv2.cvtColor(frameRGB, cv2.COLOR_RGB2GRAY)
  tipo = cv2.THRESH_BINARY
  ret, frameBinarizado = cv2.threshold(frameCinza, 127, 255, tipo)

  valorMedioAtual = int(cv2.mean(frameBinarizado)[0])

  if valorMedioAtual != 0:
    if valorMedioAtual == int(cv2.mean(valoresMedidos)[0]):
      contornos, hierarquia = cv2.findContours(frameBinarizado, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      objeto = contornos[0]
      perimetro = cv2.arcLength(objeto, True)
      poligono = cv2.approxPolyDP(objeto, 0.03 * perimetro, True)
      totalVertices = len(poligono)

      if totalVertices != totalVerticesAnterior:
        totalVerticesAnterior = totalVertices
        if totalVertices == 3:   print "triangulo"
        elif totalVertices == 4: print "quadrado"
        elif totalVertices > 7:  print "circulo"

  valoresMedidos[indiceFrame] = valorMedioAtual
  if indiceFrame == 6:
    indiceFrame = -1

  indiceFrame += 1
  cv2.imshow("Video", frameRGB)
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

video.release()
cv2.destroyAllWindows()