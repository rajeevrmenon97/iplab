import math
from math import log, sqrt
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from os import system

def sobel():
	G_x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
	G_y = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
	return G_x, G_y
	
	
def prewitt():
	G_x = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
	G_y = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
	return G_x, G_y

def laplacian():
	G = np.array([[0,1,0],[1, -4, 1],[0, 1, 0]])
	return G

def differential_1(img, n):
	if(n==2):
		G_x, G_y = prewitt()
	elif(n==1):
		G_x, G_y = sobel()

	
	height, width= np.shape(img)

	G_x_final=np.zeros((height,width))
	G_y_final=np.zeros((height,width))
	G_final=np.zeros((height, width))

	row_num=1

	pad_img = np.pad(img, [(row_num, row_num), (row_num, row_num)], mode = "constant")
	height+=2
	width+=(2*row_num)

	for i in range(row_num, height-row_num):
		for j in range(row_num, width-row_num):
			sum=0
			for r in range(0,3):
				for c in range(0,3):
					sum+=G_x[r,c]*pad_img[i-row_num+r,j-row_num+c]
			G_x_final[i-row_num,j-row_num]=(sum**2)

	for i in range(row_num, height-row_num):
		for j in range(row_num, width-row_num):
			sum=0
			for r in range(0,3):
				for c in range(0,3):
					sum+=G_y[r,c]*pad_img[i-row_num+r,j-row_num+c]
			G_y_final[i-row_num,j-row_num]=(sum**2)


	for i in range(0,height-2):
		for j in range(0,width-2):
			sum=0
			G_final[i,j]=(G_x_final[i-row_num,j-row_num] + G_y_final[i-row_num,j-row_num])**(1/2)

	return G_final

def differential_2(img):

	height, width= np.shape(img)

	G=laplacian()
	G_final=np.zeros((height, width))

	row_num=1

	pad_img = np.pad(img, [(row_num, row_num), (row_num, row_num)], mode = "constant")
	height+=2
	width+=(2*row_num)

	for i in range(row_num, height-row_num):
		for j in range(row_num, width-row_num):
			sum=0
			for r in range(0,3):
				for c in range(0,3):
					sum+=G[r,c]*pad_img[i-row_num+r,j-row_num+c]
			G_final[i-row_num,j-row_num]=sum

	return G_final

img = plt.imread("cameraman.tif")

while 1:
	system("clear")
	print("MENU: \n1. Sobel \n2. Prewitt \n3. Laplacian \n4. Exit")
	n= int(input("\nEnter option: "))

	if n == 4:
		break
	if n == 1 or n == 2:
		out = differential_1(img.copy(),n)
	elif n == 3:
		out = differential_2(img.copy())
	else:
		continue
	p, axarr = plt.subplots(1, 2, figsize=(12,4))
	axarr[0].imshow(img, cmap = 'gray')
	axarr[0].set_title('Original Image')
	axarr[1].imshow(out, cmap = 'gray')
	axarr[1].set_title('Output image')
	for ax in axarr.flat:
    		ax.label_outer()
	plt.show()
