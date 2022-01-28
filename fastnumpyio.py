import numpy as np
import struct

def fast_numpy_save(array):
    size=len(array.shape)
    return bytes(array.dtype.str,'utf-8')+struct.pack(f'<B{size}I',size,*array.shape)+array.tobytes()

def fast_numpy_load(data):
    dtype = str(struct.unpack_from('<3s', data, 0)[0],'utf-8')
    size = struct.unpack_from('<B', data, 3)[0]
    shape = struct.unpack_from(f'<{size}I', data, 4)
    return np.ndarray(shape, dtype=dtype, buffer=data[4+size*4:])

if __name__ == "__main__":
    import io
    from timeit import default_timer as timer
    from datetime import timedelta
    iterations=100000
    testarray=np.float32(np.random.rand(3,64,64))

    start = timer()
    for i in range(iterations):
        buffer = io.BytesIO()
        np.save(buffer, testarray)
        numpy_save_data=buffer.getvalue()
    print("numpy.save:",timedelta(seconds=timer()-start))

    start = timer()
    for i in range(iterations):
        fast_numpy_save_data=fast_numpy_save(testarray)
    print("fast_numpy_save:",timedelta(seconds=timer()-start))

    start = timer()
    for i in range(iterations):
        buffer = io.BytesIO(numpy_save_data)
        testarray_numpy_save=np.load(buffer)
    print("numpy.load:",timedelta(seconds=timer()-start))

    start = timer()
    for i in range(iterations):
        testarray_fast_numpy_save=fast_numpy_load(fast_numpy_save_data)
    print("fast_numpy_load:",timedelta(seconds=timer()-start))

    print("numpy.save+numpy.load == fast_numpy_save+fast_numpy_load:", np.array_equal(testarray_numpy_save,testarray_fast_numpy_save))
