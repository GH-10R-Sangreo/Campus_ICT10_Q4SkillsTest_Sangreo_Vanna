# numerical python and matt plotting library
from pyscript import display
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt
# removin font cache message
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close


f = np.array([1, 2, 3, 4, 5]) # 1d array
r = np.array([[1, 2,], [3, 4]]) # 2d array
a = np.array([[1, 2], [3,4]]) # 3d array

#array properties
display(r.shape, target='output')
display(r.ndim, target='output')
display(r.size, target='output')
display(r.dtype, target='output')

# mathematical operations in numpy
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

display(a + b, target='output')
display(a * b, target='output')
display(a ** b, target='output')

# magthematical functions
c = np.array([[1, 2], [3, 4]])

display(np.sum(c), target='output')
display(np.mean(c), target='output')
display(np.max(c), target='output')
display(np.min(c), target='output')

# creating graph using mathplotlib
days = np.array(['Mon', 'Tue', 'Wed', 'Thurs', 'Fri'])
sales = np.array([1000, 2500, 1200, 700, 3200])
sangreo_graph = plt.plot(days, sales) # creating graph
plt.show() # display graph

