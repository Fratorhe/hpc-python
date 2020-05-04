import numpy as np

dataxy = np.loadtxt('xy-coordinates.dat')
print(dataxy)

dataxy_plus = dataxy+2.5

print(dataxy_plus)

args = {
	  'header': 'XY coordinates',
  	  'fmt': '%7.3f',
  	  'delimiter': ','
}

np.savetxt('output.dat', dataxy_plus, **args)