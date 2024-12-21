import platform

if __name__ == '__main__':
    
    if platform.system() == 'Linux':
        print("Running on Linux")
        # Do something specific for Linux
    elif platform.system() == 'Windows':
        print("Running on Windows")
        # Do something specific for Windows
    else:
        print("Unknown operating system")

