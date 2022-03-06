# https://kitware.github.io/vtk-examples/site/Python/Filtering/Glyph3D/
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints, vtkFloatArray
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersCore import vtkGlyph3D
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
# from pyMCDS_cells import pyMCDS_cells
# from vtk.util import numpy_support
# import numpy as np


def main():
    colors = vtkNamedColors()

    points = vtkPoints()
    points.InsertNextPoint(-1, 0, 0)
    points.InsertNextPoint(0, 0, 0)
    points.InsertNextPoint(1, 0, 0)

    cell_type = vtkFloatArray()
    cell_type.InsertNextValue(0)
    cell_type.InsertNextValue(1)
    cell_type.InsertNextValue(2)

    cell_radius = vtkFloatArray()
    cell_radius.InsertNextValue(0.5)
    cell_radius.InsertNextValue(1.0)
    cell_radius.InsertNextValue(1.5)

    polydata = vtkPolyData()
    polydata.SetPoints(points)
    polydata.GetPointData().SetScalars(cell_radius)
    # polydata.GetPointData().SetScalars(cellID)

    ss = vtkSphereSource()
    print("sphere source radius=",ss.GetRadius())
    # ss.SetRadius(0.25)
    nres = 12
    ss.SetPhiResolution(nres)
    ss.SetThetaResolution(nres)

    glyph = vtkGlyph3D()
    glyph.SetSourceConnection(ss.GetOutputPort())
    # glyph.SetInputConnection(polydata.GetOutputPort())
    glyph.SetInputData(polydata)
    # glyph.SetColorModeToColorByScalar()
    # glyph.SetScaleModeToDataScalingOff()
    # glyph.SetScaleModeToDataScalingOn()

    glyph.ScalingOn()
    glyph.SetScaleModeToScaleByScalar()
    # glyph.SetVectorModeToUseVector()
    # glyph.OrientOn()
    # glyph.SetScaleFactor(1)  # Overall scaling factor
    # glyph.SetRange(0, 1.5)  # Default is (0,1)

    # glyph.SetInputArrayToProcess(0, 0, 0, 0, 'cell_type')  # scalars
    # glyph.SetInputArrayToProcess(1, 0, 0, 0, 'cell_size')  # vectors

    glyph.Update() # update the scalar range to set the color map range

    # Tell glyph which attribute arrays to use for what
    # glyph.SetInputArrayToProcess(0, 0, 0, 0, 'Elevation')  # scalars
    # glyph.SetInputArrayToProcess(1, 0, 0, 0, 'RTDataGradient')  # vectors
    # # glyph.SetInputArrayToProcess(2,0,0,0,'nothing')       # normals
    # glyph.SetInputArrayToProcess(3, 0, 0, 0, 'RTData')  # colors

    # Visualize
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(glyph.GetOutputPort())
    coloring_by = 'cell_type'
    coloring_by = 'cell_size'
    # mapper.SetScalarModeToUsePointFieldData()
    # mapper.SetColorModeToMapScalars()
    mapper.ScalarVisibilityOn()

    # GetRange() call doesn't work because attributes weren't copied to glyphs
    # as they should have been...
    # mapper.SetScalarRange(glyph.GetOutputDataObject(0).GetPointData().GetArray(coloring_by).GetRange())

    # mapper.SelectColorArray(coloring_by)

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
    renderer.SetBackground(colors.GetColor3d('SlateGray'))  # Background Slate Gray

    renderWindow.SetWindowName('PhysiCell model')
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()
