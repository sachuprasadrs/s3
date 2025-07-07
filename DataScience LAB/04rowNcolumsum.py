import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
total_sum = np.sum(arr)
row_sum = np.sum(arr, axis=1)
col_sum = np.sum(arr, axis=0)
print("Original Array:\n", arr)
print("\nSum of all elements:", total_sum)
print("Sum of each row:", row_sum)
print("Sum of each column:", col_sum)
