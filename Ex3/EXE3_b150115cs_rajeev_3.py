import numpy as np
from math import log, pi, sqrt
from matplotlib import pyplot as plt

def DFT_1D(x, inverse = False):
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    if inverse:
        M = np.exp(2j * np.pi * k * n / N)
    else:
        M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

def DFT_2D(mat, inverse = False):
    m,n = np.shape(mat)
    row_wise = np.row_stack([DFT_1D(mat[i], inverse) for i in range(m)])
    dft = np.column_stack([DFT_1D(row_wise[:,i], inverse) for i in range(n)])
    return dft

img = plt.imread("Q3.tif")
m, n = np.shape(img)
dft = DFT_2D(img)

if m > n:
    padded_img = np.pad(img, [(0, 0), (0, m - n)], mode = "constant")
elif n > m:
    padded_img = np.pad(img, [(0, m - n), (0, 0)], mode = "constant")
else:
    padded_img = np.pad(img,50, mode = "constant")

padded_dft = DFT_2D(padded_img)

c = 20
spectrum = np.abs(dft)
spectrum = c*np.log(spectrum)

padded_spectrum = np.abs(padded_dft)
padded_spectrum = c*np.log(padded_spectrum)

p, axarr = plt.subplots(2, 2, figsize=(15,10))
axarr[0, 0].imshow(img, cmap = 'gray')
axarr[0, 0].set_title('Original Image')
axarr[0, 1].imshow(padded_img, cmap = 'gray')
axarr[0, 1].set_title('Padded Image')
axarr[1, 0].imshow(spectrum, cmap = 'gray')
axarr[1, 0].set_title('Fourier Spectrum')
axarr[1, 1].imshow(padded_spectrum, cmap = 'gray')
axarr[1, 1].set_title('Fourier Spectrum')
for ax in axarr.flat:
    ax.label_outer()
plt.show()