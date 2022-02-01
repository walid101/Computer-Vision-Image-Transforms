import sys
from PIL import Image, ImageOps
alpha = float(sys.argv[1])
if(alpha < 0 or alpha > 1):
    raise Exception("alpha must be between 0 and 1")
im = ImageOps.grayscale(Image.open('dyadic1.jpg'))
im2 = ImageOps.grayscale(Image.open('dyadic2.jpg'))
pixelMap1 = im.load()
pixelMap2 = im2.load()

img = Image.new('L', im.size)
pixelsNew = img.load()


for r in range(img.size[0]):
    for c in range(img.size[1]):
        curr_pixel1 = pixelMap1[r,c]
        curr_pixel2 = pixelMap1[r,c] if im2.size[0] <= r or im2.size[1] <= c else pixelMap2[r,c]
        new_pixel = int((1-alpha)*curr_pixel1 + (alpha)*curr_pixel2)
        pixelsNew[r,c] = new_pixel
img.save("dyadic_output.jpg") 
img.close()

