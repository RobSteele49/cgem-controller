# Filename: cgemController.py

# Provide basic goto operations for a manually entered RA/Declination

import convertRaDecToCgemUnits
import cgemInterface
import serial
import command
import time

# Initialize the CgemInterface with a False - this will need to be updated
# after we get the serial simulator working.

# 2025-01-01 The ra and dec, as written did not work with the current
# definition in convertRaDecToCgemUnits

cgem = cgemInterface.CgemInterface()
ra  = convertRaDecToCgemUnits.ConvertRa()
dec = convertRaDecToCgemUnits.ConvertDec()

print ('Enter a negative number for the RA hours wnd the loop will exit.')

loopControl = True
while loopControl:
    raHr   = input ('hr     : ')
    
    if int(raHr) <= -1:
        print ('User specified time to quit')
        loopControl = False
    else:
        raMin  = input ('raMin  : ')
        raSec  = input ('raSec  : ')
    
        decDeg = input ('decDeg : ')
        decMin = input ('decMin : ')
        decSec = input ('decSec : ')

        ra.set(raHr, raMin, raSec)
        dec.set(decDeg, decMin, decSec)
        
        print (f'RA  : {ra.getCgemUnits()}')
        print (f'DEC : {dec.getCgemUnits()}')

        print ('Execute the HP goto command.')        
        cgem.gotoCommandWithHP (ra, dec)
        # 2025-01-04 request HP return value
        (returnRa, returnDec) = cgem.requestHighPrecisionRaDec()
        
        raHrMinSec   = ra.getHrMinSec()
        decDegMinSec = dec.getDegMinSec()

        print (raHrMinSec)
        print (decDegMinSec)
        
        print (f'RA  ( hr, min, sec): {raHrMinSec[0]}:{raHrMinSec[1]}:{raHrMinSec[2]}')
        print (f'DEC (deg, min, sec): {decDegMinSec[0]}:{decDegMinSec[1]}:{decDegMinSec[2]}')

cgem.quitSimulator()

time.sleep (2)

cgem.closeSerial()

