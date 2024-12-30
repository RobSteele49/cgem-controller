# spawnSimulatorV2.py

import os
import platform
import subprocess
import threading
import time

def runCommandNullModem ():
#    result = subprocess.run(["./nullmodem.sh"],
#                            capture_output = True,
#                            text           = True)
    print ('first line of runCommandNullModem')
    if platform.system() == 'Windows':
        process = os.system('./nullmodem.sh')
    else:
        command = ["bash", "./nullmodem.sh"]
        process = subprocess.Popen(command, shell=True)
    print (f"process : {process}")
    return process

def runCommand (baseCommand):
    print ('first line of runCommand')
    if platform.system() == 'Windows':
        process = os.system(baseCommand)
    else:
        command = ["bash", baseCommand]
        print (f"command : {command}")
        process = subprocess.Popen(command, shell=True)
    print (f"process : {process}")
    return process
     
class runNullModem (threading.Thread):
    
    def __init__ (self, target):
        super().__init__ (target=target)
        self.stopRunNullModem = False
        
    def stop(self):
        self.stopRunNullModem = True
        
    def run(self):
        runCommand("./nullmodem.sh")
        while not self.stopRunNullModem:
            print ('inside of runNullModem.run()')
            time.sleep(1)
   
if __name__ == '__main__':
#    def myLoopingFunction():
#        while True:
#            time.sleep(1)
    
    print ('First line of __main__')

# using the runCommandNullModem function able to start the
# nullmodem.sh script.

#    runCommandNullModem()
    runCommand ("./nullmodem.sh")
    
#    threadRunNullModem = runNullModem(target=myLoopingFunction)
#    threadRunNullModem.start()

    print ('Execute the subprocess.run for nullmodem.sh')
    
#    pidModem = subprocess.run(['./nullmodem.sh', '&'],
#                                capture_output = True,
#                                text           = True)
    
    print ('inside of spawnSimulatorV2.__main__')

    for i in range (1,10):
        print ('inside of for loop ' + str(i))
        time.sleep(1)

    print ('Calling runNullModem.stop')

#    threadRunNullModem.stop()

    print ('About to exit from spawnSimulatorV2.__main__')


    

    



