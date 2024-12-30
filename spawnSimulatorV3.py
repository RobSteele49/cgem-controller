# spawnSimulatorV3.py

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


    

    



