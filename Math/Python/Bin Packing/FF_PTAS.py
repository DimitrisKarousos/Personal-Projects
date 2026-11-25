from decimal import *
import math as m

from FirstFit import FirstFit as FF

def FF_PTAS(e, BinCapacity, VolList, currentcapacity = 0):
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

    eListffRes = FF(BinCapacity, eList) #solve that list with FirstFit
    BinsNeeded += eListffRes[0]
    Remainders.append(eListffRes[1])

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
        res = FF(BinCapacity, element) #solve each sublist with FirstFit
        BinsNeeded += res[0]
        Remainders.append(res[1])    

    return [BinsNeeded, Remainders]
