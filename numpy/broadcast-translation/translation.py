import numpy as np
import matplotlib.pyplot as plt

points_circle = np.genfromtxt('points_circle.dat')

vect = np.array([3,5])

points_after = points_circle+vect

# print(points_after)


plt.plot(points_circle[:,0],points_circle[:,1], 'o', label='before')
plt.plot(points_after[:,0],points_after[:,1], 'o', label='after')
plt.show()