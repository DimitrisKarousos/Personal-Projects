import numpy as np
from FindSubarray import FindSetSizeSubarray as Find

def BottomUpLeftJustified2D(Items, BinParams = [0, 1, 2, 1]): #parameters must be expressed in cm
    #let BinParams[0] denote the shape of the bin
    if BinParams[0] == 0: #let 0 denote a square shaped bin
        BinLength = BinParams[1]
        BinWidth = BinParams[2]
        BinHeight = BinParams[3]
    elif BinParams[0] == 1: #let 1 denote a circle shaped bin
        #BinRad = BinParams[1]
        BinHeight = BinParams[2]
    else: return "Only square and circle shaped bins are currently supported"

    if BinParams[0] == 0: #for square bins, map surface area to a zero filled array
        FloorArea = np.zeros((BinWidth, BinLength))

        unpacked = [] #this will store items not packed in current floor
        toNewBin = [] #this will store items that wont fit current bin due to height restriction
        binGeometry = [] #this will store the floor geometry of all bins

        for item in Items: #assume all items will be rectangular
            ori = sorted(item) #sort dimensions to determine object orientation
            #object height, minimum, since we are trying to minimize height
            #object length, maximum if vertical bin orientation
            #object width, maximum if horizontal bin orientation
            [h, l, w] = [ori[0], ori[2] if BinLength > BinWidth else ori[1], ori[2] if BinWidth > BinLength else ori[1]]

            packedInCurrFloor = False
            #check if item can fit the deepest level from left to right
            inspection = Find(FloorArea, [l, w], FloorArea.min())
            if inspection != None: #if item fits
                packedInCurrFloor = True
                if (FloorArea[inspection[0][0]] + h).all() <= BinHeight: #if height condition is satisfied
                    #add item height to the designated cells
                    if inspection[1] == 0:
                        FloorArea[inspection[0][0] : inspection[0][0] + l, inspection[0][1] : inspection[0][1] + w] += h
                    elif inspection[1] == 1:
                        FloorArea[inspection[0][0] : inspection[0][0] + w, inspection[0][1] : inspection[0][1] + l] += h
                    else:
                        print("Orientation of fitted item was neither 0, nor 1, check Find() for possible bugs")
                else:
                    toNewBin.append(Items.index(item)) #mark item for new bin
            #if item can still not be packed and is not marked for a new bin, mark it as unpacked
            if(packedInCurrFloor == False and Items.index(item) not in toNewBin):
                unpacked.append(Items.index(item))

        #After running through all items
        LowPoint = FloorArea.min() #Find the deepest empty cell
        while unpacked != []: #if there are still unpacked items
            for ind in unpacked:
                LowPoint += 1 #incriment low point by 1 since no item in unpacked will fit in that level
                ori = sorted(Items[ind])
                [h, l, w] = [ori[0], ori[2] if BinLength > BinWidth else ori[1], ori[2] if BinWidth > BinLength else ori[1]]
                inspection = Find(FloorArea, [l, w], LowPoint) #check if item fits in current level
                if inspection != None: #if item fits
                    if (FloorArea[inspection[0][0]] + h).all() <= BinHeight: #if height condition is satisfied
                        #add item height to the designated cells
                        if inspection[1] == 0:
                            FloorArea[inspection[0][0] : inspection[0][0] + l, inspection[0][1] : inspection[0][1] + w] = LowPoint + h
                            unpacked.remove(ind) #remove index of unpacked item
                        elif inspection[1] == 1:
                            FloorArea[inspection[0][0] : inspection[0][0] + w, inspection[0][1] : inspection[0][1] + l] = LowPoint + h
                            unpacked.remove(ind) #remove index of unpacked item
                        else:
                            print("Orientation of fitted item was neither 0, nor 1, check Find() for possible bugs")
                    else: #if height condition is not satisfied
                        toNewBin.append(ind) #mark item for new bin
                        unpacked.remove(ind) #remove index of unpacked item

        binGeometry.append(FloorArea) #FloorArea will be a bin that will no longer fit any item, hence it is added to the overall list

        if toNewBin != []: #if new bin is needed
            if BinParams[0] == 0: #on a square surface
                FloorArea = np.zeros((BinWidth, BinLength)) #open a fresh bin

    return binGeometry
