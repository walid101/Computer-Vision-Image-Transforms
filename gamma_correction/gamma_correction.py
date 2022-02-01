import sys
from PIL import Image
try:
    gamma_factor = float(sys.argv[1])
    im = Image.open('pre_gamma.jpg')
    pixelMap = im.load()

    img = Image.new( 'L', im.size)
    pixelsNew = img.load()

    for r in range(img.size[0]):
        for c in range(img.size[1]):
            curr_pixel = pixelMap[r,c]
            new_pixel = int(curr_pixel[2]**(gamma_factor))
            pixelsNew[r,c] = new_pixel
    img.save("gamma_output.jpg")
    img.close()
except Exception as error:
    print(error)
    print("please enter a gamma factor")