#!/bin/bash
# debugTTy.sh

# 2024-12-30 Added a & to the end of the command. But, this isn't
# working on my Chromebook

baudrate='b9600'
debug='-v -D -d -d'
debug= ' '

socat ${debug} PTY,link=./pty1,${baudrate},cfmakeraw GOPEN:/dev/ttyUSB0,${baudrate},cfmakeraw 2> ttyLogFile.txt &

