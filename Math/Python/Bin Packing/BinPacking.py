import math as m
from decimal import *

def BinPacking(BinCapacity, WasteBagVol, NoOfWasteBags, currentCapacity = 0):
    error = "Waste bags are bigger than the designated bin size."

    if WasteBagVol > BinCapacity:
        return error

    TotalVol = WasteBagVol * NoOfWasteBags
    lowerBound = m.ceil(TotalVol / BinCapacity)
    remainingBags = NoOfWasteBags

    BinsNeeded = 1

    remainder = [float(BinCapacity - currentCapacity)] #first bin starts empty

    for i in range(lowerBound): #fill lowerBound bins
        while currentCapacity < BinCapacity and remainingBags > 0:
            remainingBags -= 1
            currentCapacity += WasteBagVol
            if currentCapacity < BinCapacity:
                remainder[i] = float(BinCapacity - currentCapacity) #update current bin remainder
        if currentCapacity > BinCapacity:
            BinsNeeded += 1
            currentCapacity -= WasteBagVol
            remainingBags += 1
            remainder.append(float(BinCapacity - currentCapacity))
            currentCapacity = 0
        elif currentCapacity == BinCapacity:
            remainder[i] = 0 #current bin is full
            if remainingBags > 0:
                BinsNeeded += 1
                remainder.append(0) #add another empty bin
                currentCapacity = 0

    while remainingBags > 0:
        currentCapacity += WasteBagVol
        remainingBags -= 1
        if currentCapacity < BinCapacity:
            remainder[-1] = float(BinCapacity - currentCapacity)
        elif currentCapacity > BinCapacity:
            currentCapacity -= WasteBagVol
            remainingBags += 1
            BinsNeeded += 1
            remainder.append(float(BinCapacity - currentCapacity))
            currentCapacity = 0
        elif currentCapacity == BinCapacity and remainingBags > 0:
            BinsNeeded += 1
            remainder.append(0)
            currentCapacity = 0

    #returns number of bins needed, the remaining empty volume on each bin and the wastebag size
    return [BinsNeeded, remainder, WasteBagVol]
