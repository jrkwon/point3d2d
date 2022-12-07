"""
History:
12/07/2022: Created. 
@author: jaerock
"""

import numpy as np

from point3d2d import CameraIntrinsic
from point3d2d import Point3D2D


def main():
    # camera 3
    rotation_vector = np.array([0.0249593, -1.5888666, -0.1002387])
    translation_vector = np.array([1.0249999, 0.8818195, 3.3404123])
    camera_intrinsic = CameraIntrinsic(f = 632.86136, cx = 328.65439, cy = 243.59555)
    
    # sample points
    points_world_list = [
        [1, 0, 2], 
        [0, 0, 0]
    ]
    points_world = np.array(points_world_list)
    
    point3d2d = Point3D2D(camera_intrinsic, 
                          rotation_vector, translation_vector, verbose=True)

    for point_world in points_world:
        (u, v) = point3d2d.project(point_world)
        print(f"point_world: {point_world} --> (u, v): {u}, {v}")
    

if __name__ == '__main__':
    main()