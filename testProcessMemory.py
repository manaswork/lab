# encoding: utf-8

import ctypes
import multiprocessing
import numpy as NP
import os
import time
#arr = NP.zeros(int(6e7)).reshape(-1,200000)
shared_array_base = multiprocessing.Array(ctypes.c_double, int(6e7))
shared_array = NP.ctypeslib.as_array(shared_array_base.get_obj())
arr = shared_array.reshape(-1,200000)

def my_func(i):
    arr[i,:] = i
    arr[:,i] = i

if __name__ == '__main__':
    for i in range(int(3e2)):
        pid = os.fork()
        if(pid == 0):
            my_func(i)    
            time.sleep(100)
            os._exit(0)
    print arr[:11,:]
    time.sleep(100)
