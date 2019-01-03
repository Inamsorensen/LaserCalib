#!/usr/bin/env python

import numpy as np
from mayavi import mlab

dphi, dtheta = np.pi / 250.0, np.pi / 250.0
[phi, theta] = np.mgrid[0 : np.pi + dphi * 1.5 : dphi, 0 : 2.0 * np.pi + dtheta * 1.5 : dtheta]
print(phi)
print(theta)
m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
r = np.sin(m0 * phi) ** m1 + np.cos(m2 * phi) ** m3 + np.sin(m4 * theta) ** m5 + np.cos(m6 * theta) ** m7
x = r * np.sin(phi) * np.cos(theta)
print(x)
y = r * np.cos(phi)
z = r * np.sin(phi) * np.sin(theta)

# View it.
s = mlab.mesh(x, y, z)
# mlab.show()

