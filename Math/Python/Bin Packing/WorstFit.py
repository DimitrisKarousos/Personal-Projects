from decimal import *

def WorstFit(BinCapacity, VolList, currentCapacity = 0):
    Bins = [float(currentCapacity)]

    for v in VolList:
        BagStored = False #all bags start off as unstored
        worst = -1
        for i in range(len(Bins)):
            if Bins[i] + float(v) <= BinCapacity and Bins[i] <= Bins[worst]: #find emptiest bin
                worst = i
        if worst != -1: #if bin that can accomodate v is found
            Bins[worst] += float(v) #add bag to bin
            BagStored = True #mark bag as stored
        if BagStored == False: #if bag hasnt been stored after looking at all bins
            Bins.append(float(v)) #create a new bin for the bag

    BinsNeeded = len(Bins)
    Remainders = []

    for i in Bins:
        Remainders.append(BinCapacity - i)

    return [BinsNeeded, Remainders]
