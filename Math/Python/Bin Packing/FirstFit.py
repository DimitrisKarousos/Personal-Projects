from decimal import *

def FirstFit(BinCapacity, VolList, currentCapacity = 0):
    Bins = [float(currentCapacity)]

    for v in VolList:
        BagStored = False #all bags start off as unstored
        for i in range(len(Bins)):
            if Bins[i] + float(v) <= BinCapacity and BagStored == False: #if bin can store bag
                Bins[i] += float(v)
                BagStored = True
        if BagStored == False: #if bag hasnt been stored after looking at all bins
            Bins.append(float(v)) #create a new bin for the bag

    BinsNeeded = len(Bins)
    Remainders = []

    for i in Bins:
        Remainders.append(BinCapacity - i)

    return [BinsNeeded, Remainders]
