# cgem-controller

serial.in_waiting() will get the number of bytes waiting for input

2022-12-12

Installed, via pip install, sufficient packages to get testSerial.py to
work. Here is the screen shot of the run:

obsteele49@penguin:~/git/cgem-controller$ python3 testSerial.py 
Enter 1 for simulation 2 for hardware 1
Comm Working Flag :  True
Aligment          :  True
GotoInProgress    :  False
RTC location      :  [34.0, 34, 0, 0, 0, 119.0, 119, 0, 0, 1]
Time              :  [19, 42, 52, 12, 12, 2022, 61, False]
response :  b'#\x02'
response[0] :  35
response[1] :  2
Tracking mode     :  Undefined
In requestHighPrecisionRaDec
raHex, decHex  b'#34AB0500'   b''
telescopeRaDecCgem:  [b'#34AB0500', b'']
requestHighPrecisionRaDec failed
In requestLowPrecisionRaDec
raHex, decHex  b'#34AB'   b''
telescopeRaDecCgem:  [b'#34AB', b'']
Quitting, closing simulator, and serial interfaces.

I did run the shell for debugTty.sh, but I'm not sure if that was even
required.

