from PIL import Image

def addition(im1, im2):
	h,w = im1.size
	out_img = Image.new(im1.mode,(h,w))
	for i in range(h):
		for j in range(w):
			pix = im1.getpixel((i,j)) + im2.getpixel((i,j))
			if pix > 255:
				pix = 255
			out_img.putpixel((i,j),pix)
	return out_img

def subtraction(im1,im2):
        h,w = im1.size
        out_img = Image.new(im1.mode,(h,w))
        for i in range(h):
                for j in range(w):
                        pix = im1.getpixel((i,j)) - im2.getpixel((i,j))
                        if pix < 0:
                                pix = 0
                        out_img.putpixel((i,j),pix)
        return out_img

def multiplication(im1, c):
        h,w = im1.size
        out_img = Image.new(im1.mode,(h,w))
        for i in range(h):
                for j in range(w):
                        pix = im1.getpixel((i,j)) * c
                        if pix > 255:
                                pix = 255
                        out_img.putpixel((i,j),pix)
        return out_img

def division(im1, c):
        h,w = im1.size
        out_img = Image.new(im1.mode,(h,w))
        for i in range(h):
                for j in range(w):
                        pix = im1.getpixel((i,j)) // c
                        if pix < 0:
                                pix = 0
                        out_img.putpixel((i,j),pix)
        return out_img

im1 = Image.open("cameraman.tif").convert("L")
im2 = Image.open("bridge.jpg").convert("L")
im3 = Image.open("angio.tif").convert("L")

input("Addition")
out = addition(im1, im2)
out.show()
out.save("6_a.jpg")

input("Subtraction")
out = subtraction(im1, im2)
out.show()
out.save("6_b.jpg")

num = input("Enter multiplication factor: ")
out = multiplication(im1, int(num))
out.show()
out.save("6_c.jpg")

num = input("Enter division factor: ")
out = division(im1, int(num))
out.show()
out.save("6_d.jpg")
