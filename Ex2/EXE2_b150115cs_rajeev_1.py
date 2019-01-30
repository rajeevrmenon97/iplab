from PIL import Image

img = Image.open("cameraman.tif").convert("L")
height, width = img.size
out_img = Image.new(img.mode,(height,width))
mean = 0
for i in range(height):
	for j in range(width):
		mean += img.getpixel((i,j))
mean = mean//(height*width)
for i in range(height):
	for j in range(width):
		pix = img.getpixel((i,j))
		if pix > mean:
			out_img.putpixel((i,j),255)
		else:
			out_img.putpixel((i,j),0)
print("Mean pixel density: ",mean)
out_img.show()
out_img.save("1.jpg")		
