from matplotlib import pyplot as plt
import numpy as np

img = plt.imread("cameraman.tif")
gamma = np.power(img,2)


p, axarr = plt.subplots(1, 4, figsize=(15,4))
axarr[0].imshow(img, cmap = 'gray')
axarr[0].set_title('Original Image')
axarr[1].hist(img.ravel(), bins=256, range=(0,256), fc='k', ec='k')
axarr[1].set_title('Original Histogram')
axarr[2].hist(gamma.ravel(), bins=256, range=(0,256), fc='k', ec='k')
axarr[2].set_title('Dark Image Histogram')
axarr[3].imshow(img, cmap = 'gray')
axarr[3].set_title('Histogram equalized')
for ax in axarr.flat:
    ax.label_outer()
plt.show()