

#
# This code was written 2024-12-28 base on code generated by Gemini
#

import os
import serial

class PortDoesNotExist(Exception):
    pass

def file_exists(file_path):
  """Checks if a file exists at the given path.

  Args:
    file_path: The path to the file.

  Returns:
    True if the file exists, False otherwise.
  """
  return os.path.exists(file_path) and os.path.isfile(file_path)

if __name__ == '__main__':
    if os.name == 'nt':
        port = 'COM6'
    else:
        port = '/dev/ttyUSB0'

    try:
        if (file_exists(port)):
            print (f'Open the serial port, with port {port}')
            ser = serial.Serial(port, 9600)
        else:
            print ('Port does not exist')
            raise PortDoesNotExist()
    
        print (f"Serial info: {ser}")
        print (f"Print the current timeout and then set it for 2.0")
        print (f"Serial timeout: {ser.timeout}")
        ser.timeout = 2.0
        print (f"Connectd to port: {port}")
        print (f"Serial timeout: {ser.timeout}")
        # serial read/write code codes here
    
        input = ser.read (1)

        print (f"Serial read has timed out")
    
    except serial.SerialException as e:
        print (f"Error connecting to serial port: {e}")

    except PortDoesNotExist:
        print ('Exception, port does not exist occurred')
        
    finally:
        print (f"About to close the serial port")
        try:
            ser.close()
        except:
            print ('Exit as ser is not defined so no need to close')
            

    






