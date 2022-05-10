import ctypes
import os

class MinHeap:
    def __init__(self):
        self.libpath = "lib/libminheap.so"
        if not os.path.exists(self.libpath):
            self.libpath = "../lib/libminheap.so"

        assert os.path.exists(self.libpath), "The library does not exist. Did you compile your source code?"

        self.libpath = os.path.realpath(self.libpath)

        self.c_lib = ctypes.CDLL(self.libpath)

        # Create Binary Search Tree Function
        self.c_lib.createMinHeap.restype = ctypes.c_void_p

        # Push Function
        self.c_lib.push.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

        # Pop Function
        self.c_lib.pop.argtypes = [ctypes.c_void_p]

        # Get Min Distance
        self.c_lib.getMinDistance.argtypes = [ctypes.c_void_p]
        self.c_lib.getMinDistance.restype = ctypes.c_int

        # Get Min Vertex
        self.c_lib.getMinVertex.argtypes = [ctypes.c_void_p]
        self.c_lib.getMinVertex.restype = ctypes.c_int

        # Release Binary Search tree Function
        self.c_lib.releaseMinHeap.argtypes = [ctypes.c_void_p]

        self.heap = self.c_lib.createMinHeap()

    def __del__(self):
        self.c_lib.releaseMinHeap(self.heap)


    def push(self, vertex, distance):
        self.c_lib.push(self.heap, vertex, distance)

    def pop(self):
        self.c_lib.pop(self.heap)

    def top(self):
        vertex = self.c_lib.getMinVertex(self.heap)
        distance = self.c_lib.getMinDistance(self.heap)
        return vertex, distance


if __name__ == "__main__":
    heap = MinHeap()

