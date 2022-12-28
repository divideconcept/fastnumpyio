# Fastnumpyio
Fast Numpy I/O : Fast replacements for numpy.load and numpy.save

numpy.load and numpy.save is not optimal speed wise, specially if your arrays don't have complex internal structures.

fastnumpyio.load/fastnumpyio.save can be used as a replacement to numpy.load/numpy.save with a significant speedup.

fastnumpyio.pack/fastnumpyio.unpack (saving/loading bytes objects) is even faster if you don't care about the npy format and path/file-like objects

Running fastnumpyio.py (saving and loading 100k float32 array with shape 3x64x64) shows the following results:

Windows 11, Python 3.9.12 x64, Numpy 1.24.0, Intel Core i7-12700K:
```
numpy.save: 0:00:00.786250
fastnumpyio.save: 0:00:00.329080
fastnumpyio.pack: 0:00:00.262129
numpy.load: 0:00:09.689329
fastnumpyio.load: 0:00:00.341074
fastnumpyio.unpack: 0:00:00.208267
numpy.save+numpy.load == fastnumpyio.save+fastnumpyio.load: True
numpy.save+numpy.load == fastnumpyio.pack+fastnumpyio.unpack: True
```

macOS 12.5, Python 3.9.15 arm64, Numpy 1.24.0, Apple M1:
```
numpy.save: 0:00:00.831839
fastnumpyio.save: 0:00:00.389113
fastnumpyio.pack: 0:00:00.298685
numpy.load: 0:00:07.552911
fastnumpyio.load: 0:00:00.301430
fastnumpyio.unpack: 0:00:00.179266
numpy.save+numpy.load == fastnumpyio.save+fastnumpyio.load: True
numpy.save+numpy.load == fastnumpyio.pack+fastnumpyio.unpack: True
```

With larger arrays (3x512x512), fastnumpyio is still slightly faster for save and 2 times faster for load.

When using fastnumpyio.pack/fastnumpyio.unpack the packed bytes object is formatted like this:
```
endianness: 1 byte, value can be '<', '>', '|'
type: 1 byte, value can be 'b', 'i', 'u', 'f', 'c'
type size: 1 byte, value can be 1, 2, 4, 8, 16
number of dimensions: 1 byte, value can be 0-255
shape: 4 bytes per dimension
raw samples data
```
