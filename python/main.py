#!/usr/bin/env python3

import os
import numpy as np
from cffi import FFI

# Import Utils
from cffi_utils import ensure_folder_or_file, ensure_np_type
from cffi_utils import get_pointer_to_np_arr


# Wrapper Class myProcessor
class MyProcessor:

    def __init__(self, cpp_lib, ffi, exp, size):
        self.cpp_lib = cpp_lib
        self.ffi = ffi
        self.id = self.cpp_lib.myProcessorInit(exp, size)

    def process(self, data, size):
        data = ensure_np_type(data, 'float64')
        pointer_to_data = get_pointer_to_np_arr(data, "double*", self.ffi)
        ret = self.cpp_lib.myProcessorProcess(self.id, pointer_to_data, size)
        if ret < 0:
            raise ValueError("Sth bad happened in c++ code")
        else:
            return data


def main():
    # Libs
    sharedLibFolderURI = os.path.abspath("../cpp_lib/bin")
    headerFileURI = os.path.abspath("../cpp_lib/cpp_lib.h")
    dllURI = os.path.join(sharedLibFolderURI, "lib.so")

    # Preparations
    ensure_folder_or_file(sharedLibFolderURI)
    ensure_folder_or_file(headerFileURI)
    ensure_folder_or_file(dllURI)
    functionDefinitions = "".join([
        "unsigned int myProcessorInit(int exp_in, int size_in);",
        "int myProcessorProcess(unsigned int id, double *d, int size);"
    ])

    # Add Lib to PATH
    os.environ['PATH'] = sharedLibFolderURI + os.pathsep + os.environ['PATH']

    # Instantiate FFI
    ffi = FFI()
    cpp_lib = ffi.dlopen(dllURI)
    ffi.cdef(functionDefinitions)

    exp = 2
    size = 10
    data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    mpInst = MyProcessor(cpp_lib, ffi, exp, size)
    data = mpInst.process(data, size)
    print(data)


if __name__ == "__main__":
    main()
