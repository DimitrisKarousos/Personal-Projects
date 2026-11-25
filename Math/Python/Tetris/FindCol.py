import numpy as np

def FindValidPlacements(Grid, piece, target = 0):
    possibleCols = []
    (gridRows, gridCols) = np.shape(Grid)
    for i in range(gridCols): #check every column
        if i + piece[0] <= gridCols: #if column-wise placement is possible
            if np.all(Grid[0, i : i + piece[0]] == target): #if current columns are empty
                if np.all(Grid[0 : piece[1], i : i + piece[0]] == target): #if row-wise placement is possible
                    possibleCols.append(i)
    return possibleCols
