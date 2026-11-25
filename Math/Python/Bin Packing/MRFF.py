from RefinedFF import RFF

from decimal import *

def MRFF(BinCapacity, VolList, currentCapacity = 0):
    large = []
    medium = []
    small = []
    tiny = []

    for bag in VolList: #separate all bags into four distinct categories
        if bag <= BinCapacity / 6:
            tiny.append(bag)
        elif bag <= BinCapacity / 3:
            small.append(bag)
        elif bag <= BinCapacity / 2:
            medium.append(bag)
        else:
            large.append(bag)

    large.sort(reverse = True)
    medium.sort()
    small.sort()

    #First Step
    Bins = large #allot a bin for each large bag

    #Second Step
    BinsWithMediumBag = []

    for b in range(len(Bins)): #for each of those bins
        if medium != []:
            if Bins[b] + medium[0] <= BinCapacity: #if the smallest medium item fits in it
                    med = max(m for m in medium if Bins[b] + m <= BinCapacity)
                    Bins[b] += med #add the biggest medium item that fits in it
                    medium.remove(med)
                    BinsWithMediumBag.append(b) #save which bins have a medium bag stored in them

    #Third Step
    rBins = []

    for i in reversed(Bins):
        rBins.append(i)

    for b in range(len(rBins)): #for each bin in reversed order
        if b not in BinsWithMediumBag: #for all bins that dont contain a medium bag
            if len(small) >= 2: #if there are at least 2 small bags
                if rBins[b] + small[0] + small[1] <= BinCapacity: #if the two smallest small bags fit
                    rBins[b] += small[0] #add the smallest small bag
                    small.remove(small[0])
                    smol = max(s for s in small if rBins[b] + s <= BinCapacity)
                    rBins[b] += smol #add the largest small bag that fits
                    small.remove(smol)

    #Fourth Step
    remainingBags = tiny + small + medium #all unstored bags
    remainingBags.sort()

    finalBins = []

    for i in reversed(rBins):
        finalBins.append(i)

    for b in range(len(finalBins)): #for each bin in forward order
        while remainingBags != [] and finalBins[b] + remainingBags[0] <= BinCapacity: #if the smallest remaining bag fits
            rem = max(r for r in remainingBags if finalBins[b] + r <= BinCapacity)
            finalBins[b] += rem #add the largest remaining bag
            remainingBags.remove(rem)

    #Fifth Step
    if remainingBags != []:
        rffRes = RFF(BinCapacity, remainingBags, currentCapacity) #use FFD on remaining bags
    else:
        rffRes = [0, []]

    BinsNeeded = len(finalBins) + rffRes[0]

    Remainders = []

    for i in finalBins:
        Remainders.append(float(BinCapacity - i))

    Remainders += rffRes[1]

    return [BinsNeeded, Remainders]
