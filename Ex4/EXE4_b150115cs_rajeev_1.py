import numpy as np
from math import log, pi, sqrt, pow, cos
from matplotlib import pyplot as plt

def binbits(x, n):
    bits = bin(x).split('b')[1]
    if len(bits) < n:
        return '0' * (n - len(bits)) + bits
    else:
        return bits

def hadamard(mat):
    N = np.shape(mat)[0]
    n = int(log(N, 2))
    H = np.zeros(np.shape(mat), dtype = int)
    for x,y in np.ndindex(mat.shape):
        p = 0
        for i in range(n):
            p += int(binbits(x, n)[i]) * int(binbits(y, n)[i])
        H[x, y] = int(pow(-1, p))
    return np.matmul(np.matmul(H, mat), H)/N

def walsh(mat):
    N = np.shape(mat)[0]
    n = int(log(N, 2))
    W = np.ones(np.shape(mat), dtype = int)
    for x,y in np.ndindex(mat.shape):
        s = 1
        for i in range(n):
            p = int(binbits(x, n)[n - 1 - i]) * int(binbits(y, n)[i])
            s *= int(pow(-1, p))
        W[x, y] = s
    return np.matmul(np.matmul(W, mat), W)/N

def KLT(a):
    val,vec = np.linalg.eig(np.cov(a))
    klt = np.dot(vec,a)
    return klt,vec,val

def inverse_KLT(a, vec):
    inverse = np.linalg.inv(vec)
    iklt = np.dot(vec, a)
    return iklt


def haar_1D(x):
    N = len(x)
    output = [0.0]*N

    length = N >> 1
    while True:
        for i in range(0,length):
            summ = x[i * 2] + x[i * 2 + 1]
            difference = x[i * 2] - x[i * 2 + 1]
            output[i] = summ
            output[length + i] = difference

        if length == 1:
            return output

        x = output[:length << 1]

        length >>= 1

def haar(mat):
    m,n = np.shape(mat)
    row_wise = np.row_stack([haar_1D(mat[i]) for i in range(m)])
    transform = np.column_stack([haar_1D(row_wise[:,i]) for i in range(n)])
    return transform

def inverse_haar_1D(x):
    N = len(x)
    output = [0.0]*N

    length = N >> 1
    while True:
        for i in range(0,length):
            difference = x[i * 2] + x[i * 2 + 1]
            summ = x[i * 2] - x[i * 2 + 1]
            output[i] = summ
            output[length + i] = difference

        if length == 1:
            return output

        x = output[:length << 1]

        length >>= 1

def inverse_haar(mat):
    try:
        import pywt
        coeffs = mat, (None, None, None)
        return pywt.idwt2(coeffs, 'haar')
    except:
        pass
    m,n = np.shape(mat)
    row_wise = np.row_stack([inverse_haar_1D(mat[i]) for i in range(m)])
    transform = np.column_stack([inverse_haar_1D(row_wise[:,i]) for i in range(n)])
    return transform

def DCT_1D(vector):
	result = []
	factor = pi / len(vector)
	for i in range(len(vector)):
		sum = 0.0
		for (j, val) in enumerate(vector):
			sum += val * cos((j + 0.5) * i * factor)
		result.append(sum)
	return result

def inverse_DCT_1D(vector):
	result = []
	factor = pi / len(vector)
	for i in range(len(vector)):
		sum = vector[0] / 2.0
		for j in range(1, len(vector)):
			sum += vector[j] * cos(j * (i + 0.5) * factor)
		result.append(sum)
	return result

def DCT(mat):
    m,n = np.shape(mat)
    row_wise = np.row_stack([DCT_1D(mat[i]) for i in range(m)])
    transform = np.column_stack([DCT_1D(row_wise[:,i]) for i in range(n)])
    return transform

def inverse_DCT(mat):
    m,n = np.shape(mat)
    row_wise = np.row_stack([inverse_DCT_1D(mat[i]) for i in range(m)])
    transform = np.column_stack([inverse_DCT_1D(row_wise[:,i]) for i in range(n)])
    return transform/m


img = plt.imread("Q1.jpg")
rand = np.random.randint(2, size=np.shape(img))

print("Walsh transform")
w = walsh(img)
print("Hadamard transform")
h = hadamard(img)
print("Haar transform")
ha = haar(img)
print("Cosine transform")
c = DCT(img)
print("KL transform")
k, vec, val = KLT(img)

print("Inverse Walsh transform")
iw = walsh(np.multiply(w, rand))
print("Inverse Hadamard transform")
ih = hadamard(np.multiply(h, rand))
print("Inverse Haar transform")
iha =  inverse_haar(np.multiply(ha, rand))
print("Inverse Cosine transform")
ic = inverse_DCT(np.multiply(c, rand))
print("Inverse KL transform")
ik = inverse_KLT(np.multiply(k, rand), vec)

p, axarr = plt.subplots(2, 5, figsize=(12,8))
axarr[0, 0].imshow(20*np.log(w), cmap = 'gray')
axarr[0, 0].set_title('Walsh Transform')
axarr[0, 1].imshow(20*np.log(h), cmap = 'gray')
axarr[0, 1].set_title('Hadamard Transform')
axarr[0, 2].imshow(ha, cmap = 'gray')
axarr[0, 2].set_title('Haar Transform')
axarr[0, 3].imshow(20*np.log(c), cmap = 'gray')
axarr[0, 3].set_title('Discrete Cosine Transform')
axarr[0, 4].imshow(k, cmap = 'gray')
axarr[0, 4].set_title('KL Transform')
axarr[1, 0].imshow(iw, cmap = 'gray')
axarr[1, 0].set_title('Inverse Walsh Transform')
axarr[1, 1].imshow(ih, cmap = 'gray')
axarr[1, 1].set_title('Inverse Hadamard Transform')
axarr[1, 2].imshow(iha, cmap = 'gray')
axarr[1, 2].set_title('Inverse Haar Transform')
axarr[1, 3].imshow(ic, cmap = 'gray')
axarr[1, 3].set_title('Inverse Discrete Cosine Transform')
axarr[1, 4].imshow(ik, cmap = 'gray')
axarr[1, 4].set_title('Inverse KL Transform')
for ax in axarr.flat:
    ax.label_outer()
plt.show()