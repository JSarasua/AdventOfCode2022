from AoCUtilities import *
from collections import Counter


def GetAdjacentLocations(dataArray : list, xy : tuple):
    up = (0,1)
    down = (0,-1)
    left = (-1,0)
    right = (1,0)

    upCoord = AddXY(xy, up)
    downCoord = AddXY(xy, down)
    leftCoord = AddXY(xy, left)
    rightCoord = AddXY(xy, right)

    adjacentLocs = []

    if IsValidCoordinateTuple(dataArray, upCoord):
        adjacentLocs.append(upCoord)
    if IsValidCoordinateTuple(dataArray, downCoord):
        adjacentLocs.append(downCoord)
    if IsValidCoordinateTuple(dataArray, leftCoord):
        adjacentLocs.append(leftCoord)
    if IsValidCoordinateTuple(dataArray, rightCoord):
        adjacentLocs.append(rightCoord)

    return adjacentLocs

def IsReachable(dataArray : list, startLoc : tuple, endLoc : tuple):
    startVal = GetValAtCoordinate(dataArray, startLoc)
    endVal = GetValAtCoordinate(dataArray, endLoc)
    if endVal <= startVal + 1:
        return True
    return False

def IsReachableReversed(dataArray : list, startLoc : tuple, endLoc : tuple):
    startVal = GetValAtCoordinate(dataArray, startLoc)
    endVal = GetValAtCoordinate(dataArray, endLoc)
    if startVal <= endVal + 1:
        return True
    return False


def AddHeatToPos(dataArray : list, heatMap : list, currentNextLocations : set):
    startLocation = currentNextLocations.pop()
    currentHeatVal = GetValAtCoordinate(heatMap,startLocation)

    adjacentLocs = GetAdjacentLocations(dataArray, startLocation)

    nextHeatVal = currentHeatVal + 1
    for loc in adjacentLocs:
        if IsReachable(dataArray, startLocation, loc):
            heatValAtCoord = GetValAtCoordinate(heatMap, loc)
            if heatValAtCoord == None or heatValAtCoord > nextHeatVal:
                SetValAtCoordinate(heatMap, loc, nextHeatVal)
                currentNextLocations.add(loc)

def AddHeatToPosReversed(dataArray : list, heatMap : list, currentNextLocations : set):
    startLocation = currentNextLocations.pop()
    currentHeatVal = GetValAtCoordinate(heatMap,startLocation)

    adjacentLocs = GetAdjacentLocations(dataArray, startLocation)

    nextHeatVal = currentHeatVal + 1
    for loc in adjacentLocs:
        if IsReachableReversed(dataArray, startLocation, loc):
            heatValAtCoord = GetValAtCoordinate(heatMap, loc)
            if heatValAtCoord == None or heatValAtCoord > nextHeatVal:
                SetValAtCoordinate(heatMap, loc, nextHeatVal)
                currentNextLocations.add(loc)

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    dataArray = Make2DAsciiArray(fileData)

    start = ord('S')
    end = ord('E')
    startPos = FindValIn2DList(dataArray,start)
    endPos = FindValIn2DList(dataArray,end)

    rowLen = len(dataArray)
    colLen = len(dataArray[0])
    heatMap = Make2DList(rowLen, colLen, None)


    SetValAtCoordinate(dataArray, startPos, ord('a'))
    SetValAtCoordinate(dataArray, endPos, ord('z'))
    SetValAtCoordinate(heatMap, startPos, 0)
    currentNextLocations = {startPos}

    while(len(currentNextLocations) > 0):
        AddHeatToPos(dataArray, heatMap, currentNextLocations)


    #Print2DStrListSeparator(dataArray, ',')
    #Print2DStrListSeparator(heatMap, ',')

    endHeat = GetValAtCoordinate(heatMap, endPos)
    return endHeat


def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    dataArray = Make2DAsciiArray(fileData)

    start = ord('S')
    end = ord('E')
    startPos = FindValIn2DList(dataArray,start)
    endPos = FindValIn2DList(dataArray,end)

    rowLen = len(dataArray)
    colLen = len(dataArray[0])
    heatMap = Make2DList(rowLen, colLen, None)


    SetValAtCoordinate(dataArray, startPos, ord('a'))
    SetValAtCoordinate(dataArray, endPos, ord('z'))
    SetValAtCoordinate(heatMap, endPos, 0)
    currentNextLocations = {endPos}

    while(len(currentNextLocations) > 0):
        AddHeatToPosReversed(dataArray, heatMap, currentNextLocations)


    Print2DStrListSeparator(dataArray, ',')
    Print2DStrListSeparator(heatMap, ',')

    allAs = FindAllIn2DList(dataArray, ord('a'))

    lowestHeatA = allAs[0]
    lowestHeatVal = GetValAtCoordinate(heatMap, lowestHeatA)

    for a in allAs:
        currentHeatVal = GetValAtCoordinate(heatMap, a)
        if currentHeatVal != None and currentHeatVal < lowestHeatVal:
            lowestHeatA = a
            lowestHeatVal = currentHeatVal

    return lowestHeatVal

filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day12.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))
