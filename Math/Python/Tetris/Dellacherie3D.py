import numpy as np
from functools import reduce
import copy

from GridInit import TetrisInit as Init
from Dellacherie2D import Dellacherie2D as packFloor

def Dellacherie3DSolver(Pieces, VertOri, dims):
        Grid3D = Init(VertOri, dims)
        FloorMaps = [Grid3D] #this will hold the snapshots of each 2d solution
        #Grid3DLim = dims[2]
        #Assume that all pieces share a common dimension
        Trim = list(set(piece) for piece in Pieces) #trim equal dimensions in the same piece to reduce the number of elements
        comDim = list(reduce(lambda i, j : i & j, Trim)) #Find the shared dimension between all pieces
        depth = 0
        if comDim == []: #if no dimension is shared across all pieces
                print("Error! Proof of consept requires that the lists representing each piece share at least one common element.")
                return
        elif len(comDim) > 1: #in the case where more than one dimensions are shared
                depth = max(comDim) #always assume the largest value to be the depth
        else: #common case scenario
                depth = comDim[0]
        #remove the common dimension from all elements in Pieces
        Pieces2d = copy.deepcopy(Pieces)
        for piece in Pieces2d:
                piece.remove(depth)
        #use the curated list as the input for the 2d solver
        FloorSnapshot = packFloor(Pieces2d, VertOri, [dims[0], dims[1]])
        FloorSnapshot = FloorSnapshot * depth #expand into 3D using the shared dimension of all pieces
        #if packing returned more than one elements, there are pieces that couldnt fit in the current floor
        while type(FloorSnapshot[0]) is tuple: #since the remaining pieces are marked as tuples, the type() method will serve as the end condition
                FloorMaps.append(FloorSnapshot[1] * depth) #take a snapshot of the filled floor and store it
                faultInd = Pieces2d.index(list(FloorSnapshot[0])) #get the index of the first piece that couldnt fit
                #print(faultInd)
                FloorSnapshot = packFloor(Pieces2d[faultInd:], VertOri, [dims[0], dims[1]])
                #print(FloorSnapshot)
        FloorMaps.append(FloorSnapshot * depth) #append the final piece that was packed
        for i in range(len(FloorMaps)): #flip every other snapshot to better take advantage of empty dpace in the top half
                if i % 2 == 0:
                        FloorMaps[i] = list(reversed(FloorMaps[i]))
        for i in range(1, len(FloorMaps) - 1):
                #print(FloorMaps[-1])
                #print(" ")
                CeilCheck = np.add(FloorMaps[i], FloorMaps[-1]) #stack snapshots in pairs
                #if np.max(CeilCheck) > Grid3DLim: #check if bin overflows
                #        print("Height limit reached.")
                #        return FloorMaps[-1]
                FloorMaps[-1] = CeilCheck #store the stacking result in the last element
        return FloorMaps[-1]
