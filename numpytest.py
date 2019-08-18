import numpy as np 

# ! Rank 1 array
an_array = np.array([0, 3, 33, 333])
print("Rank 1")
print(type(an_array))
print(an_array.shape)
an_array[0] = 888
print(an_array)

# ? Rank 2 array
another = np.array([[11, 12, 13], [21, 22, 23]])
print("Rank 2")
print(another)
print("Shape", another.shape)
print("Accessing elements:", another[0, 0], another[0, 1], another[1, 1])

# create matrix with zeros, ones
zeros = np.zeros((2, 2))
print(zeros)
ones = np.ones((3, 5))
print(ones)
full = np.full((7, 12), 3)
print(full)
eye = np.eye(10, 10)
print(eye)
print(eye.shape)
random = np.random.random((2, 5))
print(random)