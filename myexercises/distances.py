# Example: calculate distances to a fixed point (origin) from a list of coordinates (points):

import numpy

points = numpy.random.random((100, 3))  # 100 coordinates in 3D
origin = numpy.array((1.0, 2.2, -2.2))  # fixed point

# calculate distances
distances = (points - origin)**2
distances = numpy.sqrt(numpy.sum(distances, axis=1))

# find the most distant point
i = numpy.argmax(distances)
print(points[i])