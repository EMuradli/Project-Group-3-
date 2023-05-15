from fractions import Fraction as frac
from math import gcd

# Matrix input
R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))
# Initialize matrix
matrix = []
print("Enter the entries row-wise:")

t = []

# For user input
for i in range(R):      # Loop for rows
    a = []
    for j in range(C):      # Loop for columns
        a.append(int(input()))
    matrix.append(a)

b = list(map(int, input("Enter your vector, separated by spaces: ").split()))

# Printing matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()

A = matrix


def gaussian_elimination(A, b):
    m = len(A)
    n = len(A[0])
    # Augment matrix A with vector b
    Ab = [A[i] + [b[i]] for i in range(m)]
    # Elimination phase
    for i in range(min(m, n)):
        # Find row with largest pivot
        max_row = i
        for j in range(i + 1, m):
            if abs(Ab[j][i]) > abs(Ab[max_row][i]):
                max_row = j
        # Swap current row with row containing largest pivot
        Ab[i], Ab[max_row] = Ab[max_row], Ab[i]
        # Eliminate entries below pivot
        for j in range(i + 1, m):
            factor = Ab[j][i] / Ab[i][i]
            for k in range(i + 1, n):
                Ab[j][k] = Ab[j][k] - factor * Ab[i][k]
            Ab[j][i] = 0


    # Back substitution phase
    for k in range(min(m, n) - 1, 0, -1):
        if Ab[k][k] == 0:
            continue
        for i in range(k - 1, -1, -1):
            factor = Ab[i][k] / Ab[k][k]
            for j in range(i, n):
                Ab[i][j] = Ab[i][j] - factor * Ab[k][j]
    for i in range(min(m, n)):
        if Ab[i][i] == 0:
            continue
        for j in range(n - 1, i - 1, -1):
            Ab[i][j] = Ab[i][j] / Ab[i][i]


    matrixArray = Ab
    print(Ab)
    for i, row in enumerate(matrixArray):
        if i == len(matrixArray) - 1 and matrixArray[i][-1] == 0:
            continue
        elif matrixArray[i][i] == 0:
            continue
        else:
            print(matrixArray[i][-1])
gaussian_elimination(A, b)
    # Turning decimals into fractions if needed
#     sol = {}
#     for k in range(len(x)):
#         xStr = str(x[k])
#         xStrFrac = frac(xStr).limit_denominator()
#         sol[f"x{k + 1}"] = str(xStrFrac)
#
#     return sol
#
# sol = gaussian_elimination(A, b)
#
# print(sol)
