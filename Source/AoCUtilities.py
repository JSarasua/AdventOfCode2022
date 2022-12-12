import statistics
from collections import Counter

#For all days
def print_count(countValue):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Total Count: {countValue}')  # Press Ctrl+F8 to toggle the breakpoint.

def split(word):
    return [char for char in word]

def splitInt(word):
    return [int(char) for char in word]

def IsValidIndex( listToCheck:list, index):
    if 0 <= index < len(listToCheck):
        return True
    return False

def IsValidCoordinate( listToCheck, rowIndex, colIndex):
    if IsValidIndex(listToCheck, rowIndex):
        if IsValidIndex(listToCheck[rowIndex], colIndex):
            return True
    return False

def IsValidCoordinateTuple( listToCheck, xyTuple:tuple):
    return IsValidCoordinate(listToCheck, xyTuple[1], xyTuple[0])

def GetValAtCoordinate( list:list, xy:tuple):
    return list[xy[1]][xy[0]]

def SetValAtCoordinate( list:list, xy:tuple, val):
    list[xy[1]][xy[0]] = val
    return

def GetCharacterCount(char, wordList):
    charCount = 0
    for word in wordList:
        count = Counter(word)
        if count[char] > 0:
            charCount += 1
    return charCount

def Make2DDataArray(fileData):
    dataArray = []
    for fileLine in fileData:
        dataArray.append(splitInt(fileLine.strip()))

    return dataArray

def AddCountToDict(dict:dict, key, count):
    if key in dict.keys():
        dict[key] += count
    else:
        dict[key] = count

def MakeListInitialVal(length, initialVal):
    list = [initialVal] * length
    return list

def Make2DList(rowLen, colLen, initialVal):
    list = []
    for colIndex in range(0, colLen):
        list.append(MakeListInitialVal(rowLen, initialVal))

    return list

def Print2DStrList(list):
    for line in list:
        lineStr = ListToString(line)
        print(lineStr)

def Print2DStrListReversed(list):
    for line in reversed(list):
        lineStr = ListToString(line)
        print(lineStr)

def AddXY(a,b):
    c = (a[0] + b[0], a[1] + b[1])
    return c

def MulXY(a,b):
    c = (a[0] * b[0], a[1] * b[1])
    return c

def ListToString(list:list):
    return ''.join(map(str,list))