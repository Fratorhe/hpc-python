import numpy as np

A = np.random.random([3,3])*20
A_sym = A + A.T

B = np.random.random([3,3])*20
B_sym = B + B.T
print(A)


C = A_sym.dot(B_sym)
print(C)

eig = np.linalg.eigvals(C)
print(eig)