from AoCUtilities import *
from collections import Counter


def GetLastColStr(cols):
    lastColStr = ''

    for col in cols:
        lastColStr += col[len(col)-1]

    return lastColStr

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    packet = fileData[0].strip()

    bHasFoundIndex = False
    currentIndex = 0
    while not bHasFoundIndex:
        testVals = packet[currentIndex:currentIndex+4]
        uniqueChars = Counter(testVals)
        if(len(uniqueChars) == len(testVals)):
            return currentIndex + 4
        currentIndex += 1
    return 0

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    packet = fileData[0].strip()

    bHasFoundIndex = False
    currentIndex = 0
    while not bHasFoundIndex:
        testVals = packet[currentIndex:currentIndex+14]
        uniqueChars = Counter(testVals)
        if(len(uniqueChars) == len(testVals)):
            return currentIndex + 14
        currentIndex += 1
    return 0

filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day6.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))