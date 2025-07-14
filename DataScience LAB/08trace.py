import numpy as np
n = int(input("Enter size of square matrix (n x n): "))
print(f"Enter {n*n} elements (row-wise, space separated):")
elements = list(map(float, input().split()))
matrix = np.array(elements).reshape(n, n)
print("\nOriginal Matrix:")
print(matrix)
trace=np.trace(matrix)
print("Trace of the matrix is: ",trace)
