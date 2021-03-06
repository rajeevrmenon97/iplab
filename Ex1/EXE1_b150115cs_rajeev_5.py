from PIL import Image
import math

img = Image.open("test.jpg").convert("L")

out_img = Image.new(img.mode,(img.size[0],img.size[1]))
for i in range(img.size[0]):
	for j in range(img.size[1]):
		pix = img.getpixel((i,j))
		if 0*255 <= pix < 0.25*255:
			out_img.putpixel((i,j),0)
		elif 0.25*255 <= pix < 0.5*255:
                        out_img.putpixel((i,j),int(round(0.25*255)))
		elif 0.5*255 <= pix < 0.75*255:
                        out_img.putpixel((i,j),int(round(0.5*255)))
		elif 0.75*255 <= pix < 1*255:
                        out_img.putpixel((i,j),int(round(0.75*255)))
		else:
                        out_img.putpixel((i,j), 255)
out_img.show()
out_img.save("5.jpg")
