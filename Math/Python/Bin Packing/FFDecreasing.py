import FirstFit as ff

from decimal import *

def FFD(BinCapacity, VolList, currentCapacity = 0):
    inst = VolList.copy()
    inst.sort(reverse = True)

    return ff.FirstFit(BinCapacity, inst, currentCapacity)
