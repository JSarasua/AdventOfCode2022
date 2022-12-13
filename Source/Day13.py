from AoCUtilities import *
import ast
import functools
from collections import Counter



def IsRightOrder(packet1, packet2) -> int:

    if isinstance(packet1,int):
        if isinstance(packet2,int):
            if packet1 < packet2:
                return 1
            elif packet1 > packet2:
                return -1
            else:
                return 0
        else:
            packet1List = [packet1]
            return IsRightOrder(packet1List, packet2)
    elif isinstance(packet2,int):
        packet2List = [packet2]
        return IsRightOrder(packet1, packet2List)

    #List v List
    packet1Len = len(packet1)
    packet2Len = len(packet2)

    lenToRun = packet1Len if packet1Len <= packet2Len else packet2Len


    for index in range(lenToRun):
        returnVal = IsRightOrder(packet1[index], packet2[index])
        if returnVal == 1:
            return 1
        elif returnVal == -1:
            return -1
        else:
            continue

    if packet1Len < packet2Len:
        return 1
    elif packet1Len > packet2Len:
        return -1
    else:
        return 0

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    pairsInRightOrder = 0

    packet1 = None
    packet2 = None

    currentIndice = 1

    for fileLine in fileData:
        if fileLine == '\n':
            continue

        if packet1 == None:
            packet1 = ast.literal_eval(fileLine.strip())
        elif packet2 == None:
            packet2 = ast.literal_eval(fileLine.strip())

        if packet1 != None and packet2 != None:
            if IsRightOrder(packet1, packet2) == 1:
                pairsInRightOrder += currentIndice
            packet1 = None
            packet2 = None
            currentIndice += 1

    return pairsInRightOrder


def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    packets = []
    for fileLine in fileData:
        if fileLine == '\n':
            continue
        packets.append(ast.literal_eval(fileLine.strip()))
    key1 = [[2]]
    key2 = [[6]]

    packets.append(key1)
    packets.append(key2)

    sortedPackets = sorted(packets, key=functools.cmp_to_key(IsRightOrder), reverse=True)

    key1Pos = 0
    key2Pos = 0

    for index in range(len(sortedPackets)):
        if sortedPackets[index] == key1:
            key1Pos = index + 1
        if sortedPackets[index] == key2:
            key2Pos = index + 1

    return key1Pos * key2Pos


filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day13.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))
