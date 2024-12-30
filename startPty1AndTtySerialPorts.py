# startPty1AndTtySerialPorts.py

# 2024-12-30 This code was copied (moved) from spawnSimulatorV3.py
# Is is currently starting the socat function to kick off the two
# serial interfaces. As of right now it just runs for a fixed amount of
# time. The code needs to be modified to be able to stopped externally.

# The main function shows how this code can be used in the context of
# a bigger program.

import os
import platform
import subprocess
import threading
import time
from killProcess import killProcess

def runCommand (command):
    print ('first line of runCommand')
    if platform.system() == 'Windows':
        result = os.system(command)
    else:
        result = os.system(f"bash -c '{command}'")
    print (f"result : {result}")
#    print (f"result.returncode : {result.returncode}")    


class runDebugTtyModem (threading.Thread):
    
    def __init__ (self, target):
        super().__init__ (target=target)
        self.stopRunDebugTtyModem = False
        
    def stop(self):
        removePty1Command = ['rm', '-rf', './pty1']
        removeTtyUsb0Command = ['rm', '-rf', './tty/USB0']
        self.stopRunDebugTtyModem = True
        time.sleep(2)
        subprocess.run (removePty1Command,    capture_output=True, text=True)
        subprocess.run (removeTtyUsb0Command, capture_output=True, text=True)
        killProcess ('socat')
        
    def run(self):
        print ('Execute runCommand with debugTty.sh')
        runCommand("./debugTty.sh")
        while not self.stopRunDebugTtyModem:
#           print ('inside of runDebugTtyModem.run()')
            time.sleep(1)
   
if __name__ == '__main__':

    print ('First line of __main__')

    threadRunDebugTtyModem = runDebugTtyModem(target=None)
    threadRunDebugTtyModem.start()
    
    print ('inside of startPty1AndTtySerialPorts.__main__')

    for i in range (1,21):
        print ('inside of for loop ' + str(i))
        time.sleep(1)

    print ('Calling runNullModem.stop')
    threadRunDebugTtyModem.stop()
    
    print ('About to exit from startPty1AndTtySerialPorts.__main__')

    

    



