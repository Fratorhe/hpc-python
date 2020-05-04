import numpy

xy = numpy.loadtxt('data.dat')

print(xy)


args = {
  'header': 'XY coordinates',
  'fmt': '%7.3f',
  'delimiter': ','
}
numpy.savetxt('output.dat', xy, **args)