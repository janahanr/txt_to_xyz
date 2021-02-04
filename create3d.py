import open3d
import math
import numpy as np

def modeling(xyz):

    pcd = open3d.io.read_point_cloud(xyz, format = 'xyz')

    print(pcd)

    print(np.asarray(pcd.points))

    po=0

    lines=[]

    for x in range(511):
        for y in range(20):
            if((y+1)%20==0):
                lines.append([po+y, po])
            else:
                lines.append([po+y, po + y +1])
        po += 20;

    po=0
    do=20

    for x in range(512):
        for y in range(20):
            lines.append([y+po, y+po+do])
        po += 20;

    line_set = open3d.geometry.LineSet(points=open3d.utility.Vector3dVector(np.asarray(pcd.points)), lines = open3d.utility.Vector2iVector(lines))

    open3d.visualization.draw_geometries([line_set])