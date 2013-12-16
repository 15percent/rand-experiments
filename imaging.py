import sys, Image, ImageDraw

inputImage = Image.open("img.jpg")

white = (255, 255, 255)
black = (0, 0, 0)

size = width, height = inputImage.size
x, y, z = 255, 0, 0

inputImage.save("output.jpg")
outputImage = Image.open("output.jpg")
img = outputImage.load()

#Making all white-like pixels = (255, 255, 255) and black-like pixels = (0, 0, 0)
for i in range(0, height):
	for j in range(0, width):
		p, q, r = img[i,j]
		if p<75 and q<75 and r<75:
			img[i,j] = black
		else:
			img[i,j] = white

#Algorithm
for i in range(0, width):
	x, y, z = 255, 0, 0
	for j in range(0, height):
		if img[j, i] == black:
			while img[j, i] == black:
				img[j, i] = (x, y, z)
				j = j+1
			if x==255: x, y = 0, 255
			elif y==255: y, z = 0, 255
			elif z==255: z, x = 0, 255


outputImage.show()
outputImage.save("output.jpg")
