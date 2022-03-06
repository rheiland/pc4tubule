#!/usr/bin/env python
# -*- coding: utf-8 -*-

# adapted from https://gist.github.com/somada141/acefac8a6360cba21f3a
from vtk import *

# Let's create a surface with 3 points unconnected.
points = vtkPoints()
points.InsertNextPoint(1, 0, 0)
points.InsertNextPoint(0, 0, 0)
points.InsertNextPoint(0, 1, 0)

polydata = vtkPolyData()
polydata.SetPoints(points)

colors = vtkUnsignedCharArray()
colors.SetNumberOfComponents(3)
colors.SetNumberOfTuples(polydata.GetNumberOfPoints())

colors.InsertTuple3(0, 147, 25, 98) # reddish
colors.InsertTuple3(1, 32, 84, 247) # bluish
colors.InsertTuple3(2, 198, 214, 36) # yellowish

polydata.GetPointData().SetScalars(colors)

# Now, let's control normal on each point composing or 'fake' surface
# We should say, let's give a direction to each point, a normal in strange for a point.
pointNormalsArray = vtkDoubleArray()
pointNormalsArray.SetNumberOfComponents(3)
pointNormalsArray.SetNumberOfTuples(polydata.GetNumberOfPoints())

pN1 = [1.0, 0.0, 0.0]
pN2 = [0.0, 1.0, 0.0]
pN3 = [0.0, 0.0, 1.0]

pointNormalsArray.SetTuple(0, pN1)
pointNormalsArray.SetTuple(1, pN2)
pointNormalsArray.SetTuple(2, pN3)

polydata.GetPointData().SetNormals(pointNormalsArray)
# polydata.GetPointData().SetColorModeToColorByScalar(pointNormalsArray)

#sources = vtkConeSource()
sources = vtkSphereSource()
sources.Update()

glyph = vtkGlyph3D()
# try:
    # glyph.SetInput(polydata)
# except AttributeError:
glyph.SetInputData(polydata)

glyph.SetSourceConnection(sources.GetOutputPort())
glyph.SetColorModeToColorByScalar()
# glyph.SetVectorModeToUseNormal()  # only relevant if using Cone sources
# glyph.ScalingOn()   # centers all 3 around 0,0,0
glyph.ScalingOff()
glyph.Update()

mapper = vtkPolyDataMapper()
mapper.SetInputConnection(glyph.GetOutputPort())

actor = vtkActor()
actor.SetMapper(mapper)

ren = vtkRenderer()
ren.SetBackground(0.2, 0.5, 0.3)
ren.AddActor(actor)

renwin = vtkRenderWindow()
renwin.SetSize(800,800)
renwin.AddRenderer(ren)
iren = vtkRenderWindowInteractor()
iren.SetInteractorStyle(vtkInteractorStyleTrackballCamera())
iren.SetRenderWindow(renwin)

renwin.Render()
iren.Initialize()
renwin.Render()
iren.Start()
