# Fastnumpyio
Fast Numpy I/O : Fast replacement for numpy.load and numpy.save

numpy.load and numpy.save is not optimal speed wise, specially if your arrays don't have complex internal structures.

fastnumpio provides significant speedup over numpy.load and numpy.save.
It's designed to save and load a bytes object (as opposed to a file-like object with numpy.save and numpy.load).

Running fastnumpyio.py (saving and loading 100k float32 array with shape 3,64,64) shows the following results:

Windows 11, Python 3.9.5, Numpy 1.22.0, Intel Core i7-9750H:
```
numpy.save: 0:00:01.809470
fast_numpy_save: 0:00:00.413202
numpy.load: 0:00:17.921214
fast_numpy_load: 0:00:00.002260
numpy.save+numpy.load == fast_numpy_save+fast_numpy_load: True
```

Ubuntu 20.04, Python 3.9.7, Numpy 1.21.4, Intel Core i7-9750H:
```
numpy.save: 0:00:01.887152
fast_numpy_save: 0:00:00.745052
numpy.load: 0:00:16.368871
fast_numpy_load: 0:00:00.381135
numpy.save+numpy.load == fast_numpy_save+fast_numpy_load: True
```

macOS 12.0.1, Python 3.9.5, Numpy 1.21.2, Apple M1:
```
numpy.save: 0:00:01.268598
fast_numpy_save: 0:00:00.449448
numpy.load: 0:00:11.303569
fast_numpy_load: 0:00:00.318216
numpy.save+numpy.load == fast_numpy_save+fast_numpy_load: True
```

It cannot save and load complex internal structures as-is, but it could probably be improved to handle special cases as well.

The saved bytes object is formatted like this:
```
endianness: 1 byte, value can be < > |
type: 1 byte, value can be b i f c
type size: 1 byte, value can be 1 2 4 8 16
number of dimensions: 1 byte, value can be 0-255
shape: 4 bytes per dimension
raw samples data
```
