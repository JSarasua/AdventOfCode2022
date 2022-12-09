from AoCUtilities import *
from collections import Counter


def MoveHeadTailOne(headTail : tuple[tuple[int,int],tuple[int,int]], dir : tuple[int,int]) -> tuple[tuple[int,int],tuple[int,int]]:
    newHeadPos = AddXY(headTail[0], dir)
    currentTailPos = headTail[1]
    oldHeadPos = headTail[0]
    newTailPos = None


    xDist = newHeadPos[0] - currentTailPos[0]
    yDist = newHeadPos[1] - currentTailPos[1]

    if abs(xDist) > 1 or abs(yDist) > 1:
        newTailPos = oldHeadPos
    else:
        newTailPos = headTail[1]

    newHeadTailPos = (newHeadPos,newTailPos)

    return newHeadTailPos

def MoveHeadOne(headPos : tuple[int,int], dir : tuple[int,int]) -> tuple[int,int]:
    newHeadPos = AddXY(headPos, dir)
    return newHeadPos

def MoveTailOne(headPos : tuple[int,int], oldHeadPos : tuple[int,int], tailPos : tuple[int,int]) -> tuple[int,int]:
    xDist = headPos[0] - tailPos[0]
    yDist = headPos[1] - tailPos[1]

    newX = tailPos[0]
    newY = tailPos[1]

    signX = None
    signY = None

    moveX = 0
    moveY = 0

    if xDist > 0:
        moveX = 1
    elif xDist < 0:
        moveX = -1
    if yDist > 0:
        moveY = 1
    elif yDist < 0:
        moveY = -1

    if abs(xDist) > 1 or abs(yDist) > 1:
        newX += moveX
        newY += moveY

    return (newX, newY)


def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    uniqueTailPos = 1
    tailPosVisited = {(0,0)}
    headPos = (0,0)
    tailPos = (0,0)

    left = (-1,0)
    right = (1,0)
    up = (0,1)
    down = (0,-1)

    headTailPos = (headPos, tailPos)
    for fileLine in fileData:
        instruction = fileLine.strip().split(' ')
        dir = instruction[0]
        num = int(instruction[1])

        stepDir = None
        if dir == 'L':
            stepDir = left
        elif dir == 'R':
            stepDir = right
        elif dir == 'U':
            stepDir = up
        elif dir == 'D':
            stepDir = down
        for step in range(num):
            headTailPos = MoveHeadTailOne(headTailPos, stepDir)
            newTailPos = headTailPos[1]
            tailPosVisited.add(newTailPos)


    return len(tailPosVisited)


def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    uniqueTailPos = 1
    tailPosVisited = {(0,0)}

    left = (-1,0)
    right = (1,0)
    up = (0,1)
    down = (0,-1)

    rope = [(0,0)] * 10

    for fileLine in fileData:
        instruction = fileLine.strip().split(' ')
        dir = instruction[0]
        num = int(instruction[1])

        stepDir = None
        if dir == 'L':
            stepDir = left
        elif dir == 'R':
            stepDir = right
        elif dir == 'U':
            stepDir = up
        elif dir == 'D':
            stepDir = down
        for step in range(num):
            prevKnot = rope[0]
            for knotIndex in range(len(rope)):
                if knotIndex == 0:
                    rope[knotIndex] = MoveHeadOne(rope[knotIndex], stepDir)
                else:
                    newPrevKnot = rope[knotIndex]
                    rope[knotIndex] = MoveTailOne(rope[knotIndex-1], prevKnot, rope[knotIndex])
                    prevKnot = newPrevKnot

            tailPosVisited.add(rope[len(rope)-1])


    return len(tailPosVisited)

filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day9.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))
