import numpy as np

# with random data
# X = np.random.random((10, 3))

# with some numbers for testing
array1 = [[1, 1, 1], [3, 5, 8], [50, 10, 20]]
X = np.array(array1)


D = np.sqrt(((X[:, np.newaxis, :] - X) ** 2).sum(axis=-1))

# this generates a matrix of distances between each i, j point in X in a symmetrical matrix
print(D)