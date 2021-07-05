import cv2
import numpy as np
import os

alpha = 2.5
beta = 25

klasor="testprocessed"
dosyayaz = open(klasor+".csv","w+")
image = []
adi = []
def loadImages(path="."):
  return [os.path.join(path,f) for f in os.listdir(path)]

def build_filters():
  filters = []
  ksize = 31
  for theta in np.arange(0, np.pi, np.pi / 16):
    kern = cv2.getGaborKernel((ksize, ksize), 4.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
    kern /= 1.5*kern.sum()
    filters.append(kern)
  return filters
 
def process(img, filters):
  accum = np.zeros_like(img)
  for kern in filters:
    fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
    np.maximum(accum, fimg, accum)
  return accum

dosyalar = loadImages(klasor)

for x in dosyalar:
  dosyayaz.write("'")
  dosyayaz.write(x)
  dosyayaz.write("',")
  dosyayaz.write(klasor)
  dosyayaz.write("\n")
  image.append(cv2.imread(x,1))
  adi.append(x)
dosyayaz.close()

print("okundu")

for i in range(len(image)):
  image = cv2.imread(adi[i])
  filters = build_filters()
  res1 = process(image, filters)
  #result = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
  #result = cv2.addWeighted(image,alpha, np.zeros(image.shape, image.dtype), 0, beta)
  cv2.imwrite(adi[i],res1)
print("sonuc")

