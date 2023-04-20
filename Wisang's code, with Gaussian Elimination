
# A basic code for matrix input from user

R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))
# Initialize matrix
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):		 # A for loop for row entries
	a = []
	for j in range(C):	 # A for loop for column entries
		a.append(int(input()))
	matrix.append(a)

b = list(map(int, input("Enter your vector, separated by spaces: ").split()))

# For printing the matrix
for i in range(R):
	for j in range(C):
		print(matrix[i][j], end = " ")
	print()

A = matrix

def gaussian_elimination(A, b):
    n = len(A)

    # Augment the matrix A with the vector b
    Ab = [A[i] + [b[i]] for i in range(n)]

    # Elimination phase
    for i in range(n):
        # Find the row with the largest pivot
        max_row = i
        for j in range(i + 1, n):
            if abs(Ab[j][i]) > abs(Ab[max_row][i]):
                max_row = j
        # Swap the current row with the row with the largest pivot
        Ab[i], Ab[max_row] = Ab[max_row], Ab[i]

        # Eliminate the entries below the pivot
        for j in range(i + 1, n):
            factor = Ab[j][i] / Ab[i][i]
            for k in range(i + 1, n + 1):
                Ab[j][k] -= factor * Ab[i][k]
            Ab[j][i] = 0

    # Back substitution phase
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i][n]
        for j in range(i + 1, n):
            x[i] -= Ab[i][j] * x[j]
        x[i] /= Ab[i][i]

    return x

sol = gaussian_elimination(A, b)

print(sol)  # Output: [1.0, 2.0, 3.0]
