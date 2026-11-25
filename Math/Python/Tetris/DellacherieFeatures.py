import numpy as np

def GetLandingHeight(Grid, CurrCol):
    emptyHeight = 0
    for i in range(np.shape(Grid)[0]):
        if Grid[i, CurrCol] == 0: #as long as Grid elements keep on being empty
            emptyHeight += 1 #the size of the empty column increases
        else:
            return emptyHeight #else empty column size is calculated
    return emptyHeight

def CheckrowFull(Grid, CurrCol, piece):
    Rows = 0
    return Rows
