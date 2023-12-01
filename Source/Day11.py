from AoCUtilities import *
import ast
import functools
from collections import Counter


class Monkey:
    def __init__(self, startingItems : list, op : str, opVal : str, testDiv : int, evenThrow : int, oddThrow : int ):
        self.Items = startingItems.copy()
        self.Op = op
        self.OpVal = opVal
        self.TestDiv = testDiv
        self.evenThrow = evenThrow
        self.oddThrow = oddThrow

    def AddItem(self, itemToAdd):
        self.Items.append(itemToAdd)

    def ThrowAllItems(self) -> map:
        newMap = {}
        return newMap

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    monkeyList = []

    startingItems = []
    op = ''
    opVal = ''
    testDiv = 1
    evenThrow = 0
    oddThrow = 0


    for fileLine in fileData:
        if fileLine == '\n':
            monkeyList.append(Monkey(startingItems, op, opVal, testDiv, evenThrow, oddThrow))
            continue
        elif fileLine.startswith('Monkey '):
            continue
        elif fileLine.startswith('  Starting items: '):
            strippedFileLine = fileLine.strip().split(': ')[1]
            startingItems = splitIntWithStr(strippedFileLine, ', ')
        elif fileLine.startswith('  Operation: '):
            strippedFileLine = fileLine.strip().split('= old')[1]
            operation = strippedFileLine.split(' ')
            op = operation[1]
            opVal = operation[2]
        elif fileLine.startswith('  Test:'):
            strippedFileLine = fileLine.strip().split('by')[1]
            testDiv = int(strippedFileLine)
        elif fileLine.startswith('    If true:'):
            strippedFileLine = fileLine.strip().split('monkey')[1]
            evenThrow = int(strippedFileLine)
        elif fileLine.startswith('    If false:'):
            strippedFileLine = fileLine.strip().split('monkey')[1]
            oddThrow = int(strippedFileLine)

    currentIndex = 0
    timesToRun = 20
    for index in range(0, 20):
        for monkey in range(0, monkeyList.count()):
            throwMap = monkeyList[monkey].ThrowAllItems()
            throwKeys = throwMap.Keys
    return 0


def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    return 0



filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day11.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))