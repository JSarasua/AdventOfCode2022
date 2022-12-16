from AoCUtilities import *
import ast
import functools
from collections import Counter


class IntLine:
    def __init__(self, startPos, endPos):
        self.startPos = startPos
        self.endPos = endPos
        self.m = (endPos[1] - startPos[1])/(endPos[0] - startPos[0])

        #y = mx + b
        x = startPos[0]
        y = startPos[1]
        self.b = y - self.m * x

    def IsParallel(self, line : 'IntLine') -> bool:
        if self.m == line.m:
            return True

    def GetParallelDist(self, line : 'IntLine') -> int:
        return GetDistance(self.b, line.b)

    def GetHigherBParallelLine(self, line : 'IntLine') -> 'IntLine':
        if self.b > line.b:
            return self
        else:
            return line

    def GetIntersection(self, line: 'IntLine') -> tuple: #in the future changing away from tuples would be good
        if self.IsParallel(line):
            return None
        myB = self.b
        theirB = line.b

        #y = x + 1
        #y = -x + 5
        # x = y - 1
        # x = 5 - y
        # y - 1 = 5 - y
        # 2y = 6
        # y = 3

        y = (myB + theirB)/2
        x = (y-myB)/self.m

        return(x,y)

def GetParallelLinesWithDist2( parallelLines : list['IntLine']):
    dist2Lines = []
    for line in parallelLines:
        for otherLine in parallelLines:
            if line == otherLine:
                continue
            dist = line.GetParallelDist(otherLine)
            if dist == 2:
                dist2Lines.append((line, otherLine))
    return dist2Lines

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

def GetPossibleCenterPoints(posLinePairs : list[tuple['IntLine','IntLine']], negLinePairs : list[tuple['IntLine','IntLine']]) -> set:
    centerPoints = set()
    for posLinePair in posLinePairs:
        higherPosLine = posLinePair[0].GetHigherBParallelLine(posLinePair[1])
        for negLinePair in negLinePairs:
            higherNegLine = negLinePair[0].GetHigherBParallelLine(negLinePair[1])
            intPoint = higherPosLine.GetIntersection(higherNegLine)
            centerPoint = (intPoint[0],intPoint[1]-1)
            centerPoints.add(centerPoint)
    return centerPoints

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

    # Ok I'm making a big assumption that the point isn't on the boundary. If so, then come up with another solution!
    # Convert all of the sensor/beacon pairs into two lists of lines. The positive and negative slope lines
    # For each line, look for a line where the gap is 2 between
    # Please for the love of all that is holy be there two of these.
    # Get the intersection point between these lines
    # Ideally I can grab the higher b value of the positive and negative lines and then find their intersection
    # The intersection should by right above the point we're looking for
    #
    # Edge cases to check for if this doesn't work:
    # * There's an intersection between lines right next to the border. The point we're looking for will then be on the border
    # * Theoretically the diamonds created could have all of their points surround the point we're looking for. I don't want to deal with this
    # * Ok and this could easily happen. Currently I'm treating my lines as if they are infinite. THEY ARE NOT. I JUST DON'T WANT TO DEAL WITH IT

    sensors = []
    beacons = []

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

    posLines = []
    negLines = []
    for posLine in blTotR:
        newLine = IntLine(posLine[0], posLine[1])
        posLines.append(newLine)

    for negLine in tLTobR:
        newLine = IntLine(negLine[0], negLine[1])
        negLines.append(newLine)

    dist2PosLines = GetParallelLinesWithDist2(posLines)
    dist2NegLines = GetParallelLinesWithDist2(negLines)

    intersectionPoints = GetPossibleCenterPoints(dist2PosLines, dist2NegLines)

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
