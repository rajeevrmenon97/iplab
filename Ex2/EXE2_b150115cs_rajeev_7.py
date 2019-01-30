from PIL import Image

def and_img(im1, im2):
	h,w = im1.size
	out_img = Image.new(im1.mode,(h,w))
	for i in range(h):
		for j in range(w):
			pix = im1.getpixel((i,j)) & im2.getpixel((i,j))
			if pix > 255:
				pix = 255
			out_img.putpixel((i,j),pix)
	return out_img

def or_img(im1,im2):
        h,w = im1.size
        out_img = Image.new(im1.mode,(h,w))
        for i in range(h):
                for j in range(w):
                        pix = im1.getpixel((i,j)) | im2.getpixel((i,j))
                        if pix > 255:
                                pix = 255
                        out_img.putpixel((i,j),pix)
        return out_img

def complement(im1):
        h,w = im1.size
        out_img = Image.new(im1.mode,(h,w))
        for i in range(h):
                for j in range(w):
                        pix = 255 - im1.getpixel((i,j))
                        if pix > 255:
                                pix = 255
                        out_img.putpixel((i,j),pix)
        return out_img

im1 = Image.open("cameraman.tif").convert("L")
im2 = Image.open("bridge.jpg").convert("L")
im3 = Image.open("angio.tif").convert("L")

input("And operation")
out = and_img(im1, im2)
out.show()
out.save("7_a.jpg")

input("Or operation")
out = or_img(im1, im2)
out.show()
out.save("7_b.jpg")

input("Complement")
out = complement(im3)
out.show()
out.save("7_c.jpg")
