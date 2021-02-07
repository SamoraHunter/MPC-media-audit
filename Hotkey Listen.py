from pynput import keyboard
import os


global toWrite

toWrite = ''

#Set log file locations:
deleteLogLocation = "C:\\Users\\Artemis\\toDelete.txt"
tempWriteLocation = "C:\\Users\\Artemis\\tempWrite.txt"


def writeToLog(line):
    file_path = deleteLogLocation
    with open(file_path, 'a') as file:
        file.write(line + "\n")

def readCurrentlyPlaying():
    file_path = tempWriteLocation
    with open(file_path, 'a') as file:
        contents = file.readline()
    return str(contents)


def listener():
    print("Listening...")
    # The key combination to check
    COMBINATIONS = [
        # {keyboard.Key.shift, keyboard.KeyCode(char='a')},
        # {keyboard.Key.shift, keyboard.KeyCode(char='A')}
        {keyboard.KeyCode(char='*')}
    ]

    # The currently active modifiers
    current = set()

    def execute():
        print("Key pressed! Writing to log")
        #% store - r
        global toWrite
        print(readCurrentlyPlaying)
        writeToLog(readCurrentlyPlaying)
        # os.remove(toWrite)

    def on_press(key):
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.add(key)
            if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
                execute()

    def on_release(key):
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.remove(key)

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


listener()