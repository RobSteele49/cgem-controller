# Filename: spawnSimulator.py

# 2025-01-03 Did a git move from spawnSimulatorV2.py to
# spawnSimulator.py

# As of 2024 12, the spawnlp task has been depricated and this code does
# not work.

# 2025-01-01 Starting to work. Will remove some of the old unused code
# before committing. See need to kill the files.

import os
import signal
import time
import threading
import subprocess

# Kicks off either the nullmodem.sh script or debugTty.sh
# The debugTty.sh script is used for debugging hardware.
# The nullModem.sh and simulatory.py are using when running the simulator.

from killProcess import killProcess

# 2025-01-02 There are two instances of simulator.py, one is simulator.py
# and the other is simulatorV2.py. I'm not really sure what the difference
# between these two is.

def runSimulator():
    subprocess.run(["python", "simulator.py"])

def runNullModem():
    subprocess.run(["bash", "-c", "./nullmodem.sh"])

def runTtyModem():
    subprocess.run(["bash", "-c", "./debugTty.sh"])
          
class SpawnSimulator:

    # Initializer for starting either nullmodem and simulator or
    # debugTty.sh.
    
    def __init__(self, simulate=True):

        print ('simulate: {simulate}')
               
        self.simulate = simulate
               
        print ('Inside of spawnSimulator.__init__')
               
        if self.simulate == True:

            print ('execut target runNullModem')
            nullModemThread = threading.Thread(target=runNullModem)
            nullModemThread.start()
            
            # Check that both pty1 and pty2 files exist before continuing
            # Appears that nullmodem.sh creates the pty1 and pty2 files.
            # But I want to check with Zach to see if he remembers this
            # part of the code.
            
            #checkFileExistance = True
            #while checkFileExistance:
            #    checkFileExistance1 = os.path.exists("pty1")
            #    checkFileExistance2 = os.path.exists("pty2")
            #    checkFileExistance  = not(checkFileExistance1 and
            #                             checkFileExistance2)

            print ('execute target runSimulator')
            simulatorThread = threading.Thread(target=runSimulator)
            simulatorThread.start()
        
        else:

# 2025-01-01            self.pid_modem = os.spawnlp(os.P_NOWAIT,
# 2025-01-01                                "./debugTty.sh", " ", " ")
            
            # Check that both pty1 and /dev/ttyUSB0 exists before continuing
            
            checkFileExistance = True
            while checkFileExistance:
                checkFileExistance1 = os.path.exists("pty1")
                checkFileExistance2 = os.path.exists("/dev/ttyUSB0")
                checkFileExistance  = not(checkFileExistance1 and
                                          checkFileExistance2)
    def shutdown(self):
        removePty1Command = ['rm', '-rf', './pty1']
        removePty2Command = ['rm', '-rf', './pty2']
        removeTtyCommand  = ['rm', '-rf', './tty']
        print ('running shutdown')
        if self.simulate == True:
            killProcess('runNullModem')
            killProcess('socat')
            subprocess.run (removePty1Command, capture_output=True, text=True)
            subprocess.run (removePty2Command, capture_output=True, text=True)
            subprocess.run (removeTtyCommand,  capture_output=True, text=True)
        killProcess('simulator.py')
        killProcess('runTtyModem')

# Just as a reminder, this code will ONLY execute when the file is
# run from the command line ('python spawnSimulator.py').

if __name__ == '__main__':
    print ('First line of __main__ spawnSimulatorV3.py')
    sp = SpawnSimulator(True)
    print ('Finished SpawnSimulator')
    time.sleep(3600)
    print ('done with 3600 second wait, will now call shutdown')
    sp.shutdown()




