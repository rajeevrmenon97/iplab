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


img = plt.imread("Q1.tif")

dft =  DFT_2D(img)

c = 20
magnitude_spectrum = np.abs(dft)
magnitude_spectrum = c*np.log(magnitude_spectrum)

phase_spectrum = np.angle(dft)

double_magnitude_spectrum = np.abs(dft) * 2
double_magnitude_spectrum = c*np.log(double_magnitude_spectrum)

idft = DFT_2D(dft, inverse = True)

img_removing_phase = np.abs(DFT_2D(np.abs(dft), inverse = True))
img_removing_phase = c*np.log(img_removing_phase)

p, axarr = plt.subplots(2, 3, figsize=(12,8))
axarr[0, 0].imshow(img, cmap = 'gray')
axarr[0, 0].set_title('Original Image')
axarr[0, 1].imshow(magnitude_spectrum, cmap = 'gray')
axarr[0, 1].set_title('Magnitude Spectrum')
axarr[0, 2].imshow(phase_spectrum, cmap = 'gray')
axarr[0, 2].set_title('Phase Spectrum')
axarr[1, 0].imshow(double_magnitude_spectrum, cmap = 'gray')
axarr[1, 0].set_title('Doubled Magnitude Spectrum')
axarr[1, 1].imshow(np.abs(idft), cmap = 'gray')
axarr[1, 1].set_title('IDFT')
axarr[1, 2].imshow(img_removing_phase, cmap = 'gray')
axarr[1, 2].set_title('Reconstructed without phase spectrum')
for ax in axarr.flat:
    ax.label_outer()
plt.show()