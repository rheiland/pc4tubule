#!/usr/bin/env python

import sys
from vtk import *

xmax = 400
ymax = 400
zmax = 150

cyl = vtkCylinderSource()
cyl.CappingOff()
cyl.SetCenter(0.0, 0.0, 300)
cyl.SetRadius(xmax)
cyl.SetHeight(800)
cyl.SetResolution(50)

mapper = vtkPolyDataMapper()
mapper.SetInputConnection(cyl.GetOutputPort())

cyl_actor = vtkActor()
cyl_actor.SetMapper(mapper)
cyl_actor.GetProperty().SetColor(1.0, 0.0, 0.0)
cyl_actor.GetProperty().SetRepresentationToWireframe()
cyl_actor.GetProperty().SetAmbient(1.0)

# ---------
# points = vtkPoints()
# points.InsertNextPoint(-xmax, -ymax, -zmax)
# points.InsertNextPoint(xmax, -ymax, -zmax)
# points.InsertNextPoint(xmax, ymax, -zmax)
# points.InsertNextPoint(-xmax, ymax, -zmax)

# points.InsertNextPoint(-xmax, -ymax, zmax)
# points.InsertNextPoint(xmax, -ymax, zmax)
# points.InsertNextPoint(xmax, ymax, zmax)
# points.InsertNextPoint(-xmax, ymax, zmax)

# pd = vtkPolyData()
# pd.SetPoints(points)

box_outline = vtkOutlineSource()
bds = [-xmax,xmax, -ymax,ymax, -zmax,zmax]    # {xmin,xmax,ymin,ymax,zmin,zmax} via SetBounds()
box_outline.SetBounds(bds)

box_mapper = vtkPolyDataMapper()
box_mapper.SetInputConnection(box_outline.GetOutputPort())

box_actor = vtkActor()
box_actor.SetMapper(box_mapper)
box_actor.GetProperty().SetColor(1.0, 1.0, 1.0)
#---------

ren = vtkRenderer()
camera = ren.GetActiveCamera()
# camera.SetParallelProjection(True)
camera.ParallelProjectionOn()

#ren.SetBackground(1.0, 1.0, 1.0)
ren.AddActor(cyl_actor)
ren.AddActor(box_actor)

renWin = vtkRenderWindow()
renWin.SetPosition(100,100)
renWin.SetSize(1400,1200)

renWin.AddRenderer(ren)
iren = vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

iren.Initialize()
renWin.Render()
iren.Start()



