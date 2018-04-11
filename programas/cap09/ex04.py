import cv2
import numpy as np

verdeRGB = np.uint8([[[0,255,0]]])
verdeHSV = cv2.cvtColor(verdeRGB, cv2.COLOR_BGR2HSV)

print verdeHSV