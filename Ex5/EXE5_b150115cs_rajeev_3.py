from matplotlib import pyplot as plt
import numpy as np

def equalize_image(image):
    image_histogram, bins = np.histogram(image.flatten(), 256)
    c = image_histogram.cumsum()
    c = 255 * c / c.max()
    image_equalized = np.interp(image.flatten(), bins[:-1], c)
    return image_equalized.reshape(image.shape)


img = plt.imread("cameraman.tif")

dark = img.copy()
dark = dark / 2
dark[0][0] = 0
dark[255][255] = 255

eq = equalize_image(dark)

p, axarr = plt.subplots(3, 2, figsize=(8,8))
axarr[0, 0].imshow(img, cmap = 'gray')
axarr[0, 0].set_title('Original Image')
axarr[0, 1].hist(img.ravel(), bins=256, range=(0,256), fc='k', ec='k')
axarr[0, 1].set_title('Original Histogram')
axarr[1, 0].imshow(dark, cmap = 'gray')
axarr[1, 0].set_title('Dark Image')
axarr[1, 1].hist(dark.ravel(), bins=256, range=(0,256), fc='k', ec='k')
axarr[1, 1].set_title('Dark Image Histogram')
axarr[2, 0].imshow(eq, cmap = 'gray')
axarr[2, 0].set_title('Histogram equalized')
axarr[2, 1].hist(eq.ravel(), bins=256, range=(0,256), fc='k', ec='k')
axarr[2, 1].set_title('Final Image Histogram')
for ax in axarr.flat:
    ax.label_outer()
plt.show()