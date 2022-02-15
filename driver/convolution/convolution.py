import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from matrix_transformations.Matrix import Matrix
class Convolution:
    def __init__(self):
        self = self
    def convolve(img_mat, con_mat): 
        #if(img_mat is not Matrix or con_mat is not Matrix):
         #   raise Exception("image and convolution paramaters must be of type Matrix")
        height = len(img_mat.arr)
        width  = len(img_mat.arr[0])
        output = Matrix(None, width, height)
        for r in range(height):
            for c in range(width):
                sum = 0
                counter = 0
                for rc in range(con_mat.height):
                    for cc in range(con_mat.width):
                        center_width = int((con_mat.width)/2)
                        center_dist_x = center_width - cc
                        center_dist_y = center_width - rc
                        delta_x = int(c-center_dist_x)
                        delta_y = int(r-center_dist_y)
                        #if(delta_x > 0 and delta_x < width):
                            #if(delta_y > 0 and delta_y < height):
                        try:
                            if((delta_x >= 0 and delta_x < width) and (delta_y >= 0 and delta_y < height)):
                                print("sum = ", "con_mat at ", rc, cc, "and img_mat at ", delta_x, delta_y, 
                                  " center width ", center_width)
                                sum+=con_mat.arr[rc][cc] * img_mat.arr[delta_x][delta_y]
                                counter+=1
                        except:
                            print("out of range: ", str(delta_x), str(delta_y))
                print("")
                print("sum : ", sum)
                print("counter: ", counter)
                output.arr[r][c] = int(sum/counter)
        return output
