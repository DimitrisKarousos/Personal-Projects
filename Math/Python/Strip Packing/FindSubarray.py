import numpy as np

def FindSetSizeSubarray(BigArray, dims, targetValue):
    #if only one number is given as dims, assume second dimension is 1
    if type(dims) == int:
        dims = [dims, 1]

    BigL, BigW = np.shape(BigArray)

    subL, subW = dims[0], dims[1] #first set subarry on a horizontal orientation

    ori = 0 #ori = 0 --> subarray stayed horizontal
            #ori = 1 --> subarray was flipped to verical

    #search for the subarray
    for i in range(0, BigL - subL + 1):
        for j in range(0, BigW - subW + 1):
            if np.all(BigArray[i : i + subL, j : j + subW] == targetValue):
                return [[i, j], ori] #return top left corner the subarray occupies and its orientaion

    #if this point is reached, it means the subarray doesnt exists in a horizontal orientation
    subL, subW = subW, subL #flip subarray vertically
    ori = 1
    #re-search for subarray
    for i in range(0, BigL - subL + 1):
        for j in range(0, BigW - subW + 1):
            if np.all(BigArray[i : i + subL, j : j + subW] == targetValue):
                return [[i, j], ori] ##return top left corner the subarray occupies and its orientaion
    return None #return none if subarray isnt found
