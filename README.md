# Fastnumpyio
Fast Numpy I/O : Fast replacement for numpy.load and numpy.save

numpy.load and numpy.save is not optimal speed wise, specially if your arrays don't have complex internal structures.

fastnumpio provides a x4 speedup over numpy.load, and a x8000 speedup over numpy.save.
It's designed to save and load a bytes object (as opposed to a file-like object with numpy.save and numpy.load).

Running fastnumpyio.py shows the following result on Windows 11, Python 3.9.5, Numpy 1.22.0, and an	Intel Core i7-9750H:

```
numpy.save: 0:00:01.809470
fast_numpy_save: 0:00:00.413202
numpy.load: 0:00:17.921214
fast_numpy_load: 0:00:00.002260
numpy.save+numpy.load == fast_numpy_save+fast_numpy_load: True
```

It cannot save and load complex internal structures as-is, but it could probably be improved to handle special cases as well.
