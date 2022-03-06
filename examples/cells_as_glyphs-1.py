# https://kitware.github.io/vtk-examples/site/Python/Filtering/Glyph3D/
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2

from vtk import *
# from vtkmodules.vtkCommonColor import vtkNamedColors
# from vtkmodules.vtkCommonCore import vtkPoints, vtkFloatArray
# from vtkmodules.vtkCommonDataModel import vtkPolyData,vtkUnsignedCharArray
# from vtkmodules.vtkFiltersCore import vtkGlyph3D
# from vtkmodules.vtkFiltersSources import vtkSphereSource
# from vtkmodules.vtkRenderingCore import (
#     vtkActor,
#     vtkPolyDataMapper,
#     vtkRenderWindow,
#     vtkRenderWindowInteractor,
#     vtkRenderer
# )

from pyMCDS_cells import pyMCDS_cells
from vtk.util import numpy_support
import numpy as np
from random import randint


def main():
    mcds = pyMCDS_cells('output00000003.xml', '.')  # 23123 cells
    # mcds = pyMCDS_cells('output00000003.xml', '.')  
    print('time=', mcds.get_time())

    print(mcds.data['discrete_cells'].keys())

    ncells = len(mcds.data['discrete_cells']['ID'])
    print('ncells=', ncells)

    global xyz
    xyz = np.zeros((ncells, 3))
    xyz[:, 0] = mcds.data['discrete_cells']['position_x']
    xyz[:, 1] = mcds.data['discrete_cells']['position_y']
    xyz[:, 2] = mcds.data['discrete_cells']['position_z']
    #xyz = xyz[:1000]
    print("position_x = ",xyz[:,0])
    xmin = min(xyz[:,0])
    xmax = max(xyz[:,0])
    print("xmin = ",xmin)
    print("xmax = ",xmax)

    ymin = min(xyz[:,1])
    ymax = max(xyz[:,1])
    print("ymin = ",ymin)
    print("ymax = ",ymax)

    zmin = min(xyz[:,2])
    zmax = max(xyz[:,2])
    print("zmin = ",zmin)
    print("zmax = ",zmax)

    cell_type = mcds.data['discrete_cells']['cell_type']
    unique_cell_type = np.unique(cell_type)
    print("\nunique_cell_type = ",unique_cell_type )

    #------------
    colors = vtkNamedColors()

    points = vtkPoints()
    points.InsertNextPoint(0, 0, 0)
    points.InsertNextPoint(1, 1, 1)
    points.InsertNextPoint(2, 2, 2)
    cellID = vtkFloatArray()
    cellVolume = vtkFloatArray()
    for idx in range(ncells):
        x= mcds.data['discrete_cells']['position_x'][idx]
        y= mcds.data['discrete_cells']['position_y'][idx]
        z= mcds.data['discrete_cells']['position_z'][idx]
        id = mcds.data['discrete_cells']['cell_type'][idx]
        points.InsertNextPoint(x, y, z)
        # cellVolume.InsertNextValue(30.0)
        cellID.InsertNextValue(id)

    polydata = vtkPolyData()
    polydata.SetPoints(points)
    polydata.GetPointData().SetScalars(cellVolume)
    # polydata.GetPointData().SetScalars(cellID)

    colors = vtkUnsignedCharArray()
    colors.SetNumberOfComponents(3)
    colors.SetNumberOfTuples(polydata.GetNumberOfPoints())  # ncells

    for idx in range(ncells):
        colors.InsertTuple3(0, randint(0,255), randint(0,255), randint(0,255)) # reddish

    polydata.GetPointData().SetScalars(colors)

    sphereSource = vtkSphereSource()
    nres = 12
    sphereSource.SetPhiResolution(nres)
    sphereSource.SetThetaResolution(nres)
    sphereSource.SetRadius(0.1)

    glyph3D = vtkGlyph3D()
    glyph3D.SetSourceConnection(sphereSource.GetOutputPort())
    glyph3D.SetInputData(polydata)
    glyph3D.SetColorModeToColorByScalar()
    # glyph3D.SetScaleModeToDataScalingOff()
    # glyph3D.SetScaleModeToDataScalingOn()
    # glyph3D.ScalingOn()
    glyph3D.Update()

    # Visualize
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(glyph3D.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    # actor.GetProperty().SetColor(colors.GetColor3d('Salmon'))

    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetPosition(100,100)
    renderWindow.SetSize(800,800)
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    # renderer.SetBackground(colors.GetColor3d('SlateGray'))  # Background Slate Gray

    renderWindow.SetWindowName('PhysiCell model')
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()
