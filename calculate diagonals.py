# Sum of diagonals. First digit represents the number of rows and columns
matrix_numbers = [[11, 2, 4],
                  [4, 5, 6],
                  [10, 8, -12]]


def diagonalDifference(arr):
    diag1, diag2 = 0, 0
    counter = 0
    counter2 = len(arr) - 1
    for i in arr:
        diag1 = diag1 + i[counter]
        counter += 1
    for i in arr:
        diag2 = diag2 + i[counter2]
        counter2 -= 1

    return abs(diag1 - diag2)
        

            

print (diagonalDifference(matrix_numbers))
