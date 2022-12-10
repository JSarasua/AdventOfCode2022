from AoCUtilities import *
from collections import Counter



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

    return 0

filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day10.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))
