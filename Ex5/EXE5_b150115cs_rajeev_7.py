import math
from math import log, sqrt, pow
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def ideal(img,D_o):
    height, width = np.shape(img)
    H = np.zeros((height,width))
    
    for u in range(height):
        for v in range(width):
            D_uv = sqrt((u * u) + (v * v))
            if(D_uv <= D_o):
                H[u,v] = 1
    return H

def butterworth(img,D_o,n):
    H = np.zeros(np.shape(img), dtype=complex)
    N = len(img)
    for u in range(N):
        for v in range(N):
            D_uv = sqrt((u * u) + (v * v))
            H[u,v] = 1 / (1 + pow((D_uv / D_o ),(2*n)))
    return H

def get_gaussian_low(img,D_o):
	height, width = np.shape(img)
	H=np.zeros((height,width),dtype='complex')
	
	for u in range(height):
		for v in range(width):
			D_uv=float(((u**2)+(v**2))**(1/2))
			H[u,v]=np.exp(-(D_uv**2)/(2*(D_o**2)))
	return H

def apply_filter(img,D_o,opt):
    height,width=np.shape(img)
    
    G = np.zeros((height,width))

    F = np.fft.fft2(img)
    if(opt == 1):
        H = ideal(img,D_o)
    elif(opt == 2):
        H = butterworth(img,D_o,2)
    elif(opt==3):
        H=get_gaussian_low(img,D_o)

    
    G = np.multiply(F,H)
    idft = np.fft.ifft2(G)
    return np.abs(idft)


img = plt.imread("cameraman.tif")

A=apply_filter(img,10,1)
B=apply_filter(img,10,2)
C=apply_filter(img,60,1)
D=apply_filter(img,60,2)
E=apply_filter(img,460,1)
F=apply_filter(img,460,2)
X=apply_filter(img,10,3)
Y=apply_filter(img,60,3)
Z=apply_filter(img,460,3)


p, axarr = plt.subplots(3, 3, figsize=(12,8))
axarr[0, 0].imshow(X, cmap = 'gray')
axarr[0, 0].set_title('Gaussian Low, D0=10')
axarr[0, 1].imshow(A, cmap = 'gray')
axarr[0, 1].set_title('Ideal Low, D0=10')
axarr[0, 2].imshow(B, cmap = 'gray')
axarr[0, 2].set_title('Butterworth Low, D0=10')
axarr[1, 1].imshow(C, cmap = 'gray')
axarr[1, 1].set_title('Ideal Low, D0=60')
axarr[1, 2].imshow(D, cmap = 'gray')
axarr[1, 2].set_title('Butterworth Low, D0=60')
axarr[1, 0].imshow(Y, cmap = 'gray')
axarr[1, 0].set_title('Gaussian Low, D0=60')
axarr[2, 1].imshow(E, cmap = 'gray')
axarr[2, 1].set_title('Ideal Low, D0=460')
axarr[2, 2].imshow(F, cmap = 'gray')
axarr[2, 2].set_title('Butterworth Low, D0=460')
axarr[2, 0].imshow(Z, cmap = 'gray')
axarr[2, 0].set_title('Gaussian Low, D0=460')

for ax in axarr.flat:
    ax.label_outer()
plt.show()

