import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('blob.jpg',0)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (55, 55))
kernel_small = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (35, 35))
img_dilation = cv2.dilate(img, kernel, iterations=1)
remove_noise = cv2.dilate(img, kernel_small, iterations=1)
out1 = cv2.erode(img_dilation, kernel, iterations=1)
out2 = 255 - out1 + cv2.erode(remove_noise, kernel_small, iterations=1)


p, axarr = plt.subplots(1, 3, figsize=(12,4))
axarr[0].imshow(img, cmap = 'gray')
axarr[0].set_title('Original Image')
axarr[1].imshow(out1, cmap = 'gray')
axarr[1].set_title('Big Blobs')
axarr[2].imshow(out2, cmap = 'gray')
axarr[2].set_title('Small Blobs')
for ax in axarr.flat:
 	ax.label_outer()
plt.show()