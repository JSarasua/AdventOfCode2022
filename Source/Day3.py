from AoCUtilities import *
from collections import Counter

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    currentSum = 0
    for fileLine in fileData:
        fileLine = fileLine.strip()
        fileLength = len(fileLine)
        string1, string2 = fileLine[:fileLength//2], fileLine[fileLength//2:]
        hasFoundDup = False
        for char in string1:
            if hasFoundDup:
                break

            for char2 in string2:
                if char == char2:
                    if char.isupper():
                        charNum = ord(char) - (64-26)
                        currentSum += charNum
                        hasFoundDup = True
                        break
                    else:
                        charNum = ord(char) - 96
                        currentSum += charNum
                        hasFoundDup = True
                        break



    return currentSum



def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    lines = [[],[],[]]

    currentSum = 0

    currentLineCount = 0

    for fileLine in fileData:
        lines[currentLineCount] = fileLine.strip()
        if currentLineCount == 2:
            currentLineCount = 0

            hasFoundDup = False
            for char1 in lines[0]:
                if hasFoundDup:
                    break
                for char2 in lines[1]:
                    if hasFoundDup:
                        break
                    if char1 == char2:
                        for char3 in lines[2]:
                            if char1 == char3:
                                if char1.isupper():
                                    charNum = ord(char1) - (64 - 26)
                                    currentSum += charNum
                                    hasFoundDup = True
                                    break
                                else:
                                    charNum = ord(char1) - 96
                                    currentSum += charNum
                                    hasFoundDup = True
                                    break
        else:
            currentLineCount += 1


    return currentSum

filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day3.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))