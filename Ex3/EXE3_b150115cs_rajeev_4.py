import numpy as np
from math import log, pi, sqrt
from matplotlib import pyplot as plt

def DFT_slow(x):
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

def FFT(x):
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    
    if N <= 32:
        return DFT_slow(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:N // 2] * X_odd, X_even + factor[N // 2:] * X_odd])

def DFT_2D(mat):
    m,n = np.shape(mat)
    row_wise = np.row_stack([FFT(mat[i]) for i in range(m)])
    dft = np.column_stack([FFT(row_wise[:,i]) for i in range(n)])
    return dft


img = plt.imread("Q4.tif")
dft = DFT_2D(img)
dft_of_dft = DFT_2D(dft)

c = 20
spectrum = np.abs(dft)
spectrum = c*np.log(spectrum)

double_dft_spectrum = np.abs(dft_of_dft)
double_dft_spectrum = c*np.log(double_dft_spectrum)

p, axarr = plt.subplots(1, 3, figsize=(12,4))
axarr[0].imshow(img, cmap = 'gray')
axarr[0].set_title('Original Image')
axarr[1].imshow(spectrum, cmap = 'gray')
axarr[1].set_title('DFT')
axarr[2].imshow(double_dft_spectrum, cmap = 'gray')
axarr[2].set_title('Double DFT')
plt.show()