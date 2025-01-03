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
        
        cgem.gotoCommandWithHP (ra, dec)
        #print cgem.requestHighPrecisionRaDec()

cgem.quitSimulator()
cgem.closeSerial()

