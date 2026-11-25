import numpy as np

from GridInit import TetrisInit as Init
from FindCol import FindValidPlacements as AllMoves
from DellacherieFeatures import GetLandingHeight as EmptyHeight

def Dellacherie2D(Pieces, VertOri, dims):
    Grid = Init(VertOri, dims)
    evalWeights = [-1, 1, -1, -1, -4, -1]
    for piece in Pieces:
        #piece[0] is always length
        #piece[1] is always height
        scoresH = [] #this will hold the scores for every possible horizontal move with the current piece
        scoresV = [] #this will hold the scores for every possible vertical move with the current piece

        rec = False #this helps skip vertical analysis if piece has equal dimensions
        if piece[0] == piece[1]:
            rec = True

        #horizontal inspection
        possibleMovesH = AllMoves(Grid, piece) #this gets all possible moves when piece is horizontally placed
        if possibleMovesH != []: #if piece can fit in horizontal orientation
            for i in possibleMovesH: #for every move
                LandingHeight = EmptyHeight(Grid, i) - piece[1]
                RowsEliminated = 0 #number of completely filled rows if piece would be placed
                for k in range(LandingHeight, np.shape(Grid)[0]):
                    if np.all(Grid[k, :i] == 1) and np.all(Grid[k, i + piece[0]:] == 1):
                        RowsEliminated += 1
                RowTransitions = 0 #different parity among same row cells
                for k in range(LandingHeight, LandingHeight + piece[1]):
                    #if you get an out of bounds error here check AllMoves() for out of bounds errors
                    if i != 0: #if piece wont have an edge placement on the left side
                        if Grid[k, i - 1] == Grid[k, i]: #check equality cz piece is not placed yet
                            RowTransitions += 2
                    if i + piece[0] != np.shape(Grid)[1]: #if piece wont have an edge placement on the right side
                        if Grid[k, i + piece[0] - 1] == Grid[k, i + piece[0]]: #check equality cz piece is not placed yet
                            RowTransitions += 2
                ColumnTransitions = 0 #different parity among same column cells
                if LandingHeight != 0: #if piece wont have an edge placement on the upper side
                    if Grid[LandingHeight, i] == Grid[LandingHeight - 1, i]: #check equality cz piece is not placed yet
                        ColumnTransitions += 2 #column transitions happen along the piece length
                if LandingHeight + piece[1] != np.shape(Grid)[0]: #if piece wont have an edge placement on the bottom side
                    if Grid[LandingHeight + piece[1], i] == Grid[LandingHeight + piece[1] - 1, i]: #check equality cz piece is not placed yet
                        ColumnTransitions += 2 #column transitions happen along the piece length
                #number of empty cells along a column that are covered by complete cells
                NumberOfHoles = 0
                HoleStarts = []
                if LandingHeight + piece[1] != np.shape(Grid)[0]: #if piece wont have a bottom placement
                    for k in range(i, i + piece[0]):
                        if Grid[LandingHeight + piece[1], k] == 0:
                            HoleStarts.append(k)
                    for k in HoleStarts:
                        depth = LandingHeight + piece[1]
                        while depth != np.shape(Grid)[0]:
                            if Grid[depth, k] == 0:
                                NumberOfHoles += 1
                            depth += 1
                WellSums = 0 #bunch of empty cells flanked by full cells
                #an edge move wont create new wells
                if i > 0 and i + piece[0] < np.shape(Grid)[1]: #if current move isnt an edge move
                    if Grid[LandingHeight, i - 1] == Grid[LandingHeight, i] and Grid[LandingHeight, i + piece[0] - 1] == Grid[LandingHeight, i + piece[0]]:
                        WellSums += 2

                features = [LandingHeight, RowsEliminated, RowTransitions, ColumnTransitions, NumberOfHoles, WellSums]
                score = sum([j * k for j, k in zip(features, evalWeights)]) #calculate move score
                scoresH.append(score)

        #vertical inspection
        if rec == False:
            piece[0], piece[1] = piece[1], piece[0] #rotate piece
            possibleMovesV = AllMoves(Grid, piece) #this gets all possible moves with the current piece
            if possibleMovesV == [] and possibleMovesH == []: #if piece cant fit grid
                return [tuple(piece), Grid] #throw up the piece that created the problem and the grid before
            if possibleMovesV != []:
                for i in possibleMovesV:
                    LandingHeight = EmptyHeight(Grid, i) - piece[1]
                    RowsEliminated = 0 #number of completely filled rows if piece would be placed
                    for k in range(LandingHeight, np.shape(Grid)[0]):
                        if np.all(Grid[k, :i] == 1) and np.all(Grid[k, i + piece[0]:] == 1):
                            RowsEliminated += 1
                    RowTransitions = 0 #different parity among same row cells
                    for k in range(LandingHeight, LandingHeight + piece[1]):
                        #if you get an out of bounds error here check AllMoves() for out of bounds errors
                        if i != 0: #if piece wont have an edge placement on the left side
                            if Grid[k, i - 1] == Grid[k, i]: #check equality cz piece is not placed yet
                                RowTransitions += 2
                        if i + piece[0] != np.shape(Grid)[1]: #if piece wont have an edge placement on the right side
                            if Grid[k, i + piece[0] - 1] == Grid[k, i + piece[0]]: #check equality cz piece is not placed yet
                                RowTransitions += 2
                    ColumnTransitions = 0 #different parity among same column cells
                    if LandingHeight != 0: #if piece wont have an edge placement on the upper side
                        if Grid[LandingHeight, i] == Grid[LandingHeight - 1, i]: #check equality cz piece is not placed yet
                            ColumnTransitions += 2 #column transitions happen along the piece length
                    if LandingHeight + piece[1] != np.shape(Grid)[0]: #if piece wont have an edge placement on the bottom side
                        if Grid[LandingHeight + piece[1], i] == Grid[LandingHeight + piece[1] - 1, i]: #check equality cz piece is not placed yet
                            ColumnTransitions += 2 #column transitions happen along the piece length
                    #number of empty cells along a column that are covered by complete cells
                    NumberOfHoles = 0
                    HoleStarts = []
                    if LandingHeight + piece[1] != np.shape(Grid)[0]: #if piece wont have a bottom placement
                        for k in range(i, i + piece[0]):
                            if Grid[LandingHeight + piece[1], k] == 0:
                                HoleStarts.append(k)
                        for k in HoleStarts:
                            depth = LandingHeight + piece[1]
                            while depth != np.shape(Grid)[0]:
                                if Grid[depth, k] == 0:
                                    NumberOfHoles += 1
                                depth += 1
                    WellSums = 0 #bunch of empty cells flanked by full cells
                    #an edge move wont create new wells
                    #if you get a bug here add -1 to shape
                    if i > 0 and i + piece[0] < np.shape(Grid)[1] - 1: #if current move isnt an edge move
                        if Grid[LandingHeight, i - 1] == Grid[LandingHeight, i] and Grid[LandingHeight, i + piece[0] - 1] == Grid[LandingHeight, i + piece[0]]:
                            WellSums += 2
                    features = [LandingHeight, RowsEliminated, RowTransitions, ColumnTransitions, NumberOfHoles, WellSums]
                    score = sum([j * k for j, k in zip(features, evalWeights)]) #calculate move score
                    scoresV.append(score)

        if scoresH == [] and scoresV == []:
            return [piece, Grid] #throw up the piece that created the problem and the grid before
        elif scoresH == []:
            ChosenMove = possibleMovesV[np.argmax(scoresV)]
            finalOri = "V"
        elif scoresV == []:
            ChosenMove = possibleMovesH[np.argmax(scoresH)]
            finalOri = "H"
        else:
            ChosenMove = possibleMovesH[np.argmax(scoresH)] if max(scoresH) > max(scoresV) else possibleMovesV[np.argmax(scoresV)] #find best move
            finalOri = "H" if max(scoresH) > max(scoresV) else "V"

        allHeights = []

        if finalOri == "H" and rec == False: #remember that piece is already rotated at this point
            piece[0], piece[1] = piece[1], piece[0] #rotate again
        for k in range(ChosenMove, ChosenMove + piece[0]): #determine actual landing height for specific move
            allHeights.append(EmptyHeight(Grid, k) - piece[1])
        Height = min(allHeights)

        Grid[Height : Height + piece[1], ChosenMove : ChosenMove + piece[0]] = 1 #play move

    return Grid
