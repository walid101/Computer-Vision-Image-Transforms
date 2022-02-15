from convolution import Convolution as conv
from matrix_transformations.Matrix import Matrix 
arr = [[1,2,3],
       [2,5,2],
       [6,7,2]]
A = Matrix(arr, len(arr), len(arr[0]))

convol = [[1,2,3],
          [2,3,4],
          [4,5,6]]

B = Matrix(convol, len(convol), len(convol[0]))
result = conv.convolve(A,B)
Matrix.display_matrix(result)
