#!/usr/bin/env python

import numpy as np
from mayavi import mlab

def test_triangular_mesh():
    """An example of a cone, ie a non-regular mesh defined by its
        triangles.
    """
    n = 8
    t = np.linspace(-np.pi, np.pi, n)
    z = np.exp(1j * t)
    print(z)
    x = z.real.copy()
    y = z.imag.copy()
    z = np.zeros_like(x)

    triangles = [(0, i, i + 1) for i in range(1, n)]
    print(triangles)
    x = np.r_[0, x]
    print(x)
    y = np.r_[0, y]
    z = np.r_[1, z]
    t = np.r_[0, t]

    return mlab.triangular_mesh(x, y, z, triangles, scalars=t)

if __name__ == '__main__':
    triangle = test_triangular_mesh()
    # mlab.show()
