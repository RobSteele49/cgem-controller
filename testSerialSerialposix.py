# testSerialSerialposix.py

# 2024-12-30 This is untested, but I'm not sure that the use of
# serialposix is necessary.

import serial.serialposix

print ('import was successful')

ser = serial.serialposix.Serial ('/dev/tty', 9600)

print (ser.name)

ser.write (b'AAAA')

x = ser.read (4)

ser.close()

