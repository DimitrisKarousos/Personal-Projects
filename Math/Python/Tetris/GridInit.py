import numpy as np
import sys #helper lib

np.set_printoptions(threshold=sys.maxsize) #blocks automatic truncated representation for large tables

def TetrisInit(VertOri, dims):
    if VertOri == True:
        Grid = np.zeros((max(dims[0], dims[1]), min(dims[0], dims[1])))
    else:
        Grid = np.zeros((min(dims[0], dims[1]), max(dims[0], dims[1])))
    #print("Start:")
    #print(Grid)
    #print(" ")
    return Grid
