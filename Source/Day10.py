from AoCUtilities import *
from collections import Counter

def IsPixelLit(cycle:int, register:int) -> bool:
    if register <= cycle and register+2 >= cycle:
        return True
    return False

def SetPixelOnScreen(screen : list, cycle : int, char : str):
    index = cycle - 1
    row = index // 40
    col = index % 40

    screen[row][col] = char


def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    currentCycle = 1
    register = 1
    signalStrength = 0

    cycleToCheck = 20
    cycleIncrement = 40
    maxCycleToCheck = 220

    for fileLine in fileData:
        op = fileLine.strip().split(' ')
        opsToDo = 0
        valToAdd = 0
        if op[0] == 'noop':
            opsToDo = 1
        elif op[0] == 'addx':
            opsToDo = 2
            valToAdd = int(op[1])

        for val in range(opsToDo):
            if currentCycle == cycleToCheck:
                signalStrength += currentCycle * register
                if cycleToCheck >= maxCycleToCheck:
                    return signalStrength
                cycleToCheck += cycleIncrement
            currentCycle += 1
        register += valToAdd

    return 0


def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    currentCycle = 1
    register = 1

    cycleToCheck = 20
    cycleIncrement = 40
    maxCycleToCheck = 220

    screen2D = [['.' for col in range(40)] for row in range(6)]

    for fileLine in fileData:
        op = fileLine.strip().split(' ')
        opsToDo = 0
        valToAdd = 0
        if op[0] == 'noop':
            opsToDo = 1
        elif op[0] == 'addx':
            opsToDo = 2
            valToAdd = int(op[1])

        for val in range(opsToDo):
            charToSet = '.'
            if IsPixelLit(currentCycle % 40, register):
                charToSet = '#'
            SetPixelOnScreen(screen2D, currentCycle, charToSet)
            if val == opsToDo - 1:
                register += valToAdd
            currentCycle += 1


    Print2DStrList(screen2D)

    return 0

filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day10.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))
