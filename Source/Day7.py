from AoCUtilities import *
from collections import Counter
from enum import Enum

class LineMode(Enum):
    ChangeDir = 1
    ListDir = 2

class Directory:
    def __init__(self, newDirName, newPrevDir):
        self.dirName = newDirName
        self.prevDir = newPrevDir
        self.dirs = []
        self.files = {}

    def copy(self):
        newDir = Directory(self.dirName, self.prevDir)
        newDir.dirs = self.dirs.copy()
        newDir.files = self.files.copy()
        return newDir

    def GetDirs(self):
        return self.dirs

    def GetPrevDir(self):
        return self.prevDir

    def HasPrevDir(self):
        return self.prevDir != ''

    def AddDir(self, newDir):
        self.dirs.append(newDir)

    def AddFile(self, fileName, fileSize):
        self.files[fileName] = fileSize

    def GetDirSize(self):
        dirSize = 0
        for key, value in self.files.items():
            dirSize += int(value)
        return dirSize

    def GetDirSizeRecursive(self, dirDict : dict):
        currentDirSize = self.GetDirSize()
        for dir in self.dirs:
            currentDirSize += dirDict[dir].GetDirSizeRecursive(dirDict)
        return currentDirSize

    dirName = ''
    prevDir = ''
    dirs = []
    files = {}

def GetLastColStr(cols):
    lastColStr = ''

    for col in cols:
        lastColStr += col[len(col)-1]

    return lastColStr

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    dirDict = {}

    currentDirName = ''
    currentDir = Directory('','')

    #LineMode currentMode = LineMode()

    for fileLine in fileData:
        lineData = fileLine.strip().split(' ')
        if lineData[0] == '$':
            if lineData[1] == 'cd': #Still need to handle cd ..
                if currentDirName == '':
                    currentDirName = lineData[2]
                    if currentDirName in dirDict.keys():
                        currentDir = dirDict[currentDirName].copy()
                    else:
                        currentDir = Directory(currentDirName, '')
                elif lineData[2] == '..':
                    newDirName = currentDir.GetPrevDir()
                    if newDirName == '':
                        continue
                    currentDir = dirDict[newDirName].copy()
                    currentDirName = newDirName
                else:
                    prevDir = currentDirName
                    currentDirName = lineData[2]
                    if currentDirName in dirDict.keys():
                        currentDir = dirDict[currentDirName].copy()
                    else:
                        newDir = Directory(currentDirName, prevDir)
                        currentDir = newDir.copy()
                dirDict[currentDirName] = currentDir.copy()

            elif lineData[1] == 'ls':
                #currentMode = LineMode.ListDir
                continue
        elif lineData[0] == 'dir':
            currentDir.AddDir(lineData[1])
            dirDict[currentDirName] = currentDir.copy()
        else:
            currentDir.AddFile(lineData[1], lineData[0])
            dirDict[currentDirName] = currentDir.copy()

    sumOfSizes = 0
    for key, value in dirDict.items():
        currentSize = value.GetDirSizeRecursive(dirDict)
        if currentSize < 100000:
            sumOfSizes += currentSize
    return sumOfSizes

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    return 0

filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day7.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))