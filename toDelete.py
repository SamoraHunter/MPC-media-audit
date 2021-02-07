import os

import subprocess
from send2trash import send2trash


deleteLogLocation = 'C:\\Users\\Artemis\\toDelete.txt'


def remove_empty_lines(filename):
    """Overwrite the file, removing empty lines and lines that contain only whitespace."""
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.writelines(line for line in lines if line.strip())
        f.truncate()


def readToDeleteList():
    newlist = []
    remove_empty_lines(deleteLogLocation)
    with open(deleteLogLocation, 'r') as f:
        contents = f.readlines()

        return contents


def deleteFilesFromText():
    print(len(readToDeleteList()))
    for i in range(0, len(readToDeleteList())):
        delList = readToDeleteList()
        #print(delList)
        print(delList[i].strip())
        #os.remove(delList[i].strip())
        try:
            send2trash(delList[i].strip())
        except:
            print("Failed to delete")
    open(deleteLogLocation, 'w').close()

def openTextToView():
    os.startfile(deleteLogLocation)



