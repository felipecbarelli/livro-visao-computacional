import cv2
import numpy as np

ultimaTela = indiceFrame = 0
totalAzul = totalVerde = totalRosa = 0
video = cv2.VideoCapture("objetos-coloridos-480.mov")

while True:
  indiceFrame += 1
  ret, frameRGB = video.read()
  valorMedioRGB = cv2.mean(frameRGB)
  maiorValor = np.amax(valorMedioRGB)
  indiceCanal = np.argmax(valorMedioRGB)

  if indiceFrame == 30:
    indiceFrame = 0
    if valorMedioRGB[0] == valorMedioRGB[1]:
      ultimaTela = 0
    else:
      if ultimaTela == 0:
        ultimaTela = 1
        if indiceCanal == 0:
          print "tampa azul"
          totalAzul += 1
        elif indiceCanal == 1:
          print "tampa verde"
          totalVerde += 1
        elif indiceCanal == 2:
          print "tampa rosa"
          totalRosa += 1

  cv2.imshow("Video", frameRGB)
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

video.release()
cv2.destroyAllWindows()