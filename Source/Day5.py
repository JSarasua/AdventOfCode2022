from AoCUtilities import *
from collections import Counter

def ExecuteMove(fileLine, cols):
    instructions = fileLine.strip().split(' ')
    numMoves = int(instructions[1])
    fromCol = int(instructions[3])
    toCol = int(instructions[5])

    for moveCounter in range(numMoves):

        colsToAdd = cols[fromCol-1][-1:]
        cols[fromCol-1] = cols[fromCol-1][:-1]
        cols[toCol-1].extend(colsToAdd)

    return cols

def ExecuteMove2(fileLine, cols):
    instructions = fileLine.strip().split(' ')
    numMoves = int(instructions[1])
    fromCol = int(instructions[3])
    toCol = int(instructions[5])

    colsToAdd = cols[fromCol-1][-numMoves:]
    cols[fromCol-1] = cols[fromCol-1][:-numMoves]
    cols[toCol-1].extend(colsToAdd)

    return cols

def GetLastColStr(cols):
    lastColStr = ''

    for col in cols:
        lastColStr += col[len(col)-1]

    return lastColStr

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

        cols1 = ['V','C','D','R','Z','G','B','W']
        cols2 = ['G','W','F','C','B','S','T','V']
        cols3 = ['C','B','S','N','W']
        cols4 = ['Q','G','M','N','J','V','C','P']
        cols5 = ['T','S','L','F','D','H','B']
        cols6 = ['J','V','T','W','M','N']
        cols7 = ['P','F','L','C','S','T','G']
        cols8 = ['B','D','Z']
        cols9 = ['M','N','Z','W']
    
        cols = [cols1, cols2, cols3, cols4, cols5, cols6, cols7, cols8, cols9]

    """
    cols1 = ['Z','N']
    cols2 = ['M','C','D']
    cols3 = ['P']
    cols = [cols1,cols2,cols3]
    """
    bAtMoves = False
    for fileLine in fileData:
        if fileLine == '\n':
            bAtMoves = True
            continue
        if not bAtMoves:
            continue
        else:
            cols = ExecuteMove(fileLine, cols)

    strCode = GetLastColStr(cols)


    return strCode

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

        cols1 = ['V', 'C', 'D', 'R', 'Z', 'G', 'B', 'W']
        cols2 = ['G', 'W', 'F', 'C', 'B', 'S', 'T', 'V']
        cols3 = ['C', 'B', 'S', 'N', 'W']
        cols4 = ['Q', 'G', 'M', 'N', 'J', 'V', 'C', 'P']
        cols5 = ['T', 'S', 'L', 'F', 'D', 'H', 'B']
        cols6 = ['J', 'V', 'T', 'W', 'M', 'N']
        cols7 = ['P', 'F', 'L', 'C', 'S', 'T', 'G']
        cols8 = ['B', 'D', 'Z']
        cols9 = ['M', 'N', 'Z', 'W']

        cols = [cols1, cols2, cols3, cols4, cols5, cols6, cols7, cols8, cols9]

    """
    cols1 = ['Z','N']
    cols2 = ['M','C','D']
    cols3 = ['P']
    cols = [cols1,cols2,cols3]
    """
    bAtMoves = False
    for fileLine in fileData:
        if fileLine == '\n':
            bAtMoves = True
            continue
        if not bAtMoves:
            continue
        else:
            cols = ExecuteMove2(fileLine, cols)

    strCode = GetLastColStr(cols)

    return strCode

filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day5.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))