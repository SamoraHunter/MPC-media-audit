

import time
from IPython.display import clear_output

from selenium import webdriver
from selenium.webdriver.common.by import By

import math

import atexit
import wmi

options = webdriver.ChromeOptions()
#Enable for headless, driver should terminate on closing.
#options.add_argument('headless')


browser = webdriver.Chrome("C:\\Users\\Artemis\\chromedriver.exe")

browser.get('https://www.httpbin.org/headers')


# %%

global toWrite

toWrite = ''


def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)




def defineLocalServer():
    #
    try:
        cLOCAL = wmi.WMI()
    except:
        print("failed to define local server")

    return cLOCAL


def killChromeDrivers():
    try:
        for process in defineLocalServer().Win32_Process(name="chromedriver.exe"):
            process.Terminate()
            return print(process.Terminate())
    except:
        print("failed to kill")


def killGekoDrivers():
    for process in defineLocalServer().Win32_Process(name="geckodriver.exe"):
        process.Terminate()
        return print(process.Terminate())


def killFirefox():
    for process in defineLocalServer().Win32_Process(name="firefox.exe"):
        try:
            process.Terminate()
        except:
            print("Failed on kill firefox")
        return print(process.Terminate())


# %%

def getFilePlayingPath():
    try:
        # refresh
        browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
        path = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[1]/td/a[1]').text
    except:
        print("Failed to get path")

    return path


# %%

