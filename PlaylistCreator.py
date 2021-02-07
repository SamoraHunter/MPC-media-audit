
from operator import itemgetter

import os

playlistDirectory = 'C:\\Users\\Artemis\\SK\\32\\33'



def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)


    return allFiles



def buildFileNameFileSize():
    directory = playlistDirectory

    ls = getListOfFiles(directory)

    nameSizeList = []

    for i in range(0, len(ls)):
        try:

            nameSizeList.append((ls[i], os.stat(ls[i]).st_size / 1000, os.stat(ls[i]).st_atime))

        except:
            pass
            # print("Failed to add : " + ls[i])
    # print("Built filenamesize")
    # print(len(nameSizeList))

    return nameSizeList


def cleanupSortedList(slist):
    newList = []

    for i in range(0, len(slist)):
        if(slist[i][1 ] >25000 and not slist[i][0].endswith('Zip"') and not slist[i][0].endswith('rar"') and not slist[i][0].endswith('pdf"') and len(slist[i][0] ) >0):
            # print(slist[i][0])
            newList.append(slist[i])
    print("Cleaned up:")
    print(len(newList))
    return newList

def getSortedList(OneForSizeTwoForAccessed):
    global OSTA
    OSTA = OneForSizeTwoForAccessed
    a = buildFileNameFileSize()  # True == sort by last access, false for size
    sortedlist = sorted(a, key=itemgetter(OneForSizeTwoForAccessed))
    if(OSTA == 1):
        sortedlist.reverse()
    # print(sortedlist[0])
    print("Sorted")
    print(len(sortedlist))

    return sortedlist


def writeMPCPlaylist(list):
    writeNewLine('MPCPLAYLIST')

    # for each line in the list
    print("Writing " + str(len(list)) + " lines")
    for i in range(1, len(list)):
        testString = list[i][0]
        if (len(testString) > 0):
            try:
                writeNewLine(str(i) + ',type,0')
            except:
                continue
            try:
                writeNewLine(str(i) + ',filename,' + list[i][0])
            except:

                # writeNewLine(str(i) + ',filename,' + list[i][0].encode('utf8'))

                continue
            # print("Failed To add, char prob?")

def writeNewLine(line):
    if (OSTA == 2):

        file_path = playlistDirectory+"\\customAcc.mpcpl"

    elif (OSTA == 1):
        file_path = playlistDirectory+"\\customSize.mpcpl"

    with open(file_path, 'a', encoding='utf8') as file:
        file.write(line + "\n")


file_path = playlistDirectory+"\\customAcc.mpcpl"
open(file_path, 'w').close()

file_path = playlistDirectory+"\\customSize.mpcpl"
open(file_path, 'w').close()


#Write both playlists to playlistDirectory + ...
writeMPCPlaylist(cleanupSortedList(getSortedList(2)))
writeMPCPlaylist(cleanupSortedList(getSortedList(1)))