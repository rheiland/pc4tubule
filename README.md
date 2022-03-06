# pc4tubule

PhysiCell Studio (3D) for testing cell mechanics inside a tubule.

Compile, copy the executable to the root directory, run the GUI:
```
cd pc4tubule/src
make
cp myproj ..
cd ..
python bin/studio.py
```

In the GUI:
* in the Run tab, click `Run Simulation`. Note: the simulation is run *from* the `tmpdir` directory and that's where all output files will be written.
* in the Plot tab, click `Play`.
* edit params if you want then repeat: Run, Play.
