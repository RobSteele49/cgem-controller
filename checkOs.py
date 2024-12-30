import platform

def checkOs():
    if platform.system() == 'Linux':
        print("Running on Linux")
        # Do something specific for Linux
    elif platform.system() == 'Windows':
        print("Running on Windows")
        # Do something specific for Windows
    else:
        print("Unknown operating system")


if __name__ == '__main__':
    
    checkOs()

    print ('system         : ' + platform.system())
    print ('node           : ' + platform.node())
    print ('release        : ' + platform.release())
    print ('versoin        : ' + platform.version())
    print ('machine        : ' + platform.machine())
    print ('python_version : ' + platform.python_version())


