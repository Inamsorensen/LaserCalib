#!/usr/bin/env python

import numpy as np
from mayavi import mlab

# Camera
cam = mlab.points3d(0.0, 0.0, 0.0)

# Object parameters
# Mirror
pos_m = np.array([0.0, 0.0, 5.0])
size_m = np.array([5.0, 5.0, 0.1])
rot_m = np.array([0.0, 45.0, 0.0])
colour_m = np.array([1.0, 0.0, 0.0])
opacity_m = 1.0

# Glass
pos_g = np.array([-10.0, 0.0, 2.5])
size_g = np.array([14.0, 7.0, 1.0])
rot_g = np.array([0.0, 90.0, 0.0])
colour_g = np.array([0.0, 1.0, 0.0])
opacity_g = 0.5

# Plate
pos_p = np.array([-20.0, 0.0, 2.5])
size_p = np.array([20.0, 20.0, 0.1])
rot_p = np.array([0.0, 90.0, 0.0])
colour_p = np.array([0.0, 0.0, 1.0])
opacity_p = 1.0

pos = [pos_m, pos_g, pos_p]
size = [size_m, size_g, size_p]
rot = [rot_m, rot_g, rot_p]
colour = [colour_m, colour_g, colour_p]
opacity = [opacity_m, opacity_g, opacity_p]

# Object creation
cube = np.array([
    [-0.5, -0.5, -0.5, 1.0],
    [0.5, -0.5, -0.5, 1.0],
    [-0.5, 0.5, -0.5, 1.0],
    [0.5, 0.5, -0.5, 1.0],
    [-0.5, -0.5, 0.5, 1.0],
    [0.5, -0.5, 0.5, 1.0],
    [-0.5, 0.5, 0.5, 1.0],
    [0.5, 0.5, 0.5, 1.0]])

triangles = [
        (0, 1, 2),
        (1, 2, 3),
        (0, 1, 4),
        (1, 4, 5),
        (0, 2, 4),
        (2, 4, 6),
        (1, 3, 5),
        (3, 5, 7),
        (2, 3, 6),
        (3, 6, 7),
        (4, 5, 6),
        (5, 6, 7)
        ]


for i in range(0, len(pos)):
    size_o = np.append(size[i], [1.0])
    scale = np.diag(size_o)

    rotrad_o = (rot[i] * np.pi) / 180.0
    cos, sin = np.cos(rotrad_o), np.sin(rotrad_o)
    rotx = np.matrix([
            [1.0, 0.0, 0.0, 0.0],
            [0.0, cos[0], -sin[0], 0.0],
            [0.0, sin[0], cos[0], 0.0],
            [0.0, 0.0, 0.0, 1.0]
            ])

    roty = np.matrix([
            [cos[1], 0.0, sin[1], 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [-sin[1], 0.0, cos[1], 0.0],
            [0.0, 0.0, 0.0, 1.0]
            ])

    rotz = np.matrix([
            [cos[2], -sin[2], 0.0, 0.0],
            [sin[2], cos[2], 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
            ])

    rotmat = np.dot(rotx, (np.dot(roty, rotz)))

    translate = np.identity(4)
    pos_o = np.append(pos[i], [1.0])
    translate[:, 3] = pos_o

    transform = np.dot(translate, np.dot(rotmat, scale))

    object_vertices = np.dot(transform, cube.transpose()).transpose()

    x = object_vertices[:, 0].tolist()
    y = object_vertices[:, 1].tolist()
    z = object_vertices[:, 2].tolist()

    object = mlab.triangular_mesh(x, y, z,
            triangles,
            color=tuple(colour[i].reshape(1, -1)[0]),
            opacity=opacity[i])

mlab.show()
