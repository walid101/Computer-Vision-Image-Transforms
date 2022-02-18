import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Kernel import Kernel
from convolution import Convolution as conv
from matrix_transformations.Matrix import Matrix 
from PIL import Image, ImageOps
from image_transform.Image_Conv import ImgToMatrix as ITM
from image_transform.Image_Conv import MatrixToImg as MTI
'''arr = [[1,2,3],
       [2,5,2],
       [6,7,2]]
A = Matrix(arr, len(arr), len(arr[0]))
'''
convol = Kernel.Gaussian(3,3)
B = Matrix(convol, len(convol), len(convol[0]))
#result = conv.convolve(A,B)
#Matrix.display_matrix(result)

im = ImageOps.grayscale(Image.open('conv.jpg'))
pixelMap1 = im.load()

img = Image.new('L', im.size)
pixelsNew = img.load()

input = ITM.ConvImgToMatrix(im) # gives matrix
print(len(input.pixel_mat.arr[0]))
output = conv.convolve(input.pixel_mat, B)

img_output = MTI.ConvMatrixToImg()
img_output.save("conv_output.jpg")