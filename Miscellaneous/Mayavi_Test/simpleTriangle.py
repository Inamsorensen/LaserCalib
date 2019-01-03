#!/usr/bin/env python

import numpy as np
from mayavi import mlab

orig = mlab.points3d(0.0, 0.0, 0.0)

x = np.array([0.0, 1.0, 0.0, 1.0])
y = np.array([0.0, 0.0, 1.0, 1.0])
z = np.array([1.0, 1.0, 1.0, 1.0])
triangles = [(0, 1, 2), (1, 2, 3)]
print(x)
print(y)
print(z)
print(triangles)

trian = mlab.triangular_mesh(x, y, z, triangles)
mlab.show()
