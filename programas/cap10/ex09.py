import cv2
import numpy as np

ellipse = cv2.fitEllipse(objeto)
angulo = ellipse[2]
print(angulo)

cv2.waitKey(0)
cv2.destroyAllWindows()