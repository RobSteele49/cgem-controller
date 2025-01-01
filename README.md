Filename: README.md

2025-01-01

1st execute the spawnSimulator.py program. Then, in a separate window
execute the cgemInterface.py.

The cgemController.py program is crashing. I'm not sure of the interaction
between cgemController and cgemInterface.

Started debugging cgemController.py. In the gotCommandWithHp and having
trouble with the writeString assigment. Not sure what I should be doing
with ra and dec right now. Need some more debugging but as the code stands
it was transimitting bytes to the spawned simulator.

The code as written is sending one byte from the cgemInterface to the
simulator.

# cgem-controller

2024-12-30

Using the cgemEnv on a Chromebook machine. To activate the environment
the command is:

source cgemEnv/bin/activate



2024-11-30

The messierObjstList.py program run OK on my Windows PC (attached to the telescope) from a command prompt window.
I had to do a 'pip install astroquery'

The version info is:

python --version
Python 3.12.7

Ran this same python program on a raspberry pi 4 (astroberry) and it worked
just find. The command for running it was:

python3 messierObjectList.py

This was an older version of python than on my PC:

python3 --version
Python 3.7.3

Older notes than 2024:

serial.in_waiting() will get the number of bytes waiting for input

2022-12-12

Installed, via pip install, sufficient packages to get testSerial.py to
work. Here is the screen shot of the run:

robsteele49@penguin:~/git/cgem-controller$ python3 testSerial.py 
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

