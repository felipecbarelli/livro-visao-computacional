import cv2

captura = cv2.VideoCapture(0)

while True:
  ret, frame = captura.read()
  cv2.imshow("Imagem", frame)

  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

captura.release()
cv2.destroyAllWindows()