from decimal import *
import math as m

from BestFit import BestFit as BF
def BF_PTAS(e, BinCapacity, VolList, currentcapacity = 0):
    BinsNeeded = 0
    Remainders = []

    inst = VolList.copy()

    #K = m.ceil(1 / e ** 2)
    Q = m.floor(e ** 2)

    eList = []

    for i in inst: #create a separate list for bags with volume < e
        if i < e:
            eList.append(i)
            inst.remove(i)

    eListbfRes = BF(BinCapacity, eList) #solve that list with FirstFit
    BinsNeeded += eListbfRes[0]
    Remainders.append(eListbfRes[1])

    inst.sort()

    kGroupsNum = m.floor(len(inst) / Q)

    kGroups = []

    for i in range(kGroupsNum): #partition list into K groups of Q
        sublist = []
        while len(sublist) <= Q and inst != []:
            sublist.append(inst[0])
            inst.remove(inst[0])
        kGroups.append(sublist)

    kGroups.append(inst) #make a separate sublist for leftover bags

    for element in kGroups: #round all bags in each group to the largest bag in the current group
        for i in range(len(element)):
            element[i] = max(element)
        res = BF(BinCapacity, element) #solve each sublist with FirstFit
        BinsNeeded += res[0]
        Remainders.append(res[1])     

    return [BinsNeeded, Remainders]
