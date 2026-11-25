from FirstFit import FirstFit as FF

from decimal import *

def RFF(BinCapacity, VolList, m = 6, k = 1):
#NOT an AF algorythm, results may not be optimal
    #bag types
    A = []
    B1 = []
    B2 = []
    X = []

    #bin types
    Class1 = []
    Class2 = []
    Class3 = []
    Class4 = []

    for bag in VolList:
        if bag <= BinCapacity / 3:
            X.append(bag)
        elif bag <= 2 * BinCapacity / 5:
            B2.append(bag)
        elif bag <= BinCapacity / 2:
            B1.append(bag)
        else:
            A.append(bag)

    AFF = FF(BinCapacity, A)
    Class1 = AFF[1] #place all A type bags in Class 1 bins

    B1FF = FF(BinCapacity, B1)
    Class2 = B1FF[1] #place all B1 type bag in Class 2 bins

    XFF = FF(BinCapacity, X)
    Class4 = XFF[1] #place all X type bags in Class 4 bins

    expt = []
    for i in range(len(B2)): #find mk-th bags
        if i % (m * k) == 0:
            expt.append(B2[i])
            B2.remove(B2[i])

    exptFF = FF(BinCapacity, expt)
    Class1 += exptFF[1] #place those bags in Class 1 bins

    B2FF = FF(BinCapacity, B2)
    Class3 = B2FF[1] #place the rest of B2 bags in Class 3 bins

    BinsNeeded = AFF[0] + B1FF[0] + B2FF[0] + exptFF[0] + XFF[0]
    Remainders = Class1 + Class2 + Class3 + Class4

    for i in Remainders: #filter out resulting empty bins
        if i == BinCapacity:
            BinsNeeded -= 1

    return [BinsNeeded, Remainders]
