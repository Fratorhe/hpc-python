import numpy as np

a = np.array([[12, 565, 78, 5.0 ],[654, 531, 54, 654],
	[456, 45678, 5, 45613],[456, 456123, 1, 3]])

a2row = a[1,:]
print(a2row)

a3column = a[:,3]
print(a3column)

a[0:2,0:2] = 0.21

print(a)

checkerboard = np.zeros([8,8])
checkerboard[0::2,0::2] =1
checkerboard[1::2,1::2] =1
print(checkerboard)
