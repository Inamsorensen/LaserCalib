import numpy as np


def normalize(vector):
    try:
        norm = np.linalg.norm(vector)
        if norm > 10**-7:
            vector = vector / norm
    except ValueError:
        print('Unable to perform numpy.linalg.norm on input')
    return vector


class ImageData():
    def __init__(self, worldPoints_actual, planeRotation, planeTranslation):
        self.actual_world = worldPoints_actual
        self.planeRotation = planeRotation
        self.planeTranslation = planeTranslation


class Calibration():
    def __init__(
            self,
            calibData,
            voltToAngle=np.array([2.0, 2.0]),
            angle_0=np.array([-45.0, 45.0]),
            dist_m1_m2=0.01, angle_m1=0.0,
            rayOrigin=np.array([1.0, 0.0, 0.0]),
            rayDir_0=np.array([-1.0, 0.0, 0.0])):

        # Calibration setup
        self.calibData = calibData

        # Intrinsic parameters
        self.voltToAngle_X = voltToAngle[0] * (np.pi / 180.0)
        self.voltToAngle_Y = voltToAngle[1] * (np.pi / 180.0)
        self.alpha_0 = angle_0[0] * (np.pi / 180.0)
        self.beta_0 = angle_0[1] * (np.pi / 180.0)
        self.r = dist_m1_m2
        self.gamma = angle_m1
        self.rayOrigin = rayOrigin
        self.rayDir_0 = normalize(rayDir_0)

        # Extrinsic parameters
        self.worldToLaser_rot = np.identity(3)
        self.worldToLaser_trans = np.array([0.0, 0.0, 1.0])

    def setVoltGrid(
            self,
            minVolt_X, maxVolt_X, steps_X,
            minVolt_Y, maxVolt_Y, steps_Y):

        X, Y = np.mgrid[
                minVolt_X:maxVolt_X:1j * steps_X,
                minVolt_Y:maxVolt_Y:1j * steps_Y]

        self.voltGrid = np.empty([steps_X * steps_Y, 2])
        self.voltGrid[:, 0] = X.ravel()
        self.voltGrid[:, 1] = Y.ravel()

    def voltToWorld(self, volts, planeRotation, planeTranslation):

        alpha = self.voltToAngle_X * volts[0] + self.alpha_0
        beta = self.voltToAngle_Y * volts[1] + self.beta_0

        print('alpha', alpha)
        print('beta', beta)

        norm_X = np.array([
            -np.sin(alpha),
            np.cos(alpha) * np.cos(self.gamma),
            np.cos(alpha) * np.sin(self.gamma)])

        norm_X = normalize(norm_X)

        print('norm_X', norm_X)
        print('cos(alpha)', np.cos(alpha))

        norm_Y = np.array([
            0.0,
            np.cos(beta),
            np.sin(beta)])
        norm_Y = normalize(norm_Y)

        print('norm_Y', norm_Y)

        norm_plane = np.dot(planeRotation, np.array([0.0, 0.0, 1.0]))
        norm_plane = normalize(norm_plane)

        print('norm_plane', norm_plane)

        origin_laser = np.array([0.0, 0.0, 0.0])
        point_Y_0 = np.array([0.0, self.r, 0.0])
        point_plane_0 = planeTranslation

        print('rayOrigin', self.rayOrigin)
        print('rayDir_0', self.rayDir_0)

        dist_0 = np.dot((origin_laser - self.rayOrigin), norm_X) / np.dot(self.rayDir_0, norm_X)
        point_X = self.rayOrigin + dist_0 * self.rayDir_0
        rayDir_1 = self.rayDir_0 - 2.0 * np.dot(norm_X, self.rayDir_0) * norm_X
        rayDir_1 = normalize(rayDir_1)

        print('dist_0', dist_0)
        print('point_X', point_X)
        print('rayDir_1', rayDir_1)

        dist_1 = np.dot((point_Y_0 - point_X), norm_Y) / np.dot(rayDir_1, norm_Y)
        point_Y = point_X + dist_1 * rayDir_1
        rayDir_2 = rayDir_1 -2.0 * np.dot(norm_Y, rayDir_1) * norm_Y
        rayDir_2 = normalize(rayDir_2)

        print('dist_1', dist_1)
        print('point_Y', point_Y)
        print('rayDir_2', rayDir_2)

        dist_2 = np.dot((point_plane_0 - point_Y), norm_plane) / np.dot(rayDir_2, norm_plane)
        point_plane = point_Y + dist_2 * rayDir_2

        print('dist_2', dist_2)
        print('point_plane', point_plane)

        return point_plane

    def estimateWorldPoints(self):
        for imageData in self.calibData:
            imageData.estimated_world = np.array([
                self.voltToWorld(
                    voltCoord,
                    imageData.planeRotation,
                    imageData.planeTranslation)
                for voltCoord in self.voltGrid])

            print('estimated', self.estimated_world)
