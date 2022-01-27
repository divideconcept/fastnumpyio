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

The saved bytes object is formatted like this:
```
endianness: 1 byte, value can be < > |
type: 1 byte, value can be b i f c
type size: 1 byte, value can be 1 2 4 8 16
number of dimensions: 1 byte, value can be 0-255
shape: 4 bytes per dimension
raw samples data
```
