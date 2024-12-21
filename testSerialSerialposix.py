
import serial.serialposix

print ('import was successful')

ser = serial.serialposix.Serial ('/dev/tty', 9600)

print (ser.name)

ser.write (b'AAAA')

x = ser.read (4)

ser.close()

