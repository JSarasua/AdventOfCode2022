from AoCUtilities import *
import ast
import functools
from collections import Counter

def TryAddSand(list : list) -> bool:
    currentSpot = (500,0)
    lastSpot = None
    maxIter = 500
    while lastSpot != currentSpot:
        if currentSpot[1] >= maxIter:
            return False
        lastSpot = currentSpot

        nextSpot = (currentSpot[0], currentSpot[1] + 1)
        if nextSpot not in list:
            currentSpot = nextSpot
            continue
        nextSpot = (currentSpot[0] - 1, currentSpot[1] + 1)
        if nextSpot not in list:
            currentSpot = nextSpot
            continue
        nextSpot = (currentSpot[0] + 1, currentSpot[1] + 1)
        if nextSpot not in list:
            currentSpot = nextSpot
            continue


    if currentSpot not in list:
        list.append(currentSpot)
        return True
    return False

def TryAddSand2(list: list, highestYPoint: int) -> bool:
    currentSpot = (500, 0)
    lastSpot = None

    highestYPoint += 1

    while lastSpot != currentSpot:
        lastSpot = currentSpot

        if currentSpot[1] == highestYPoint:
            break

        nextSpot = (currentSpot[0], currentSpot[1] + 1)
        if nextSpot not in list:
            currentSpot = nextSpot
            continue
        nextSpot = (currentSpot[0] - 1, currentSpot[1] + 1)
        if nextSpot not in list:
            currentSpot = nextSpot
            continue
        nextSpot = (currentSpot[0] + 1, currentSpot[1] + 1)
        if nextSpot not in list:
            currentSpot = nextSpot
            continue

    if currentSpot == (500,0):
        return False

    if currentSpot not in list:
        list.append(currentSpot)
        return True
    return True

def AddLinesToList(list : list, pointsInLine : list):
    firstPoint = None
    secondPoint = None

    for point in pointsInLine:
        if point not in list:
            list.append(point)

        if firstPoint == None:
            firstPoint = point
        elif secondPoint == None:
            secondPoint = point

        if firstPoint != None and secondPoint != None:
            fX = firstPoint[0]
            fY = firstPoint[1]
            sX = secondPoint[0]
            sY = secondPoint[1]

            xDiff = firstPoint[0] - secondPoint[0]
            yDiff = firstPoint[1] - secondPoint[1]

            if xDiff > 0:
                for x in range(sX,fX):
                    newPoint = (x,fY)
                    if newPoint not in list:
                        list.append(newPoint)
            elif xDiff < 0:
                for x in range(fX,sX):
                    newPoint = (x,fY)
                    if newPoint not in list:
                        list.append(newPoint)
            elif yDiff > 0:
                for y in range(sY,fY):
                    newPoint = (fX,y)
                    if newPoint not in list:
                        list.append(newPoint)
            elif yDiff < 0:
                for y in range(fY, sY):
                    newPoint = (fX, y)
                    if newPoint not in list:
                        list.append(newPoint)
            firstPoint = secondPoint
            secondPoint = None

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    walls = []
    for fileLine in fileData:
        vertices = [vertex for vertex in fileLine.strip().split(' -> ')]
        points = []
        for vertex in vertices:
            pointList = vertex.split(',')
            point = (int(pointList[0]),int(pointList[1]))
            points.append(point)

        AddLinesToList(walls, points)

    currentSand = 0
    while True:
        didAddSand = TryAddSand(walls)
        if didAddSand:
             currentSand += 1
        else:
            break

    return currentSand


def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    walls = []
    for fileLine in fileData:
        vertices = [vertex for vertex in fileLine.strip().split(' -> ')]
        points = []
        for vertex in vertices:
            pointList = vertex.split(',')
            point = (int(pointList[0]),int(pointList[1]))
            points.append(point)

        AddLinesToList(walls, points)


    highestY = 0
    for x,y in walls:
        if y > highestY:
            highestY = y
    currentSand = 0
    while True:
        didAddSand = TryAddSand2(walls, highestY)
        if didAddSand:
             currentSand += 1
        else:
            break

    return currentSand + 1


filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day14.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))
