import sys
import numpy as np
from matplotlib.patches import Circle, Ellipse, Rectangle
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d



cyl_radius = float(sys.argv[1])
height_scale = float(sys.argv[2])

# cell_radius = 1.  # ~2 micron spacing
cell_radius = 8.4127  # PhysiCell_phenotype.cpp
cell_diam = cell_radius*2

lngth = 2*np.pi * cyl_radius  # circumference
# print('lngth=',lngth)
x_min = 0.0
x_max = lngth
y_min = 0.0
y_max = lngth * height_scale

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
for yval in np.arange(y_min,y_max, y_spacing):
    y_idx += 1
    t = 0
    for xval in np.arange(x_min,x_max, x_spacing):
        xval_offset = xval + (y_idx%2) * cell_radius
        # xv = xval_offset - big_radius

        # cells_x = np.append(cells_x, xval)
        # cells_y = np.append(cells_y, yval)
# lngth = 2*np.pi * cyl_radius  # circumference
        # cells_x = np.append(cells_x, xval * np.cos(t))
        # cells_z = np.append(cells_z, xval * np.sin(t))

        if y_idx%2:
            xv = cyl_radius * np.cos(t) 
            zv = cyl_radius * np.sin(t)
        else:
            xv = cyl_radius * np.cos(t+dt2) 
            zv = cyl_radius * np.sin(t+dt2)
        # xv = (cyl_radius + xval_offset) * np.cos(t) 
        cells_x = np.append(cells_x, xv)
        cells_z = np.append(cells_z, zv)
        cells_y = np.append(cells_y, yval)
        print(xv,', ',yval,', ',zv,', 0')
        t += dt
            # print(xv,',',yval,',0.0, 2, 101')  # x,y,z, cell type, [sub]cell ID
            # plt.plot(xval_offset,yval,'ro',markersize=30)

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

plt.show()
