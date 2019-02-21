from  matplotlib import pyplot as plt
import numpy as np
from math import sqrt, pi

def noise(img, mean, var):
    mu = mean
    sigma = sqrt(var)
    n = np.exp(-1 * np.square(img - mu) / (2 * sigma * sigma)) / (sigma * sqrt(2 * pi))
    return img + n

img = plt.imread("cameraman.tif")

i1 = noise(img.copy(), 0, 0.01)
i2 = noise(img.copy(), 0, 0.02)
i3 = noise(img.copy(), 0, 0.05)
i4 = noise(img.copy(), 0, 0.1)

p, axarr = plt.subplots(2, 3, figsize=(15,8))
axarr[0, 0].imshow(img, cmap = 'gray')
axarr[0, 0].set_title('Original Image')
axarr[0, 1].imshow(i1, cmap = 'gray')
axarr[0, 1].set_title('Mean = 0.0 Variance = 0.01')
axarr[0, 2].imshow(i2, cmap = 'gray')
axarr[0, 2].set_title('Mean = 0.0 Variance = 0.02')
axarr[1, 0].imshow(i3, cmap = 'gray')
axarr[1, 0].set_title('Mean = 0.0 Variance = 0.05')
axarr[1, 1].imshow(i4, cmap = 'gray')
axarr[1, 1].set_title('Mean = 0.0 Variance = 0.1')
axarr[1, 2].imshow((i1 + i2 + i3 + i4) / 4, cmap = 'gray')
axarr[1, 2].set_title('Image Averaging')
for ax in axarr.flat:
    ax.label_outer()
plt.show()