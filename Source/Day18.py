from AoCUtilities import *
import ast
import functools
from collections import Counter



def GetNeighborCount(cube : tuple, grid : set) -> int:
    left = (-1,0,0)
    right = (1,0,0)
    up = (0,1,0)
    down = (0,-1,0)
    top = (0,0,1)
    bottom = (0,0,-1)

    leftCube = AddXYZ(left, cube)
    rightCube = AddXYZ(right, cube)
    upCube = AddXYZ(up, cube)
    downCube = AddXYZ(down, cube)
    topCube = AddXYZ(top, cube)
    bottomCube = AddXYZ(bottom, cube)

    neighborCount = 0
    if leftCube in grid:
        neighborCount += 1
    if rightCube in grid:
        neighborCount += 1
    if upCube in grid:
        neighborCount += 1
    if downCube in grid:
        neighborCount += 1
    if topCube in grid:
        neighborCount += 1
    if bottomCube in grid:
        neighborCount += 1

    return neighborCount

def IsAirBubble(cube : tuple, grid : set, prevLocs : set, currentDepth : int) -> int:
    if currentDepth > 50:
        return False # Haven't found an outer edge, so stop looking

    prevLocs.add(cube)

    left = (-1,0,0)
    right = (1,0,0)
    up = (0,1,0)
    down = (0,-1,0)
    top = (0,0,1)
    bottom = (0,0,-1)

    leftCube = AddXYZ(left, cube)
    rightCube = AddXYZ(right, cube)
    upCube = AddXYZ(up, cube)
    downCube = AddXYZ(down, cube)
    topCube = AddXYZ(top, cube)
    bottomCube = AddXYZ(bottom, cube)

    if leftCube not in grid and leftCube not in prevLocs:
        if not IsAirBubble(leftCube, grid, prevLocs, currentDepth + 1):
            return False
    if rightCube not in grid and rightCube not in prevLocs:
        if not IsAirBubble(rightCube, grid, prevLocs, currentDepth + 1):
            return False
    if upCube not in grid and upCube not in prevLocs:
        if not IsAirBubble(upCube, grid, prevLocs, currentDepth + 1):
            return False
    if downCube not in grid and downCube not in prevLocs:
        if not IsAirBubble(downCube, grid, prevLocs, currentDepth + 1):
            return False
    if topCube not in grid and topCube not in prevLocs:
        if not IsAirBubble(topCube, grid, prevLocs, currentDepth + 1):
            return False
    if bottomCube not in grid and bottomCube not in prevLocs:
        if not IsAirBubble(bottomCube, grid, prevLocs, currentDepth + 1):
            return False

    return True

def IsAirSurrounded(cube : tuple, grid : set) -> int:
    left = (-1,0,0)
    right = (1,0,0)
    up = (0,1,0)
    down = (0,-1,0)
    top = (0,0,1)
    bottom = (0,0,-1)

    leftCube = AddXYZ(left, cube)
    rightCube = AddXYZ(right, cube)
    upCube = AddXYZ(up, cube)
    downCube = AddXYZ(down, cube)
    topCube = AddXYZ(top, cube)
    bottomCube = AddXYZ(bottom, cube)

    isSurrounded = True
    if leftCube not in grid:
        return False
    if rightCube not in grid:
        return False
    if upCube not in grid:
        return False
    if downCube not in grid:
        return False
    if topCube not in grid:
        return False
    if bottomCube not in grid:
        return False
    return isSurrounded

def GetExposedNeighborCount(cube : tuple, grid : set) -> int:
    left = (-1,0,0)
    right = (1,0,0)
    up = (0,1,0)
    down = (0,-1,0)
    top = (0,0,1)
    bottom = (0,0,-1)

    leftCube = AddXYZ(left, cube)
    rightCube = AddXYZ(right, cube)
    upCube = AddXYZ(up, cube)
    downCube = AddXYZ(down, cube)
    topCube = AddXYZ(top, cube)
    bottomCube = AddXYZ(bottom, cube)

    neighborCount = 0
    if leftCube not in grid and not IsAirBubble(leftCube, grid, set(), 0):
        neighborCount += 1
    if rightCube not in grid and not IsAirBubble(rightCube, grid, set(), 0):
        neighborCount += 1
    if upCube not in grid and not IsAirBubble(upCube, grid, set(), 0):
        neighborCount += 1
    if downCube not in grid and not IsAirBubble(downCube, grid, set(), 0):
        neighborCount += 1
    if topCube not in grid and not IsAirBubble(topCube, grid, set(), 0):
        neighborCount += 1
    if bottomCube not in grid and not IsAirBubble(bottomCube, grid, set(), 0):
        neighborCount += 1

    return neighborCount

def GetExposdeSideCount(cube: tuple, grid : set) -> int:
    return 6 - GetNeighborCount(cube, grid)

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    gridSet = set()

    for fileLine in fileData:
        rowData = fileLine.strip().split(',')
        cube = (int(rowData[0]),int(rowData[1]),int(rowData[2]))
        gridSet.add(cube)

    exposedSides = 0
    for cube in gridSet:
        exposedSides += GetExposdeSideCount(cube, gridSet)


    return exposedSides


def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    gridSet = set()

    for fileLine in fileData:
        rowData = fileLine.strip().split(',')
        cube = (int(rowData[0]),int(rowData[1]),int(rowData[2]))
        gridSet.add(cube)

    exposedSides = 0
    for cube in gridSet:
        exposedSides += GetExposedNeighborCount(cube, gridSet)


    return exposedSides



filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day18.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))