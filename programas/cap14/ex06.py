from PIL import Image
import cv2
import pytesseract

indiceFrame = 0
valorAnterior = 0
video = cv2.VideoCapture("reconhecimento-de-caracteres-480.mov")

while True:
  indiceFrame += 1
  ret, frameRGB = video.read()
  imagem = Image.fromarray(frameRGB)

  if indiceFrame == 15:
    indiceFrame = 0
    valorAtual = pytesseract.image_to_string(imagem)
    if valorAtual != valorAnterior:
      valorAnterior = valorAtual
      print valorAtual

  cv2.imshow("Video", frameRGB)
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

video.release()
cv2.destroyAllWindows()