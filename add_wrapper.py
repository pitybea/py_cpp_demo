from numpy.ctypeslib import ctypes
import numpy as np

lib = ctypes.cdll.LoadLibrary('add.so')

func = lib.add

func.restype = ctypes.c_int

func.argtypes = [
    ctypes.c_int,
    ctypes.c_int
]

if __name__ == '__main__':
    print(func(71, 88))
