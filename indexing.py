import numpy as np

# Rank 2 array of shape (3, 4)

an_array = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]])
print(an_array)

a_slice = an_array[:2, 1:3]
print(a_slice)
print("Before:", an_array[0, 1])
a_slice[0, 0] = 1000
print("After:", an_array[0, 1])

row_rank1 = an_array[1, :]
print(row_rank1, row_rank1.shape)
column_rank1 = an_array[:, 0]
print(column_rank1, column_rank1.shape)
columns_rank2 = an_array[:, 1:2]
print(columns_rank2)

col_indices = np.array([0, 1, 2, 0])
print("\nCol indices picked:", col_indices)

row_indices = np.arange(4)
print("\nRow indices picked:", row_indices)

for row, col in zip(row_indices, col_indices):
    print(row, ",", col)