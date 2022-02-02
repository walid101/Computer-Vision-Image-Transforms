import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from PIL import Image, ImageOps
from matrix_transformations.Matrix import Matrix
from Image_Conv import ImgToMatrix
from Image_Conv import MatrixToImg

#x_trans = int(sys.argv[1])
im = Image.open('trans.jpg')
conv_mat_pair = ImgToMatrix.ConvImgToMatrix(im)
output_img = MatrixToImg.ConvMatrixToImg(conv_mat_pair)
output_img.save("Translation.jpg")
output_img.close()
'''
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
'''
im.close()


