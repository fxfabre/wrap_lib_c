#!/usr/bin/env python3

import os
import numpy as np


def ensure_folder_or_file(file_path):
    if not os.path.isdir(file_path) and not os.path.isfile(file_path):
        raise OSError("Target does not exist.\nSearched for: " + file_path + "\n")


def ensure_np_type(arr, target_type):
    if arr.dtype is not np.dtype(target_type):
        return arr.astype(np.float64)
    else:
        return arr


def get_pointer_to_np_arr(arr, ctype, ffi):
    return ffi.cast(ctype, arr.ctypes.data)
