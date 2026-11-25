import BinPacking as bp
from decimal import *

def VarBagVolBP(BinCapacity, BagVolList, currentCapacity = 0):
    BagVolList.sort(reverse = True)

    error = "At least one wastebag exceeds bin size."

    if BagVolList[0] > BinCapacity:
        return error

    groupings = [] #list of lists that separates same-sized bags
    sizeChangeIndexes = [0] #stores the indexes where bag sizes change

    results = [] #stores bin packing results
    BinsNeeded = 0
    AllRemainders = []

    for i in range(1, len(BagVolList)): #find size change indexes
        if BagVolList[i] != BagVolList[i - 1]:
            sizeChangeIndexes.append(i)

    sizeChangeIndexes.append(-1) #up to last element in list

    for i in range(1, len(sizeChangeIndexes)): #separate different size bags into lists
        groupings.append(BagVolList[sizeChangeIndexes[i - 1] : sizeChangeIndexes[i]])

    groupings[-1].append(BagVolList[-1]) #add last BagVolList element to the last list in groupings

    #use this to know wether the current capacity of first bin has been accounted for
    curCapDone = False

    for element in groupings: #run bin packing for each distinct list
        if float(element[0]) < BinCapacity - currentCapacity and curCapDone == False:
            results.append(bp.BinPacking(BinCapacity, element[0], len(element), currentCapacity))
            curCapDone = True
        else:
            results.append(bp.BinPacking(BinCapacity, element[0], len(element), 0))

    if curCapDone == False:
        print("No wastebags could fit first bin.")

    #results format: [BinsForCapacityOfX, [RemaindersOnAllBinsOfCapacityX], CapacityXInDecimal]

    #check if results can be merged
    for element1 in results: #compare all lists with each other
        for element2 in results:
            if results.index(element1) > results.index(element2): #ensure it is different lists
                if element2[1] != []: #check if remainder list is empty
                    if element2[1][-1] >= element1[2]: #if there is space in the first list
                        if element1[1] != []: #check if remainder list is empty
                            element1[1][-1] = float(Decimal(str(element1[1][-1])) + element1[2]) #remove a bag from the last bin
                            #it is always possible to do this because at this point bins only have same sized bags in them
                            if element1[1][-1] == float(BinCapacity): #if last bin became empty after doing this
                                element1[1].remove(element1[1][-1]) #delete the last element on the remainder list
                                element1[0] -= 1 #one less bin needed
                            element2[1][-1] = float(Decimal(str(element2[1][-1])) - element1[2]) #add the removed bag to the other bin

    #results[i][0]: Number of Bins
    #results[i][1]: List of remainders
    #results[i][2]: Capacity for those bins in Decimal format               

    for element in results: #work out final results
        BinsNeeded += element[0]
        AllRemainders.append(element[1])

    #filter out empty list objects from remainders list
    AllRemainders = [element for element in AllRemainders if element != []]
    #flatten remainder list
    AllRemainders = [item for sublist in AllRemainders for item in sublist]

    if curCapDone == False:
        BinsNeeded += 1
        AllRemainders.append(float(BinCapacity - currentCapacity))

    return [BinsNeeded, AllRemainders]
