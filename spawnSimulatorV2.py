# spawnSimulatorV2.py

import subprocess
import threading
import time

class runNullModem (threading.Thread):
    
    def __init__ (self, target):
        super().__init__ (target=target)
        self.stopRunNullModem = False
        
    def stop(self):
        self.stopRunNullModem = True
        
    def run(self):
        pidModem = subprocess.run(['./nullmodem.sh'],
                                  capture_output = True,
                                  text           = True)
        while not self.stopRunNullModem:
            print ('inside of runNullModem.run()')
            time.sleep(1)

if __name__ == '__main__':
    def myLoopingFunction():
        while True:
            time.sleep(1)
    
    print ('First line of __main__')
    
    threadRunNullModem = runNullModem(target=myLoopingFunction)
    threadRunNullModem.start()

    print ('inside of spawnSimulatorV2.__main__')

    for i in range (1,10):
        print ('inside of for loop ' + str(i))
        time.sleep(1)

    print ('Calling runNullModem.stop')

    threadRunNullModem.stop()

    print ('About to exit from spawnSimulatorV2.__main__')


    

    



