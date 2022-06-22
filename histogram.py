import cv2
import numpy as np
from matplotlib import pyplot as plt

image=cv2.imread("Watermark.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_,biner=cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
plt.hist(gray.ravel(),256,[0,256])
plt.show()

cv2.imshow("Binary", biner)

cv2.waitKey(0)
cv2.destroyAllWindows()