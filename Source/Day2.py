from AoCUtilities import *


def CalcMatchResult(oppMove, yourMove):
    win = 6
    draw = 3
    loss = 0

    if oppMove == 'A':
        if yourMove == 'X':
            return draw
        elif yourMove == 'Y':
            return win
        else:
            return loss
    elif oppMove == 'B':
        if yourMove == 'X':
            return loss
        elif yourMove == 'Y':
            return draw
        else:
            return win
    else:
        if yourMove == 'X':
            return win
        elif yourMove == 'Y':
            return loss
        else:
            return draw

def CalcMoveScore(yourMove):
    if yourMove == 'X':
        return 1
    elif yourMove == 'Y':
        return 2
    else:
        return 3

def CalcResultCode(resultCode):
    win = 6
    draw = 3
    loss = 0

    if resultCode == 'X':
        return loss
    elif resultCode == 'Y':
        return draw
    else:
        return win

def CalcMoveDay2Score(oppMove, yourResult):
    rock = 1
    paper = 2
    scissors = 3

    if oppMove == 'A':
        if yourResult == 'X':
            return scissors
        elif yourResult == 'Y':
            return rock
        else:
            return paper
    elif oppMove == 'B':
        if yourResult == 'X':
            return rock
        elif yourResult == 'Y':
            return paper
        else:
            return scissors
    else:
        if yourResult == 'X':
            return paper
        elif yourResult == 'Y':
            return scissors
        else:
            return rock

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    # A = Rock
    # B = Paper
    # C = Scissors

    # X = Rock
    # Y = Paper
    # Z = Scissors

    # Rock = 1
    # Paper = 2
    # Scissors = 3

    # Loss = 0
    # Draw = 3
    # Win = 6

    scoreSum = 0

    for fileline in fileData:
        moves = fileline.strip().split(' ')
        result = CalcMatchResult(moves[0], moves[1])
        moveScore = CalcMoveScore(moves[1])
        scoreSum += result + moveScore

    return scoreSum



def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    scoreSum = 0
    for fileline in fileData:
        moves = fileline.strip().split(' ')
        result = CalcResultCode(moves[1])
        moveScore = CalcMoveDay2Score(moves[0], moves[1])
        scoreSum += result + moveScore

    return scoreSum

filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day2.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))