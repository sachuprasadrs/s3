import numpy as np
n=int(input("Enter size of row (n): "))
m=int(input("Enter size of column (m): "))
print(f"Enter {n*m} elements (row-wise, space separated):")
elements = list(map(float, input().split()))
matrix = np.array(elements).reshape(n, m)
print("\nOriginal Matrix:")
print(matrix)
transpose = matrix.T
print("\nTranspose of the Matrix:")
print(transpose)
