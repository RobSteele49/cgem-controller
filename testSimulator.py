# testSimulator.py

# 2024-12-30 Currently just running the thread 'testSimulator' without
# actually running the simulator.

import time
import threading

class testSimulator(threading.Thread):
    
    def __init__ (self):
        self._stop_event = threading.Event()

    def run (self):
        while not self._stop_event.is_set():
            print ('Running in an infinite loop')
            time.sleep(1)

    def stop (self):
        self._stop_event.set()

if __name__ == '__main__':

    print ('Inside of TestSimulator.__main')
    print ("About to exit")
