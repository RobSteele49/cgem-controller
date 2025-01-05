# Filename: cgemObserveSimbadObjects.py

# This program is setup to observe Messier objetcs.

# I'm not using the alt/azi to determine if the object is above the horizon
# and I should be.

# Version working on the telescope
# commit e51ecdc9a67699133f19de118f314c9fc5237605

import convertRaDecToCgemUnits
import cgemInterface
import simbadObjectLists

if __name__ == '__main__':

    # Request input as to if simulation or using telescope hardware
    
    if input("Enter 1 for simulation 2 for hardware ") == '1':
        simulate = True
    else:
        simulate = False
    
    # The initializer for cgemInterface will open the serial port.
    # The default is ./pty1 which works with either the simulator
    # using nullmodem.sh or when using socat. If talking directly
    # to real hardware will want to set port = '/dev/ttyUSB0'
    # or something simular.

    cgem       = cgemInterface.CgemInterface()

    convertRa  = convertRaDecToCgemUnits.ConvertRa()
    convertDec = convertRaDecToCgemUnits.ConvertDec()
    
    # messierObjectList goes out to the simbad database and querys
    # for the Messier Objects. It returns a sorted list of those objects
    # ready for observing.
    
git    # As of 10/21/18 I was adding the altitude and azimuth of each
    # object in the list.

    simbadLists = simbadObjectLists.SimbadObjectLists (
        mgcMinMag          = 10.0,
        icMinMag           =  9.0,
        ngcMinMag          =  6.0,
        allMinMag          =  6.0,
        galaxiesMinMag     =  9.0,
        openClustersMinMag =  6.5)
    
    print ('Number of objects in simbadLists : ', len(simbadLists.objectTable))
    print
    print ('Loop over all visible objects.')
    
    loopOverAllSimbadObjects = True
    while loopOverAllSimbadObjects:
        loopOverSimbadObjects = True
        index        = 0
        objectNumber = 1
        while (loopOverSimbadObjects):
            x = 0
            if index == len(simbadLists.objectTable):
                loopOverSimbadObjects = False
            else:
                if simbadLists.objectTable[index].bin() > 0:
                                
                    alt = simbadLists.objectTable[index].alt.deg

                    if alt > 20.0:
                        print ('Object Number : ', objectNumber)
                        simbadLists.objectTable[index].write()
                        azi = simbadLists.objectTable[index].azi.deg

                        objectNumber += 1

                        # Grab the input value and attempt to convert it to
                        # an integer
                        
                        x = int(input('1 to observe, 2 to skip, 3 to exit : '))
                        if x == 1:
                        
                            objectRa  = simbadLists.objectTable[index].ra
                            objectDec = simbadLists.objectTable[index].dec

                            print ('object RA  (hr:min:sec)  : ', \
                                   objectRa.hr,   ':',            \
                                   objectRa.min,  ':',            \
                                   objectRa.sec)
                            print ('object Dec (deg:min:sec) : ', \
                                   objectDec.deg, ':',            \
                                   objectDec.min, ':',            \
                                   objectDec.sec)

                            newRa = convertRaDecToCgemUnits.ConvertRa \
                                (float(objectRa.hr),                  \
                                 float(objectRa.min),                 \
                                 float(objectRa.sec))
        
                    
                            newDec = convertRaDecToCgemUnits.ConvertDec \
                                (float(objectDec.deg), \
                                 float(objectDec.min), \
                                 float(objectDec.sec))

                            print ('Invoking goComandWithHP')
                            cgem.gotoCommandWithHP (newRa, newDec)

                            telescopeRaDecCgem = \
                                cgem.requestHighPrecisionRaDec()
                            print ('telescopeRaDecCgem:', telescopeRaDecCgem)
                            
                            print \
                            ('---------------------- DONE ------------------')
                            print ()
                        elif x == 3:
                            loopOverSimbadObjects = False
                            print ('Setting loopOverSimbadObjects to :',
                                   loopOverSimbadObjects)
            index += 1

        print ('Finished the list one time, loop again')

        # Attempt to convert this to an integer
        
        y = int(input('1 to loop again, 2 to exit : '))
        if y == 2:
            loopOverAllSimbadObjects = False
            print ('setting loopOverSimbadObjects to: ',
                   loopOverSimbadObjects)
            
        print ('updateObjectTable')
        
        simbadLists.updateObjectTable()

    # Done - shut down and clean up

    print ('Quitting, closing simulator, and serial interfaces.')
    
    cgem.quitSimulator() # does nothing when operating with telescope
    cgem.closeSerial()
    


    
