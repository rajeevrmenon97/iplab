import numpy as np
from math import log, pi, sqrt, pow
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
    return np.matmul(np.matmul(H, mat), H)

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
    return np.matmul(np.matmul(W, mat), W)

def KLT(a):
    val,vec = np.linalg.eig(np.cov(a))
    klt = np.dot(vec,a)
    return klt,vec,val

arr = np.array([[2, 1, 2, 1],[1, 2, 3, 2],[2, 3, 4, 3],[1, 2, 3, 2]])
print(hadamard(arr.copy()))
print(walsh(arr.copy()))
klt, vec, val = KLT(arr)
print(klt)