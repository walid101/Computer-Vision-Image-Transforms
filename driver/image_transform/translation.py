import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from PIL import Image, ImageOps
from matrix_transformations.Matrix import Matrix
from matrix_transformations.Transforms import Transforms
from Image_Conv import ImgToMatrix
from Image_Conv import MatrixToImg

#x_trans = int(sys.argv[1])
im = Image.open('trans.jpg')
conv_mat_pair = ImgToMatrix.ConvImgToMatrix(im)
conv_mat = conv_mat_pair.coord_mat
conv_mat = Transforms.translate(conv_mat, 100, 0)
output_img = MatrixToImg.ConvMatrixToImg(conv_mat_pair)
output_img.save("Translation.jpg")
output_img.close()
im.close()


