import wmi
#import win32api

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
            print('Process terminated')
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

def killVlcDrivers():
    try:
        for process in defineLocalServer().Win32_Process(CommandLine="vlc.exe"):
            #process.Terminate()
            print(process)
            #print('Process terminated')
            #return print(process.Terminate())
    except:
        print("failed to kill")

def killPythonMPCProc():
    try:
        # for process in defineLocalServer().Win32_Process(CommandLine="python.exe"):
        #     #process.Terminate()
        #     print(process)
            #print('Process terminated')
            #return print(process.Terminate())
        for process in defineLocalServer().Win32_Process(name="jupyter-notebook.exe"):
            #print(process.ProcessId, process.Name)
            if("MPC" in process.CommandLine):
                print(process.CommandLine)
                process.Terminate()

    except Exception as e:
        print("failed to kill", e)

#killPythonMPCProc()

#killVlcDrivers()
#killChromeDrivers()
#killGekoDrivers()
