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

def splitAscii(word):
    return [ord(char) for char in word]

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

def Make2DStrArray(fileData):
    dataArray = []
    for fileLine in fileData:
        dataArray.append(split(fileLine.strip()))
    return dataArray

def Make2DAsciiArray(fileData):
    dataArray = []
    for fileLine in fileData:
        dataArray.append(splitAscii(fileLine.strip()))
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
    for rowIndex in range(0, rowLen):
        list.append(MakeListInitialVal(colLen, initialVal))

    return list

def FindValIn2DList(list, val):
    for rowIndex in range(len(list)):
        for colIndex in range(len(list[rowIndex])):
            valToCheck = list[rowIndex][colIndex]
            if val == valToCheck:
                return (colIndex,rowIndex)

    return None

def FindAllIn2DList(list : list, val):
    currentList = []

    for rowIndex in range(len(list)):
        for colIndex in range(len(list[rowIndex])):
            valToCheck = list[rowIndex][colIndex]
            if val == valToCheck:
                currentList.append((colIndex,rowIndex))

    return currentList

def AddXY(a,b):
    c = (a[0] + b[0], a[1] + b[1])
    return c

def MulXY(a,b):
    c = (a[0] * b[0], a[1] * b[1])
    return c

def Print2DStrListSeparator(list, separator : str):
    for line in list:
        lineStr = ListToStringSeparator(line, separator)
        print(lineStr)

def Print2DStrList(list):
    for line in list:
        lineStr = ListToString(line)
        print(lineStr)

def Print2DStrListReversed(list):
    for line in reversed(list):
        lineStr = ListToString(line)
        print(lineStr)

def ListToStringSeparator(list:list, separator : str):
    return separator.join(map(str,list))

def ListToString(list:list):
    return ''.join(map(str,list))