import numpy as np

def FirstFitDecreasingHeight(Items, BinParams = [0, 1, 2, 1]): #parameters must be expressed in cm
    #let BinParams[0] denote the shape of the bin
    if BinParams[0] == 0: #let 0 deote a square shaped bin
        BinLength = BinParams[1]
        BinWidth = BinParams[2]
    #elif BinParams[0] == 1: #let 1 denote a circle shaped bin
    #    BinRad = BinParams[1]
    else: return "Only square and circle shaped bins are currently supported"

    #sort all items based on decreasing hieght, which is the minimum of each item dimension
    Items.sort(reversed = True, key = lambda item : min(item))

    if BinParams[0] == 0: #for square bins, map surface area to a zero filled array
        FloorArea = np.zeros((BinWidth, BinLength))

        #determine bin orientation
        BinOri = 1 if BinWidth > BinLength else 0 #1 = vertical, 0 = horizontal or square bin
        unpacked = []

        for item in Items:
            ori = sorted(item)
            #object height, minimum, since we are trying to minimize height
            #object length, maximum if vertical bin orientation
            #object width, maximum if horizontal bin orientation
            [h, l, w] = [ori[0], ori[2] if BinOri == 1 else ori[1], ori[2] if BinOri == 0 else ori[1]]
            print("Item no:" + str(Items.index(item) + 1) + "\nHeight: " + str(h) + "\nLength: " + str(l) + "\nWidth: " + str(w))

            start = 0

            if BinOri == 0: #on a horizontal or square bin
                if start + w <= BinLength: #if item would fit next to the last item
                    FloorArea[0 : l][start : start + w] += h #add item at the first available top-left spot, leftwinse momentum
                    start += w + 1 #next item is placed after this one
                else:
                    unpacked.append(Items.index(item)) #item doesnt fit in current floor
            if BinOri == 1: #on a vertical bin
                if start + l <= BinWidth:
                    FloorArea[start : start + l][0 : w] += h #add item at the first available top-left spot, downward momentum
                    start += l + 1
                else:
                    unpacked.append(Items.index(item)) #item doesnt fit in current floor

        #deal with unpacked items, keeping in mind they are already ordered
        print("Now placing unpacked items at indexes: " + str(unpacked))
        ori = sorted(item)
        #object height, minimum, since we are trying to minimize height
        #object length, maximum if vertical bin orientation
        #object width, maximum if horizontal bin orientation
        [h, l, w] = [ori[0], ori[2] if BinOri == 1 else ori[1], ori[2] if BinOri == 0 else ori[1]]
        print("Item no:" + str(Items.index(item) + 1) + "\nHeight: " + str(h) + "\nLength: " + str(l) + "\nWidth: " + str(w))
