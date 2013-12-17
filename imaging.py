import sys, Image, ImageDraw, random

inputImage = Image.open("regions.png")
size = inputImage.size
temp_size = width, height = (100, 100)
inputImage = inputImage.resize(temp_size)
white = (255, 255, 255)
black = (0, 0, 0)

def crawl(i, j, change):
	if i<0 or i>=width or j<0 or j>=height: return
	if img[i,j] == black:
		img[i,j] = change
		crawl(i+1, j, change)
		crawl(i, j+1, change)
		crawl(i-1, j, change)
		crawl(i, j-1, change)


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
	for j in range(0, height):
		x, y, z = (random.random()*1000)%255, (random.random()*1000)%255, (random.random()*1000)%255
		if img[i, j] == black:
			change = (int(x), int(y), int(z))
			crawl(i, j, change)

outputImage = outputImage.resize(size)
outputImage.show()
outputImage.save("output.jpg")
