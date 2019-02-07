import numpy as np
from matplotlib import pyplot as plt


def G(sigma, img):
    return np.exp(sigma * img.astype(float))

img = plt.imread("cameraman.tif")


p, axarr = plt.subplots(2, 4, figsize=(12,8))
axarr[0, 0].imshow(img, cmap = 'gray')
axarr[0, 0].set_title('Original Image')
axarr[0, 1].imshow(G(0.0, img), cmap = 'gray')
axarr[0, 1].set_title('Constant 0')
axarr[0, 2].imshow(G(0.3, img), cmap = 'gray')
axarr[0, 2].set_title('Constant 0.3')
axarr[0, 3].imshow(G(0.8, img), cmap = 'gray')
axarr[0, 3].set_title('Constant 0.8')
axarr[1, 0].imshow(G(1.0, img), cmap = 'gray')
axarr[1, 0].set_title('Constant 1')
axarr[1, 1].imshow(G(1.2, img), cmap = 'gray')
axarr[1, 1].set_title('Constant 1.2')
axarr[1, 2].imshow(G(1.7, img), cmap = 'gray')
axarr[1, 2].set_title('Constant 1.7')
axarr[1, 3].imshow(G(2.0, img), cmap = 'gray')
axarr[1, 3].set_title('Constant 2.0')
for ax in axarr.flat:
    ax.label_outer()
plt.show()