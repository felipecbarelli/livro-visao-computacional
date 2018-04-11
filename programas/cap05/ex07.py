import cv2

imagem = cv2.imread("folha-binaria.bmp", 0)
totalPixelsPreto = 0;
totalPixelsBranco = 0;

for x in range(0, 499):
  for y in range(0, 499):
    if imagem[x,y] == 255:
      totalPixelsBranco += 1;
    else:
      totalPixelsPreto += 1;

print(totalPixelsBranco)
print(totalPixelsPreto)