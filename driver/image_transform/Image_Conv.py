from PIL import Image, ImageOps
from matrix_transformations.Matrix import Matrix
class ImgToMatrix:
    def __init__(self, coord_mat, pixel_mat, image):
        self.coord_mat = coord_mat
        self.pixel_mat = pixel_mat
        self.image = image
    @staticmethod
    def ConvImgToMatrix(im):
        pixelMap = im.load()
        width = im.size[0]
        height = im.size[1]
        img_matrix = Matrix(None, im.size[0]*im.size[1], 3)# Coordinate Matrix
        pixel_matrix = Matrix(None, im.size[0]*im.size[1], 1)# Coresponding Pixel Matrix
        for i in range(im.size[0]*im.size[1]):
            img_matrix.arr[2][i] = 1
        
        counter = 0
        for r in range(im.size[0]):
            for c in range(im.size[1]):
                curr_pixel = pixelMap[r,c]
                #print("r*width+c = ", r*width+c)
                try:
                    img_matrix.arr[0][counter] = c # X
                    img_matrix.arr[1][counter] = r # Y
                    pixel_matrix.arr[0][counter] = curr_pixel 
                    counter+=1
                except Exception as error:
                    print("Error : ", error)
                    print("r*width + c = ", r*width+c)
        return ImgToMatrix(img_matrix, pixel_matrix, im)

class MatrixToImg:
    def __init__(self, M):
        self.coord_mat = M.coord_mat
        self.pixel_mat = M.pixel_mat
    def ConvMatrixToImg(M):
        coord_mat = M.coord_mat
        pixel_mat = M.pixel_mat
        img = Image.new(M.image.mode, M.image.size)
        pixelsNew = img.load()
        for i in range(len(M.coord_mat.arr[0])):
            x = M.coord_mat.arr[1][i]
            y = M.coord_mat.arr[0][i]
            if(x < img.size[0] and y < img.size[1]):
                pixelsNew[x,y] = pixel_mat.arr[0][i]
        return img 
