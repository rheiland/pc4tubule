#!/usr/bin/env python

import sys
from vtk import *

cyl = vtkCylinderSource()
cyl.CappingOff()
cyl.SetCenter(0.0, 0.0, 0.0)
cyl.SetRadius(1.0)
cyl.SetHeight(8.0)
cyl.SetResolution(50)

mapper = vtkPolyDataMapper()
mapper.SetInputConnection(cyl.GetOutputPort())

actor = vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(1.0, 0.0, 0.0)

ren = vtkRenderer()
#ren.SetBackground(1.0, 1.0, 1.0)
ren.AddActor(actor)

renWin = vtkRenderWindow()
renWin.SetPosition(100,100)
renWin.SetSize(1400,1200)

renWin.AddRenderer(ren)
iren = vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

iren.Initialize()
renWin.Render()
iren.Start()



