# pc4learning3D

PhysiCell Studio for testing cell a 3D model (the 3D cancer immune sample model bundled with PhysiCell). Note that on the "Config Basics" tab, there is a "3D model" checkbox that is checked, but disabled. This means that this Studio GUI will *only* generate a 3D model in the .xml.

Compile, copy the executable to the root directory, run the GUI:
```
cd pc4learning3D/src
make
cp cancer_immune_3D ..
cd ..
python bin/studio.py
```

In the GUI:
* in the Run tab, click `Run Simulation`. Note: the simulation is run *from* the `tmpdir` directory and that's where all output files will be written.
* in the Plot tab, click `Play`.
* edit params if you want then repeat: Run, Play.
