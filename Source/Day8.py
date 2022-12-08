from AoCUtilities import *
from collections import Counter

def IsValueGreaterThanList(val : int, ls : list[int]) -> bool:
    isGreater = True
    for index in ls:
        if index >= val:
            isGreater = False
            break
    return isGreater

def GetCol(dataArray : list[list[int]], rowIndex):
    row = []
    for col in dataArray:
        row.append(col[rowIndex])
    return row

def GetTreeVisCount(val : int, ls : list[int]) -> int:
    numTrees = 0
    for elem in reversed(ls):
        numTrees += 1
        if elem >= val:
            break
    return numTrees

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    visibleTrees = 0
    dataArray = Make2DDataArray(fileData)
    for rowIndex in range(len(dataArray)):
        for colIndex in range(len(dataArray[rowIndex])):
            if rowIndex == 0 or rowIndex == len(dataArray) - 1:
                visibleTrees += 1
                continue

            col = GetCol(dataArray, colIndex)
            row = dataArray[rowIndex]

            if colIndex == 0 or colIndex == len(row)-1:
                visibleTrees += 1
                continue
            val = row[colIndex]

            prevCol = row[0:colIndex]
            if IsValueGreaterThanList(val, prevCol):
                visibleTrees += 1
                continue
            nextCol = row[colIndex+1:len(col)]
            if IsValueGreaterThanList(val, nextCol):
                visibleTrees += 1
                continue
            prevRow = col[0:rowIndex]
            if IsValueGreaterThanList(val, prevRow):
                visibleTrees += 1
                continue
            nextRow = col[rowIndex+1:len(col)]
            if IsValueGreaterThanList(val, nextRow):
                visibleTrees += 1
                continue

    return visibleTrees


def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    bestVisibilityScore = 0
    dataArray = Make2DDataArray(fileData)
    for rowIndex in range(len(dataArray)):
        leftTreeCount = 0
        rightTreeCount = 0
        upTreeCount = 0
        downTreeCount = 0

        for colIndex in range(len(dataArray[rowIndex])):
            if rowIndex == 0 or rowIndex == len(dataArray) - 1:
                continue

            col = GetCol(dataArray, colIndex)
            row = dataArray[rowIndex]

            if colIndex == 0 or colIndex == len(row)-1:
                continue

            val = row[colIndex]
            prevCol = row[0:colIndex]
            leftTreeCount = GetTreeVisCount(val, prevCol)
            nextCol = row[colIndex + 1:len(col)]
            nextCol = nextCol[::-1]
            rightTreeCount = GetTreeVisCount(val, nextCol)
            prevRow = col[0:rowIndex]
            upTreeCount = GetTreeVisCount(val, prevRow)
            nextRow = col[rowIndex + 1:len(col)]
            nextRow = nextRow[::-1]
            downTreeCount = GetTreeVisCount(val, nextRow)
            treeVisVal = leftTreeCount * rightTreeCount * upTreeCount * downTreeCount

            if treeVisVal > bestVisibilityScore:
                bestVisibilityScore = treeVisVal


    return bestVisibilityScore

filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day8.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))
