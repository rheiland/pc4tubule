# python cells_cylinder.py 100 8 >cyl1.csv
import sys
import numpy as np
from matplotlib.patches import Circle, Ellipse, Rectangle
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

cyl_radius = float(sys.argv[1])
cyl_radius = float(sys.argv[1])
# height_scale = float(sys.argv[2])

# cell_radius = 1.  # ~2 micron spacing
cell_radius = 8.4127  # PhysiCell_phenotype.cpp
cell_diam = cell_radius*2

lngth = 2*np.pi * cyl_radius  # circumference
# print('lngth=',lngth)
x_min = 0.0
x_max = lngth
y_min = 0.0
# y_max = lngth * height_scale

#yc = -1.0
y_idx = -1
# hex packing constants
x_spacing = cell_radius*2
y_spacing = cell_radius*np.sqrt(3)

cells_x = np.array([])
cells_y = np.array([])
cells_z = np.array([])

# rectangle image of lenght: L and height: H
# cylinder of radius : R and height H'
# A (x,z) be a point in the picture
# A' (x',y',z') = ( R*cos(x*(2Pi/L)) , R*sin(x*(2Pi/L)) , z*(H'/H))
# x = R*cos(t), t=[0,2pi]
# y = R*sin(t)

y_idx = 0
num_xpts = (x_max - x_min) / x_spacing
dt = 2*np.pi / (num_xpts-1)
dt2 = dt/2.0

# print("dt2 (1) = ",dt2)
zval = 0.0
cyl_radius0 = cyl_radius
xctr = 0.0
yctr = 0.0
cell_type = 0
cell_ID = 0
for iblob in range(0, 3):
    for zval in np.arange(0.0, 12*cell_radius, 2.9*cell_radius ):
        cyl_radius = cyl_radius0
        dt = np.arcsin(cell_radius / cyl_radius)
        dt2 = dt*3.5
        for tdel in np.arange(0.0, 2*np.pi, dt2):
            xval = xctr + cyl_radius * np.cos(tdel)
            yval = yctr + cyl_radius * np.sin(tdel)
            # cells_x = np.append(cells_x, xval)
            # cells_y = np.append(cells_y, yval)
            # cells_z = np.append(cells_z, 0.0)
            print(xval,', ',yval,', ',zval,', ',cell_type,',',cell_ID)

        cyl_radius -= cell_radius*3.0
        dt2_old = dt2
        dt2 = dt*6.0
        # print("dt2 (2) = ",dt2)
        #for tdel in np.arange(dt2_old, 2*np.pi, dt2):
        for tdel in np.arange(0, 2*np.pi, dt2):
            xval = xctr + cyl_radius * np.cos(tdel)
            yval = yctr + cyl_radius * np.sin(tdel)
            print(xval,', ',yval,', ',zval,', ',cell_type,',',cell_ID)
                    # print(xv,',',yval,',0.0, 2, 101')  # x,y,z, cell type, [sub]cell ID
                    # plt.plot(xval_offset,yval,'ro',markersize=30)

        print(xctr,',',yctr,',',zval,', ', cell_type,',',cell_ID)
    # cell_type += 1
    cell_ID += 1
    if iblob == 0:
        xctr += cyl_radius*4.0
    elif iblob == 1:
        xctr -= cyl_radius*2.0
        yctr += cyl_radius*3.6
# zdata = 15 * np.random.random(100)
# xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
# ydata = np.cos(zdata) + 0.1 * np.random.randn(100)


# circles(cells_x,cells_y, s=cell_radius, c='b', ec='black', linewidth=0.1)


fig = plt.figure()
ax = plt.axes(projection='3d')
# set_axes_equal(ax)
# ax.set_aspect('equal')

#ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
ax.scatter3D(cells_x, cells_y, cells_z)

# plt.show()
