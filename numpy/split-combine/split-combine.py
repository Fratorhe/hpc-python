import numpy as np

rows = 8
columns = 8

data = np.array([[column +1 + (row + 1)/10  for row in range(rows)] for column in range(columns)])

##
data_split = np.split(data,2)

data_together = np.concatenate(data_split)
##
data_split = np.split(data,2, axis=1)

data_together = np.concatenate(data_split, axis=1)