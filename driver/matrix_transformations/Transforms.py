from .Matrix import Matrix
class Transforms:
    def __init__(self):
        self = self
    def translate(A, x, y): #if A describes 2D vectors, make sure to have it as a 3x3 matrix where bottom road is 1's
        #A is the matrix we need to transform
        #print("Origin Matrix A: ")
        #Matrix.display_matrix(A)
        height = A.height
        T = Matrix(None, height, height)
        for i in range(len(T.arr[0])): #identity Matrix i 
            T.arr[i][i] = 1
        T.arr[0][len(T.arr[0])-1] = x
        T.arr[1][len(T.arr[0])-1] = y 
        #print("Translate Matrix: ")
        #Matrix.display_matrix(T)
        return Matrix.mult(T, A)
    def rotate(A, theta):
        #TODO
        return 0