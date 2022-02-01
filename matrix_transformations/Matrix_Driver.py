from Matrix import Matrix
arr = [
    [1,3],
    [2,3]]

arr2 = [[1,1],
        [0,1]]
mat_ex = Matrix(arr, len(arr), len(arr[0]))
mat_ex2 = Matrix(arr2, len(arr2), len(arr2[0]))
print("Display Matrix 1: ")
Matrix.display_matrix(mat_ex)

print("Display Matrix 2: ")
Matrix.display_matrix(mat_ex2)

mult_mat = Matrix.mult(mat_ex2, mat_ex)
print("Display Mult Matrix: ")
Matrix.display_matrix(mult_mat)