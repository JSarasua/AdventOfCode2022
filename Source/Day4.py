from AoCUtilities import *
from collections import Counter

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    fullyContainedPairs = 0

    for fileLine in fileData:
        elfPairs = fileLine.strip().split(',')
        section1 = [int(x) for x in elfPairs[0].split('-')]
        section2 = [int(x) for x in elfPairs[1].split('-')]

        if section1[0] <= section2[0] and section1[1] >= section2[1]:
            fullyContainedPairs += 1
        elif section2[0] <= section1[0] and section2[1] >= section1[1]:
            fullyContainedPairs += 1

    return fullyContainedPairs



def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    overlappingPairs = 0

    for fileLine in fileData:
        elfPairs = fileLine.strip().split(',')
        section1 = [int(x) for x in elfPairs[0].split('-')]
        section2 = [int(x) for x in elfPairs[1].split('-')]

        if section1[0] <= section2[0] and section1[1] >= section2[0]:
            overlappingPairs += 1
        elif section2[0] <= section1[0] and section2[1] >= section1[0]:
            overlappingPairs += 1
        elif section1[0] <= section2[1] and section1[1] >= section2[1]:
            overlappingPairs += 1
        elif section2[0] <= section1[1] and section2[1] >= section1[1]:
            overlappingPairs += 1

    return overlappingPairs

filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day4.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))