def setSpeed():
    try:
        global speed
        mult = math.exp(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
        time.sleep(0.5)
        speed = browser.find_element(By.XPATH, '//*[@id="v1"]').size.get('width')
        speed = speed * mult
        print("Speed:" + str(speed))
        return speed
    except(Exception):
        print(Exception)
        print("failed to get speed")

    # %%
def writeToTempWrite(line):

    file_path = "C:\\Users\\Artemis\\tempWrite.txt"
    #Clear file before rewriting
    open(file_path, 'w').close()
    with open(file_path, 'a') as file:
        file.write(line)

browser.get('http://localhost:13579/controls.html')


#atexit.register(savecounter)
#atexit.register(print("Exiting and closing driver..."))
@atexit.register
def goodbye():
    print("Exiting and closing driver...")
    browser.close()

# %%

# boolean false
global speed
speed = 6
quickSec = 0.01

setSpeed()

for i in range(1, 10000):
    print(i)
    browser.get('http://localhost:13579/controls.html')
    speed = setSpeed()

    toWrite = getFilePlayingPath()
    writeToTempWrite(toWrite)
    #% store toWrite


    if (speed < 98):
        # a = keyboard.read_key()

        #     if a == '+':
        #         print("Option {} was pressed\n".format(a))
        #         time.sleep(300)
        #     else:
        #         #continue
        #         pass
        # refresh
        try:
            browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
        except:
            print("mpc is down? sleeping")
            time.sleep(60)
        time.sleep(quickSec)
        length = browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]').text
        startLen = length
        while (length == 0):
            length = browser.find_element(By.XPATH,
                                          '/html/body/div[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]').text
            time.sleep(quickSec)
            # refresh
            browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
            time.sleep(quickSec)

        full = get_sec(length)
        actualStart = get_sec(length) * 0.05
        quarter = get_sec(length) * 0.25
        half = get_sec(length) * 0.5
        twothird = get_sec(length) * 0.75
        CS = get_sec(length) * 0.95
        print("Total" + str(get_sec(length)))

        doneOne = False


        startLength = browser.find_element(By.XPATH,
                                           '/html/body/div[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]').text

        # refresh
        browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
        currentSecond = get_sec(browser.find_element(By.XPATH, '//*[@id="time"]').text)

        print("currentSecond = " + str(currentSecond))


        speed = setSpeed()
        print(currentSecond < actualStart)
        if (currentSecond < actualStart):

            doneOne = False
            doneTwo = False
            doneThree = False
            doneNext = False

            print("Going to quarter")
            ignore = False
            time.sleep(quickSec)
            print(time.strftime('%H:%M:%S', time.gmtime(quarter)))
            # refresh
            browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
            time.sleep(quickSec)
            browser.find_element(By.XPATH, '//*[@id="pos"]').clear()
            time.sleep(quickSec)
            browser.find_element(By.XPATH, '//*[@id="pos"]').send_keys(time.strftime('%H:%M:%S', time.gmtime(quarter)))
            time.sleep(quickSec)
            browser.find_element(By.XPATH, '/html/body/div[2]/form/table/tbody/tr/td[4]/input').click()
            time.sleep(quickSec * 5)
            # refresh
            try:
                browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
                currentSecond = get_sec(browser.find_element(By.XPATH, '//*[@id="time"]').text)
            except:
                print("failed on start")
                time.sleep(60)

            speed = setSpeed()
            if (currentSecond < half and currentSecond > quarter and not doneOne):
                print("Going to half")
                try:
                    time.sleep(quickSec)
                    print(time.strftime('%H:%M:%S', time.gmtime(half)))
                    # refresh
                    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
                    time.sleep(quickSec)

                    browser.find_element(By.XPATH, '//*[@id="pos"]').clear()
                    time.sleep(quickSec)

                    browser.find_element(By.XPATH, '//*[@id="pos"]').send_keys(
                        time.strftime('%H:%M:%S', time.gmtime(half)))
                    time.sleep(quickSec * 5)

                    browser.find_element(By.XPATH, '/html/body/div[2]/form/table/tbody/tr/td[4]/input').click()
                    doneOne = True
                    print(speed)
                    time.sleep(speed)

                except:
                    print("Failed going to half")
                print("finished doing half")
            else:
                print("passing at half")
                doneOne = True
                doneTwo = True
                doneThree = True
                doneNext = True

            time.sleep(3)
            # refresh

            try:
                browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
                currentSecond = get_sec(browser.find_element(By.XPATH, '//*[@id="time"]').text)
                print(currentSecond)
            except:
                print("Failed after half")
                time.sleep(60)
            print("checking twothird after half...")
            speed = setSpeed()
            if (currentSecond < twothird and currentSecond > half and not doneTwo):
                print("Going to twothird")
                time.sleep(quickSec)
                print(time.strftime('%H:%M:%S', time.gmtime(twothird)))
                # refresh
                browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
                time.sleep(quickSec)
                browser.find_element(By.XPATH, '//*[@id="pos"]').clear()
                time.sleep(quickSec)
                browser.find_element(By.XPATH, '//*[@id="pos"]').send_keys(
                    time.strftime('%H:%M:%S', time.gmtime(twothird)))
                time.sleep(quickSec)
                browser.find_element(By.XPATH, '/html/body/div[2]/form/table/tbody/tr/td[4]/input').click()
                doneTwo = True
                time.sleep(speed)
            else:
                print("passing at twothird")
                doneOne = True
                doneTwo = True
                doneThree = True
                doneNext = True

            time.sleep(quickSec)
            try:
                # refresh
                browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
                currentSecond = get_sec(browser.find_element(By.XPATH, '//*[@id="time"]').text)
                print(currentSecond)
            except:
                print("failed on twothird")
                time.sleep(60)

            speed = setSpeed()
            if (currentSecond < CS and currentSecond > twothird and not doneThree):
                print("Going to CS")
                time.sleep(speed)
                print(time.strftime('%H:%M:%S', time.gmtime(CS)))
                # refresh
                browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
                time.sleep(quickSec)
                browser.find_element(By.XPATH, '//*[@id="pos"]').clear()
                time.sleep(quickSec)
                browser.find_element(By.XPATH, '//*[@id="pos"]').send_keys(time.strftime('%H:%M:%S', time.gmtime(CS)))
                time.sleep(quickSec)
                browser.find_element(By.XPATH, '/html/body/div[2]/form/table/tbody/tr/td[4]/input').click()
                doneThree = True
                time.sleep(speed)
            else:
                print("passing at cs")
                doneOne = True
                doneTwo = True
                doneThree = True
                doneNext = True

            time.sleep(quickSec * 3)
            try:
                # refresh
                browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
                currentSecond = get_sec(browser.find_element(By.XPATH, '//*[@id="time"]').text)
                print(currentSecond)
            except:
                print("Failed on twoThird")
                time.sleep(60)

            speed = setSpeed()
            if (currentSecond > CS and not doneNext):
                print("Going to NEXT")
                time.sleep(quickSec)
                # refresh
                browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
                time.sleep(quickSec)
                browser.find_element(By.XPATH,
                                     '/html/body/div[4]/table/tbody/tr/td[3]/table/tbody/tr/td[2]/form/input[2]').click()

                time.sleep(quickSec)

                clear_output(wait=True)
                time.sleep(quickSec)
            try:
                # refresh
                browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()
                currentSecond = get_sec(browser.find_element(By.XPATH, '//*[@id="time"]').text)
                toWrite = getFilePlayingPath()
                #% store
                toWrite
                print(currentSecond)
                time.sleep(speed)
            except:
                print("Failed on cs")
                time.sleep(60)
                doneNext = True
            else:
                print("passing at next")
                doneOne = True
                doneTwo = True
                doneThree = True
                doneNext = True

        else:
            print("Interval sleep")
            time.sleep(5)
            time.sleep(quickSec)
            # refresh
            try:
                browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td[4]/form/input').click()

                currentSecond = get_sec(browser.find_element(By.XPATH, '//*[@id="time"]').text)
            except:
                print("End sleep")
                time.sleep(60)
            print(currentSecond)
            clear_output(wait=True)
    else:
        print("min speed, vol highest, pausing operations")
        print(speed)
        time.sleep(15)
