"""
History:
12/07/2022: Created. 
@author: jaerock
"""

import numpy as np
import cv2

class CameraIntrinsic:
    def __init__(self, f, cx, cy):
        self.f = f
        self.cx = cx
        self.cy = cy


class Point3D2D:
    def __init__(self, camera_intrinsic, rotation_vector, translation_vector, verbose=False):
        self.camera_intrinsic = camera_intrinsic
        self.rotation_matrix, _ = cv2.Rodrigues(rotation_vector)

        self.transformation_matrix = np.append(self.rotation_matrix, 
                                            translation_vector.reshape(3, 1), 
                                            axis=1)

        if verbose:
            print(f"rotation: \n{self.rotation_matrix}")
            print(f"transformation_matrix: \n{self.transformation_matrix}")


    def project(self, point_world):
        point_world_ = np.hstack((point_world, 1))
        point_camera = np.matmul(self.transformation_matrix, point_world_.T)
        u = self.camera_intrinsic.f*point_camera[0]/point_camera[2] + self.camera_intrinsic.cx
        v = self.camera_intrinsic.f*point_camera[1]/point_camera[2] + self.camera_intrinsic.cy

        return (u, v)
