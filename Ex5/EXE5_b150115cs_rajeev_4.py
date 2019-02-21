from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

def get_pxl(img,i,j):
    try:
        pxl = img.getpixel((i,j))
    except:
        pxl = 0
    return pxl

def blur(img):
    img1 = Image.fromarray(img)
    mask = [0] * 9
    output = Image.new("L",(img1.size[0],img1.size[1]))
    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            mask[0] = get_pxl(img1,i-1,j-1)
            mask[1] = get_pxl(img1,i-1,j)
            mask[2] = get_pxl(img1,i-1,j+1)
            mask[3] = get_pxl(img1,i,j-1)
            mask[4] = get_pxl(img1,i,j)
            mask[5] = get_pxl(img1,i,j+1)
            mask[6] = get_pxl(img1,i+1,j-1)
            mask[7] = get_pxl(img1,i+1,j)
            mask[8] = get_pxl(img1,i+1,j+1)
            mean = sum(mask) // 9
            output.putpixel((i,j),mean)
    return np.asarray(output)

img = plt.imread("cameraman.tif")
b = blur(img)
gmask = img - b
new_img = img + gmask

p, axarr = plt.subplots(2, 2, figsize=(8,8))
axarr[0, 0].imshow(img, cmap = 'gray')
axarr[0, 0].set_title('Original Image')
axarr[0, 1].imshow(b, cmap = 'gray')
axarr[0, 1].set_title('Blurred Image')
axarr[1, 0].imshow(gmask, cmap = 'gray')
axarr[1, 0].set_title('gmask')
axarr[1, 1].imshow(new_img, cmap = 'gray')
axarr[1, 1].set_title('gmask + original image')
for ax in axarr.flat:
    ax.label_outer()
plt.show()