# file name: spawnSimulatorV2.py

# 2025-01-01 It looks to me I wandered down the wrong path with this
# code as the only thing, that I can now identify with the original
# spawn program is that the original program's use of the subprocess
# had been depricated.

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
        result = os.system('./nullmodem.sh')
    else:
        result = os.system(f"bash -c ./nullmodem.sh")
    print (f"result : {result}")
    print (f"result.returncode : {result.returncode}")

def runCommand (command):
    print ('first line of runCommand')
    if platform.system() == 'Windows':
        result = os.system(command)
    else:
        result = os.system(f"bash -c '{command}'")
    print (f"result : {result}")
#    print (f"result.returncode : {result.returncode}")    

def start_socat(baudrate):
    """Starts the socat process with the specified baudrate.

    Args:
        baudrate: The baud rate for the serial communication.

    Returns:
        The subprocess object if the socat process starts successfully, 
        otherwise None.
    """
    socat_command = [
      "socat",
      f"PTY,link=./pty1,{baudrate},cfmakeraw",
      f"PTY,link=./pty2,{baudrate},cfmakeraw",
      "2>", "socatLogFile.txt"
      ]

    
    socat_command = [
      'socat',
      'PTY,link=./pty1,b9600,cfmakeraw',
      'PTY,link=./pty2,b9600,cfmakeraw',
      '2>', 'socatLogFile.txt']
# debug:
#    socat_command = ["socat", "STDIN", "STDOUT"]
    try:
        print (f"invoke subprocess.Popen socat_command : {socat_command}")
#       process = subprocess.Popen(socat_command, shell=True)  # Use shell=True for redirection
        process = subprocess.Popen(args='bash', executable='./nullmodem.sh', shell=True)
#        process = subprocess.run (socat_command, capture_output=True, text=True)
        print (f"process : {process}")
        return process
    except subprocess.CalledProcessError as e:
        print(f"Error starting socat: {e}")
        return None

def stop_socat(process):
    """Attempts to gracefully stop the socat process."""
    if process:
        try:
            print ('send a terminate signal')
            process.terminate()  # Send SIGTERM 
            process.wait(timeout=5)  # Wait for graceful termination
        except subprocess.TimeoutExpired:
            print ('force a termination')
            process.kill()  # Forceful termination if graceful termination fails
            print("Forced termination of socat process.")

class runNullModem (threading.Thread):
    
    def __init__ (self, target):
        super().__init__ (target=target)
        self.stopRunNullModem = False
        
    def stop(self):
        self.stopRunNullModem = True
        time.sleep(2)
        
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

# The runCommandNullModem and runCommand have been working - but
# I am moving to using start_socat and stop_socat as recommended by
# Gemini.
#    runCommandNullModem()
    runCommand ("./nullmodem.sh")
    
#    threadRunNullModem = runNullModem(target=myLoopingFunction)
#    threadRunNullModem.start()

    print ('Execute the subprocess.run for nullmodem.sh')
    
#    pidModem = subprocess.run(['./nullmodem.sh', '&'],
#                                capture_output = True,
#                                text           = True)

#    baudRate = 'b9600'
#    print ('invokde start_socat')
#    socatProcess = start_socat(baudRate)

#    if socatProcess:
    print ('inside of spawnSimulatorV2.__main__')

    for i in range (1,10):
        print ('inside of for loop ' + str(i))
        time.sleep(1)

#    print ('Calling runNullModem.stop')
#    print ('Calling stop_socat')
#    stop_socat(socatProcess)
#    threadRunNullModem.stop()

    removePty1Command = ['rm', '-rf', './pty1']
    removePty2Command = ['rm', '-rf', './pty2']
    
    subprocess.run (removePty1Command, capture_output=True, text=True)
    subprocess.run (removePty2Command, capture_output=True, text=True)
    
    print ('About to exit from spawnSimulatorV2.__main__')


    

    



