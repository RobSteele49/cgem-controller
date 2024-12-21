
import time

done = True
class testSimulator:
    
    def __init__ (self):
        done = True
        print ('done = ' + str(done))
        print (done)

    def run (self):
        print ('done = ' + str(done))
        print (done)
        while done:
            print ('Running in an infinite loop')
            time.sleep(1)
            print ('done = ' + str(done))
            print (done)

    def quit (self):
        done = False
        print ('done = ', str(done))

if __name__ == '__main__':

    print ('Inside of TestSimulator.__main')
    
    done = True;

    while done:
        print ('running in an infinite loop')
        time.sleep(1)

    print ("About to exit")
