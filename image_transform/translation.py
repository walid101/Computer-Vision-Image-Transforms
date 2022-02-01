import sys
from PIL import Image, ImageOps

x_trans = int(sys.argv[1])
im = Image.open('trans.jpg')
pixelMap1 = im.load()

size = (im.size[0], im.size[1]) #width x height
print("Size: ", im.size)
img = Image.new(im.mode, size)
pixelsNew = img.load()

for r in range(im.size[0]):
    for c in range(im.size[1]):
        curr_pixel1 = pixelMap1[r,c]
        if(r+x_trans < im.size[0]):
            pixelsNew[r+x_trans,c] = curr_pixel1
img.save("trans_output.jpg") 
img.close()


