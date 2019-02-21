from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
from os import system

def filt(img, fil, N):
    out = img.copy()
    n = (N - 1) // 2
    for i in range(n,img.shape[0]-n):
        for j in range(n,img.shape[1]-n):
            submatrix = img[i-n:i+n+1, j-n:j+n+1]
            if fil == 1:
                ret = sorted(submatrix.flatten())[N * N // 2]
            elif fil == 2:
                ret = np.min(submatrix)
            elif fil == 3:
                ret = np.max(submatrix)
            elif fil == 4:
                ret = np.mean(submatrix)
            out[i][j] = int(ret)
    return out

img = plt.imread("cameraman.tif")
while 1:
    system("clear")
    opt = int(input("1. Median Filter \n2. Min Filter \n3. Max filter \n4. Mean filter \n5. Exit\nSelect option :"))
    if opt == 5:
        break
    n = int(input("Enter n:"))
    if 0 <= opt <= 4:
        out = filt(img.copy(), opt, n)
    else:
        continue
    p, axarr = plt.subplots(1, 2, figsize=(8,8))
    axarr[0].imshow(img, cmap = 'gray')
    axarr[0].set_title('Original Image')
    axarr[1].imshow(out, cmap = 'gray')
    axarr[1].set_title('Output Image')
    for ax in axarr.flat:
        ax.label_outer()
    plt.show()