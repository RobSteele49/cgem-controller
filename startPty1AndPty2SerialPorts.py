# startPty1AndPty2SerialPorts.py

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


class runNullModem (threading.Thread):
    
    def __init__ (self, target):
        super().__init__ (target=target)
        self.stopRunNullModem = False
        
    def stop(self):
        removePty1Command = ['rm', '-rf', './pty1']
        removePty2Command = ['rm', '-rf', './pty2']
        self.stopRunNullModem = True
        time.sleep(2)
        subprocess.run (removePty1Command, capture_output=True, text=True)
        subprocess.run (removePty2Command, capture_output=True, text=True)
        killProcess ('socat')
        
    def run(self):
        runCommand("./nullmodem.sh")
        while not self.stopRunNullModem:
#           print ('inside of runNullModem.run()')
            time.sleep(1)
   
if __name__ == '__main__':

    print ('First line of __main__')

    threadRunNullModem = runNullModem(target=None)
    threadRunNullModem.start()
    
    print ('inside of spawnSimulatorV2.__main__')

    for i in range (1,10):
        print ('inside of for loop ' + str(i))
        time.sleep(1)

    print ('Calling runNullModem.stop')
    threadRunNullModem.stop()
    
    print ('About to exit from spawnSimulatorV2.__main__')


    

    



