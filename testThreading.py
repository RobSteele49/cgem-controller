# testThreading.sp

# As of 2024-12-28 this code was working on a Windows and Chromebook computers.
# it can be used as the basis of my threading code for the CGEM interface where
# the serial interface will run in a separate thread of control.

import threading
# import subprocess
import time
import testSimulator

class StoppableThread1(threading.Thread):
    def __init__ (self, target):
        super().__init__(target=target)
        self._stop1 = False

    def stop(self):
        self._stop1 = True
        print ('in StoppableThread1.stop')

    def run(self):
        while not self._stop1:
            print ('inside of StoppableThread1.run()')
            print ('code for infinite loop Thread1')
            time.sleep(1)

class StoppableThread2(threading.Thread):
    def __init__ (self, target):
        super().__init__(target=target)
        self._stop2 = False

    def stop(self):
        self._stop2 = True
        print ('in StoppableThread2.stop')

    def run(self):
        while not self._stop2:
            print ('inside of StoppableThread2.run()')
            print ('code for infinite loop Thread2')
            time.sleep(1)
            
if __name__ == '__main__':

    def my_looping_function():
        while True:
            # do something repeatedly
            print ('Doing work')
            time.sleep(1)

    thread1 = StoppableThread1(target=my_looping_function)
    thread2 = StoppableThread2(target=my_looping_function)
    thread1.start()
    thread2.start()
    
    print ('inside of testSpawn.__main__')

    for i in range (1,11):
        print ('inside of for loop ' + str(i))
        time.sleep(1)

    print ('calling thread.stop')
    thread1.stop()
    thread2.stop()

    # The join() function, which did not seem to be require for
    # this example.
    
    #print ('calling thread.join')
    #thread1.join()
    #thread2.join()
    
    print ('About to exit from testSpawn.__main__')

