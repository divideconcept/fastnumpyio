# Fastnumpyio
Fast Numpy I/O : Fast replacements for numpy.load and numpy.save

numpy.load and numpy.save is not optimal speed wise, specially if your arrays don't have complex internal structures.

fastnumpyio.load/fastnumpyio.save can be used as a replacement to numpy.load/numpy.save with a significant speedup.

fastnumpyio.pack/fastnumpyio.unpack (saving/loading bytes objects) is even faster if you don't care about the npy format and path/file-like objects

Running fastnumpyio.py (saving and loading 100k float32 array with shape 3x64x64) shows the following results:

Windows 11, Python 3.9.5, Numpy 1.23.3, Intel Core i7-12700K:
```
numpy.save: 0:00:00.813492
fastnumpyio.save: 0:00:00.334398
fastnumpyio.pack: 0:00:00.316542
numpy.load: 0:00:07.910804
fastnumpyio.load: 0:00:00.306737
fastnumpyio.unpack: 0:00:00.189628
numpy.save+numpy.load == fastnumpyio.save+fastnumpyio.load: True
numpy.save+numpy.load == fastnumpyio.pack+fastnumpyio.unpack: True
```

macOS 12.5, Python 3.9.5, Numpy 1.21.5, Apple M1:
```
numpy.save: 0:00:00.789568
fastnumpyio.save: 0:00:00.361045
fastnumpyio.pack: 0:00:00.300050
numpy.load: 0:00:07.271897
fastnumpyio.load: 0:00:00.289059
fastnumpyio.unpack: 0:00:00.168710
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
