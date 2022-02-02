import sys
from PIL import Image, ImageOps
try:
    mult = float(sys.argv[1])
    add = float(sys.argv[2])
    im = ImageOps.grayscale(Image.open('mult_add.jpg'))
    pixelMap = im.load()

    img = Image.new('L', im.size)
    pixelsNew = img.load()


    for r in range(img.size[0]):
        for c in range(img.size[1]):
            curr_pixel1 = pixelMap[r,c]
            new_pixel = curr_pixel1*mult + add
            pixelsNew[r,c] = int(new_pixel)
    img.save("mult_add_output.jpg") 
    img.close()
except Exception as error:
    print("error: ", error)

