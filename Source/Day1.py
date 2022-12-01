from AoCUtilities import *


def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    currentScore = 0
    bestScore = 0

    for fileline in fileData:
        if fileline == "\n":
            if currentScore > bestScore:
                bestScore = currentScore
            currentScore = 0
        else:
            currentScore += int(fileline)

    return bestScore



def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    currentScore = 0
    bestScore = 0
    secondBestScore = 0
    thirdBestScore = 0

    for fileline in fileData:
        if fileline == "\n":
            if currentScore > bestScore:
                thirdBestScore = secondBestScore
                secondBestScore = bestScore
                bestScore = currentScore
            elif currentScore > secondBestScore:
                thirdBestScore = secondBestScore
                secondBestScore = currentScore
            elif currentScore > thirdBestScore:
                thirdBestScore = currentScore
            currentScore = 0
        else:
            currentScore += int(fileline)

    return bestScore + secondBestScore + thirdBestScore

filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day1.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))