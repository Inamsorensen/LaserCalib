#!/usr/bin/env python

import numpy as np

from calibration import calibrate

if __name__ == '__main__':

    voltRange_X = np.linspace(-1.0, 1.0, num=3, endpoint=True)
    voltRange_Y = np.linspace(-1.0, 1.0, num=3, endpoint=True)

    worldPos = np.array([[1.0, 2.0, 3.0], [0.0, 2.0, 3.0], [1.0, 1.0, 2.0]])
    planeRotation = np.identity(3)
    planeTranslation = np.array([0.0, 0.0, 1.0])
    img1 = calibrate.ImageData(worldPos, planeRotation, planeTranslation)
    img2 = calibrate.ImageData(worldPos, planeRotation, planeTranslation)

    calibData = np.array([img1])

    calib = calibrate.Calibration(calibData)

    calib.setVoltGrid(-1.0, 1.0, 3, -1.0, 1.0, 3)
    # calib.estimateWorldPoints()
    volt = np.array([0.0, 0.0])
    print('volt', volt)
    print('planeRot', img1.planeRotation)
    print('planeTrans', img1.planeTranslation)
    calib.voltToWorld(
            volt,
            img1.planeRotation,
            img1.planeTranslation)
