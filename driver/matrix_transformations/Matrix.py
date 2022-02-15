class Matrix:
    def __init__(self, arr, width, height):
        self.arr = arr if arr != None else [[0 for x in range(width)] for y in range(height)] 
        self.width = width
        self.height = height
    def mult_row_col(self, row, col, A, B):
        sum = 0
        for r in range(len(A)):
            sum += A[row][r] * B[r][col]
        return sum
    @staticmethod
    def mult(A, B):
        print("A width = ", A.width)
        print("B height = ", B.height)
        output = [[0 for x in range(A.width)] for y in range(B.height)] 
        for r in range(A.height):
            output.append([])
            for c in range(B.width):
                #for each row in A, multiply by all cols in B
                mult_result = A.mult_row_col(r, c, A.arr, B.arr)
                output[r][c] = mult_result
        return Matrix(output, len(output), len(output[0]))
    @staticmethod
    def display_matrix(A):
        arr = A.arr
        for r in range(len(arr)):
            for c in range(len(arr[r])):
                print(arr[r][c], end = " ")
            print("\n")
