from PIL import Image

img = Image.open("test.jpg").convert("L")
height, width = img.size
maxi = mini = img.getpixel((0,0))
for i in range(height):
	for j in range(width):
		if img.getpixel((i,j)) > maxi:
			maxi = img.getpixel((i,j))
		if img.getpixel((i,j)) < mini:
			mini = img.getpixel((i,j))
print("Max: ",maxi," Mini: ",mini)
input("Press any key to display image")
img.show()
img.save("1.jpg")
