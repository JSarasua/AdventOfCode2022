from AoCUtilities import *
import ast
import functools
from collections import Counter

def ExpandRange(minPos, maxPos, newPos):
    if minPos == None:
        minPos = newPos
    if maxPos == None:
        maxPos = newPos

    newMinX = minPos[0]
    newMinY = minPos[1]
    newMaxX = maxPos[0]
    newMaxY = maxPos[1]

    if newPos[0] < minPos[0]:
        newMinX = newPos[0]
    if newPos[1] < minPos[1]:
        newMinY = newPos[1]
    if newPos[0] > maxPos[0]:
        newMaxX = newPos[0]
    if newPos[1] > maxPos[1]:
        newMaxY = newPos[1]

    minPos = (newMinX, newMinY)
    maxPos = (newMaxX, newMaxY)
    return minPos, maxPos

def AddRestrictions(sensorPos, beaconPos, restrictedLocations : set, colNum):
    maxDist = GetManhattanDist(sensorPos, beaconPos)

    closestPoint = (sensorPos[0], colNum)
    currentPointLeft = closestPoint
    currentPointRight = closestPoint

    while GetManhattanDist(sensorPos,  currentPointLeft) <=maxDist:
        restrictedLocations.add(currentPointLeft)
        currentPointLeft = (currentPointLeft[0]-1,colNum)

    while GetManhattanDist(sensorPos,  currentPointRight) <= maxDist:
        restrictedLocations.add(currentPointRight)
        currentPointRight = (currentPointRight[0]+1,colNum)

    if beaconPos in restrictedLocations:
        restrictedLocations.remove(beaconPos)

def AddLinesToLists(bLTotR : list, tLTobR : list, sensorPos : tuple, beaconPos : tuple):
    dist = GetManhattanDist(sensorPos, beaconPos)
    minX = sensorPos[0] - dist
    maxX = sensorPos[0] + dist
    minY = sensorPos[1] - dist
    maxY = sensorPos[1] + dist

    leftPoint = (minX, sensorPos[1])
    rightPoint = (maxX, sensorPos[1])
    topPoint = (sensorPos[0], maxY)
    bottomPoint = (sensorPos[0], minY)

    bLTotR.append((leftPoint,topPoint))
    bLTotR.append((bottomPoint,rightPoint))
    tLTobR.append((leftPoint,bottomPoint))
    tLTobR.append((topPoint,rightPoint))

    return

def FindLinesWithDist2(parallelLines : list) -> set:
    dist2Lines = set()

    for line in parallelLines:
        point1 = line[0]
        yMinusX = point1[1] - point1[0]
        for otherLine in parallelLines:
            point2 = otherLine[0]
            otherYMinusX = point2[1] - point2[0]
            dist = GetDistance(yMinusX, otherYMinusX)
            if dist == 2:
                dist2Lines.add((line,otherLine))
    return dist2Lines

def FindNegLinesWithDist2(parallelLines : list) -> set:
    dist2Lines = set()

    for line in parallelLines:
        point1 = line[0]
        yPlusX = point1[1] + point1[0]
        for otherLine in parallelLines:
            point2 = otherLine[0]
            otherYPlusX = point2[1] + point2[0]
            dist = GetDistance(yPlusX, otherYPlusX)
            if dist == 2:
                dist2Lines.add((line,otherLine))
    return dist2Lines

def GetIntersectionBetweenLines( line1 : tuple, line2 : tuple):
    #y=x+b
    point1 = line1[0]
    b = point1[1] - point1[0]

    point2 = line2[0]
    negB = point2[1] + point2[0]

    y = (negB - b) / 2
    x = y - b

    return(x,y)


def GetPossibleCenterPoint(posLines : tuple, negLines : tuple):
    highestPosB = -9999999999
    highestNegB = -9999999999

    for posLine in posLines:
        point1 = posLine[0]
        b = point1[1] - point1[0]
        if b > highestPosB:
            highestPosB = b

    for negLine in negLines:
        point1 = negLine[0]
        b = point1[1] + point1[0]
        if b > highestNegB:
            highestNegB = b

    y = (highestNegB - highestPosB) / 2
    x = y - highestPosB
    return (x, y-1)



def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    sensors = []
    beacons = []

    minPos = None
    maxPos = None

    for fileLine in fileData:
        lineSplit = fileLine.strip().split('Sensor at ')[1].split(': closest beacon is at ')
        sensorLine = lineSplit[0].split('x=')[1].split(', y=')
        beaconLine = lineSplit[1].split('x=')[1].split(', y=')

        sensorPos = (int(sensorLine[0]), int(sensorLine[1]))
        beaconPos = (int(beaconLine[0]), int(beaconLine[1]))
        sensors.append(sensorPos)
        beacons.append(beaconPos)
        minPos, maxPos = ExpandRange(minPos, maxPos, sensorPos)
        minPos, maxPos = ExpandRange(minPos, maxPos, beaconPos)

    restrictedLocations = set()

    for index in range(len(sensors)):
        AddRestrictions(sensors[index], beacons[index], restrictedLocations, 2000000)

    return len(restrictedLocations)


def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    sensors = []
    beacons = []

    # Ok I'm making a big assumption that the point isn't on the boundary. If so, then come up with another solution!
    # Convert all of the sensor/beacon pairs into two lists of lines. The bottom left to top right and top right to bottom left
    # For each line, look for a line where the gap is 1 between
    # Please for the love of all that is holy be there two of these.
    # Get the intersection point between these points
    # Look at the data and hope you got your answer
    blTotR = []
    tLTobR = []

    for fileLine in fileData:
        lineSplit = fileLine.strip().split('Sensor at ')[1].split(': closest beacon is at ')
        sensorLine = lineSplit[0].split('x=')[1].split(', y=')
        beaconLine = lineSplit[1].split('x=')[1].split(', y=')

        sensorPos = (int(sensorLine[0]), int(sensorLine[1]))
        beaconPos = (int(beaconLine[0]), int(beaconLine[1]))
        sensors.append(sensorPos)
        beacons.append(beaconPos)
        AddLinesToLists(blTotR, tLTobR, sensorPos, beaconPos)
    # Looking for two sets of parallel lines

    blLinesWithDis2 = FindLinesWithDist2(blTotR)
    tLLinesWithDis2 = FindNegLinesWithDist2(tLTobR)

    intersectionPoints = set()
    for blLine in blLinesWithDis2:
        for tlLine in tLLinesWithDis2:
            point = GetPossibleCenterPoint(blLine, tlLine)
            intersectionPoints.add(point)

    for intersectionPoint in intersectionPoints:
        print(intersectionPoint)

    for point in intersectionPoints:
        x = point[0] * 4000000
        y = point[1]
        xy = x + y
        print(xy)



    return 0


filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day15.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))
