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
    ra.hr   = input ('raHr   : ')
    
# Touch base, with Zach, see if using an exit() here would by python like?

    if int(ra.hr) <= -1:
        print ('User specified time to quit')
        loopControl = False
    else:
        ra.min  = input ('raMin  : ')
        ra.sec  = input ('raSec  : ')
    
        dec.deg = input ('decDeg : ')
        dec.min = input ('decMin : ')
        dec.sec = input ('decSec : ')
        
        print ('dec.deg : ', dec.deg)

        print ('Execute the HP goto command.')
        print (f'RA  : {ra.toCgem()}')
        print (f'DEC : {dec.toCgem()}')

        # 2025-01-04 ra is of type 'convertRaDecToCgemUnits.ConvertRa'
        # and dec is of type 'convertRaDecToGemUnits.ConvertDec'
        # Need to build a check for that.
        
        
        cgem.gotoCommandWithHP (ra, dec)
        # 2025-01-04 request HP return value
        (returnRa, returnDec) = cgem.requestHighPrecisionRaDec()
        
        raHrMinSec   = ra.fromCgem(returnRa)
        decDegMinSec = dec.fromCgem(returnDec)

        print (raHrMinSec)
        print (decDegMinSec)
        
        print (f'RA  ( hr, min, sec): {raHrMinSec[0]}:{raHrMinSec[1]}:{raHrMinSec[2]}')
        print (f'DEC (deg, min, sec): {decDegMinSec[0]}:{decDegMinSec[1]}:{decDegMinSec[2]}')

cgem.quitSimulator()

time.sleep (2)

cgem.closeSerial()

