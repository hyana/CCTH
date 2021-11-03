def zeroMatrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                setNone(matrix, row, col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == None:
                matrix[row][col] = 0
    return matrix

# mark None instead of 0 so that replaced 0 is not counted as input 0
def setNone(matrix, row, col):
    for i in range(0,len(matrix[row])):
        if matrix[row][i] != 0:
            matrix[row][i] = None
    for j in range(0, len(matrix)): 
        if matrix[j][col] != 0:
            matrix[j][col] = None
    return matrix

def main():
    zeroMatrix([[1,1,1],[1,0,1],[1,1,1],[1,1,0]])
main()