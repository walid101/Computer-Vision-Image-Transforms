class Matrix:
    def __init__(self, arr, width, height):
        self.arr = arr if arr else []
        self.width = width
        self.height = height
    def mult_row_col(self, row, col, A, B):
        sum = 0
        if(len(A) != len(B[0])):
            print("# rows of A must equal # cols of B")
            print("Row is %d and col is %d", len(A), len(B[0]))
            return -1
        else:
            for r in range(len(A)):
                sum += A[row][r] * B[r][col]
        return sum
    @staticmethod
    def mult(A, B):
        output = [[0 for x in range(A.height)] for y in range(B.width)] 
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
