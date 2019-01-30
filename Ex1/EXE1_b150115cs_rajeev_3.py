from PIL import Image
import math

img = Image.new("L",(64,64))
for i in range(64):
	for j in range(64):
		pix = int(round(abs(math.cos(math.sqrt(i*i + j*j))) * 255))
		img.putpixel((i,j),pix)
img.show()
img.save("3.jpg")
