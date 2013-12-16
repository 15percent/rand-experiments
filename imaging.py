import sys, Image, ImageDraw

inputImage = Image.open("img.jpg")


txt = "Not really a fancy text!"
size = (1150, 550)
color = (0, 225, 0)
img = Image.new('RGB', size, color)
imgDrawer = ImageDraw.Draw(img)
imgDrawer.text((15, 120), txt)
#img.show()

inputImage.save("output.jpg")
outputImage = Image.open("output.jpg").resize(size)
outputImage.resize(size)
outputImage.show()
outputImage.save("output.jpg")
