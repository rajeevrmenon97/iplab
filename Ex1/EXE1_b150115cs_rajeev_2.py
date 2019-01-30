from PIL import Image

sub_qstn = 1

def resolution(img, factor):
	global sub_qstn
	height, width = img.size
	out_img = Image.new(img.mode,(height//factor,width//factor))
	i = j = p = q= 0
	while i < height:
		j = 0
		q = 0
		while j < width:
			total = 0
			for l in range(factor):
				for m in range(factor):
					total += img.getpixel((i + l, j + m))
			avg = total // (factor * factor)	
			out_img.putpixel((p,q), avg)
			q += 1
			j += factor
		i += factor
		p += 1
	fin_img = Image.new(img.mode,(height,width))
	i = j = p = q = 0
	while i < height:
                j = 0
                q = 0
                while j < width:
                        for l in range(factor):
                                for m in range(factor):
                                        fin_img.putpixel((i + l, j + m), out_img.getpixel((p, q)))
                        q += 1
                        j += factor
                i += factor
                p += 1
	input("Press any key to view " + str(1024//factor) + "x" + str(1024//factor) + " image")
	out_img.show()
	input("Press any key to show image scaled up to 1024x1024")
	fin_img.show()
	fin_img.save("2 " + str(sub_qstn) + ".jpg")
	sub_qstn += 1

img = Image.open("test.jpg").convert("L")
resolution(img,2)
resolution(img,4)
resolution(img,8)
resolution(img,16)
resolution(img,32)
resolution(img,64)
