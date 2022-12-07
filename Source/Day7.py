from AoCUtilities import *
from collections import Counter

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

    def GetName(self) -> str:
        return self.dirName

    def GetDirs(self) -> list['Directory']:
        return self.dirs

    def GetDir(self, dirName) -> 'Directory':
        for dir in self.dirs:
            if dir.dirName == dirName:
                return dir
        return None

    def GetPrevDir(self):
        return self.prevDir

    def HasPrevDir(self):
        return self.prevDir != ''

    def AddDir(self, newDir):
        self.dirs.append(newDir)

    def AddFile(self, fileName, fileSize):
        self.files[fileName] = fileSize

    def ContainsDir(self, dirName: str):
        for dir in self.dirs:
            if dir.dirName == dirName:
                return True
        return False

    def GetDirSize(self):
        dirSize = 0
        for key, value in self.files.items():
            dirSize += int(value)
        return dirSize

    def GetDirSizeRecursive(self):
        currentDirSize = self.GetDirSize()
        for dir in self.dirs:
            currentDirSize += dir.GetDirSizeRecursive()
        return currentDirSize

    dirName = ''
    prevDir = None
    dirs = []
    files = {}


def GetLastColStr(cols):
    lastColStr = ''

    for col in cols:
        lastColStr += col[len(col) - 1]

    return lastColStr


def TraverseDirectory(rootDir: 'Directory'):
    totalSum = 0
    currentSize = rootDir.GetDirSizeRecursive()
    if currentSize < 100000:
        totalSum += currentSize

    for dir in rootDir.dirs:
        totalSum += TraverseDirectory(dir)
    return totalSum


def GetLowestFileSizeOverMin(rootDir: 'Directory', minFileSize):
    currentBestFileSize = -1

    dirSize = rootDir.GetDirSizeRecursive()

    if dirSize > minFileSize:
        currentBestFileSize = dirSize

    for dir in rootDir.dirs:
        bestFileSize = GetLowestFileSizeOverMin(dir, minFileSize)
        if bestFileSize > minFileSize and bestFileSize < currentBestFileSize:
            currentBestFileSize = bestFileSize

    return currentBestFileSize


def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    rootDir = None
    currentDirName = ''
    currentDir = Directory('', None)

    # LineMode currentMode = LineMode()

    for fileLine in fileData:
        lineData = fileLine.strip().split(' ')
        if lineData[0] == '$':
            if lineData[1] == 'cd':
                if currentDirName == '':
                    currentDirName = lineData[2]
                    currentDir = Directory(currentDirName, None)
                    rootDir = currentDir

                elif lineData[2] == '..':
                    currentDir = currentDir.GetPrevDir()
                    currentDirName = currentDir.GetName()
                else:
                    currentDir = currentDir.GetDir(lineData[2])
                    currentDirName = currentDir.GetName()

            elif lineData[1] == 'ls':
                # currentMode = LineMode.ListDir
                continue
        elif lineData[0] == 'dir':
            newDir = Directory(lineData[1], currentDir)
            currentDir.AddDir(newDir)
        else:
            currentDir.AddFile(lineData[1], lineData[0])

    sumOfSizes = TraverseDirectory(rootDir)
    return sumOfSizes


def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    rootDir = None
    currentDirName = ''
    currentDir = Directory('', None)

    # LineMode currentMode = LineMode()

    for fileLine in fileData:
        lineData = fileLine.strip().split(' ')
        if lineData[0] == '$':
            if lineData[1] == 'cd':
                if currentDirName == '':
                    currentDirName = lineData[2]
                    currentDir = Directory(currentDirName, None)
                    rootDir = currentDir

                elif lineData[2] == '..':
                    currentDir = currentDir.GetPrevDir()
                    currentDirName = currentDir.GetName()
                else:
                    currentDir = currentDir.GetDir(lineData[2])
                    currentDirName = currentDir.GetName()

            elif lineData[1] == 'ls':
                # currentMode = LineMode.ListDir
                continue
        elif lineData[0] == 'dir':
            newDir = Directory(lineData[1], currentDir)
            currentDir.AddDir(newDir)
        else:
            currentDir.AddFile(lineData[1], lineData[0])

    totalSpace = 70000000
    neededSpace = 30000000

    usedSpace = rootDir.GetDirSizeRecursive()
    currentUnusedSpace = totalSpace - usedSpace
    spaceToFreeUp = neededSpace - currentUnusedSpace

    lowestSizeOverMin = GetLowestFileSizeOverMin(rootDir, spaceToFreeUp)
    return lowestSizeOverMin


filePath = "C:\\dev\\AdventOfCode2022\\Input\\Day7.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))
