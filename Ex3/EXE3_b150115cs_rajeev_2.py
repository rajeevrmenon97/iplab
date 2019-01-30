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


img = plt.imread("Q2.tif")
N,M = np.shape(img)
i, j = np.meshgrid(np.arange(M), np.arange(N))
mult_factor = np.power( np.ones((N,M)) * -1 , i + j )
tmp = img * mult_factor
dft = DFT_2D(tmp)
idft = DFT_2D(dft.conj(), inverse = True)
out_img = np.abs((mult_factor * idft.real) + (1j * idft.imag))

p, axarr = plt.subplots(1, 2, figsize=(12,4))
axarr[0].imshow(img, cmap = 'gray')
axarr[0].set_title('Original Image')
axarr[1].imshow(out_img, cmap = 'gray')
axarr[1].set_title('Output Image')
plt.show()