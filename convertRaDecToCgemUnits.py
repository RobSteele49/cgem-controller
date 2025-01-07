# Filename: convertRaDecToCgemUnits

# Pretty sure that having the name Ra and Dec as classes in two different
# modules is confusing me. For now I'm going to prefix Ra and Dec in this
# module with 'Convert'.

# from raDecLst import Ra, Dec, Lst, Alt, Azi
# 2024-12-20 NOT USED: import serial

# 2024-12-30 Worked OK on a windows computer.
# 2025-01-04 Worked OK on a Chromebook computer.

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class RaError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg  = msg

class DecError(Error):
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg  = msg
    
class CgemConverter(object):

# This is setting up constants for the conversion process to the
# units used on my CGEM telescope.

    softwareResolution = 2**24;
    fullCircleDeg      = 360
    fullCircleSec      = fullCircleDeg * 60.0 * 60.0
    
    oneTwelthArcSeconds = fullCircleSec * 12.0
    conversionFactor    = softwareResolution / oneTwelthArcSeconds

# The for loop below worked in the older version of Python.
# At the current time 1/29/21 I'm not even sure of what this logic
# was supposed to do.

    def __init__(self, args={}):
        self.toCgem()
        self.fromCgem(cgemUnits = '0')

# The class CovertRa handles conversion to and from cgem units for
# the RA. The methods defined in the class are:
# __init__
# toCgem
# fromCgem
# getSeconds
# __sub__

class ConvertRa(CgemConverter):

    # 2025-01-07 __init__ creates an object with the intenal default
    # values of 0:0:0 and creates an internal RA in Cgem units in the
    # variable self.raCgemUnits.
    
    def __init__ (self, hr=0, min=0, sec=0):
        #args = locals()
        #super(Ra, args.pop('self')).__init__(args)
        self.hr  = hr
        self.min = min
        self.sec = sec
        self.toCgem(hr,min,sec)

    # 2025-01-07 toCgem takes the RA with the default values of 0:0:0
    # and creates a RA value in Cgem units in the variable self.raCgemUnits.
    # The arguments in RA are saved in the self.[hr,min,sec]
    
    def toCgem (self, hr, min, sec=0):
        self.hr = hr
        self.min = min
        self.sec = sec
        self.__oldToCgem()
        return self.raCgemUnits

    # 2025-01-07 This is the old toCgem function that incorporates the
    # logic for the Cgem unit conversion. I just left this name, but
    # is really intended to be a private function - but I'm not sure how
    # to implement that parigm in python. Looks like adding the __ as
    # a prefix is the way to do it.
    
    def __oldToCgem(self):
        self.raInSeconds = (float(self.hr)          * \
                            3600 + float(self.min)  * \
                            60.0 + float(self.sec)) * \
                            15.0
        
        if int(self.hr) < 0 or int(self.hr) > 23:
            raise RaError.message('hour out of range')
        if int(self.min) < 0 or int(self.min) > 59:
            raise RaError.message('min out of range')
        if float(self.sec) < 0.0 or float(self.sec) > 59.99:
            raise RaError.message('sec out of range')
        if float(self.raInSeconds) < 0.0:
            raise RaError.message('seconds less than 0')
        if float(self.raInSeconds) >= 86400*15.0:
            raise RaError.message('seconds > 86400 seconds')

        gotoValue = self.raInSeconds * 12.0 * CgemConverter.conversionFactor
        hexGotoValue = hex(int(gotoValue) << 8)
        strGotoValue = str(hexGotoValue)[2:]
        addCharacters = 8-len(strGotoValue)

        for i in range (0,addCharacters):
            strGotoValue = '0' + strGotoValue

        self.raCgemUnits = str.upper(strGotoValue)
        
        return self.raCgemUnits

    # 2025-01-07 Another poorly named fuction. This one takes the
    # internal value of the RA in Cgem units and coverts them to an
    # RA as [hr,min,sec]
    
    def fromCgem(self):
        x = (int(self.raCgemUnits,16)) >> 8
        seconds = x / 15.0 / 12.0 / CgemConverter.conversionFactor
        hr = int(seconds / 3600.0)
        min = int((seconds - (hr * 3600.0)) / 60.0)
        sec = int(seconds - (hr * 3600.0) - (min * 60.0))
        returnValue = str(hr) + 'h' + str(min) + 'm' + str(sec) + 's'
        return [hr, min, sec]

    # 2025-01-07 This is also private and only used in subtraction
    # method defined below.
    
    def __getSeconds(self):
        return ((float(self.hr )   * 3600.0) +
                (float(self.min)   *   60.0) +
                (float(self.sec))) *   15.0

    # 2025-01-07 This sets the RA for the class in both RA[hr:min:sec]
    # and in Cgem Units in the variable self.raCgemUnits.
    
    def set (self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec
        self.__oldToCgem()
        return self.raCgemUnits

    # 2025-01-07 getHrMinSec retrieves the current RA [hr:min:sec]
    # value.
    
    def getHrMinSec (self):
        return [self.hr, self.min, self.sec]

    # 2025-01-07 getCgemUnits retireves the current RA in Cgem units.
    
    def getCgemUnits (self):
        return self.raCgemUnits

    # 2025-01-07 This is used more for debugging but allows me to set
    # the RA in Cgem units directly as a hex value. I'm not even sure
    # if this function is even necessary.
    
    def setHex (self, hex):
        self.raCgemUnits = str.upper(hex)
        return self.raCgemUnits
    
    # define subtraction

    def __sub__ (self, y):
        xSeconds = self.__getSeconds()
        ySeconds = y.getSeconds()
        return xSeconds - ySeconds

    def __lt__ (self,y):
        return self.__getSeconds() < y.__getSeconds()

    def __le__ (self,y):
        return self.__getSeconds() <= y.__getSeconds()

    def __eq__ (self,y):
        return self.__getSeconds() == y.__getSeconds()
    
# The class CovertDec handles conversion to and from cgem units for
# the Dec. The methods defined in the class are:
# __init__
# toCgem
# fromCgem
# getSeconds
# __lt__
# __le__
# __eq__

class ConvertDec(CgemConverter):

    # 2025-01-07 __init__ creates an object with the intenal default
    # values of 0:0:0 and creates an internal Declination in Cgem units in
    # the variable self.decCgemUnits.
    
    def __init__ (self, deg=0, min=0, sec=0):
        self.deg = deg
        self.min = min
        self.sec = sec
        self.toCgem(deg,min,sec)

    # 2025-01-07 toCgem takes the Declination with the default values of
    # 0:0:0 and creates a Declination value in Cgem units in the variable
    # self.decCgemUnits.
    # The arguments in RA are saved in the self.[deg,min,sec]

    def toCgem(self, deg, min, sec=0):
        self.deg = deg
        self.min = min
        self.sec = sec
        self.__oldToCgem()
        return self.decCgemUnits

    # 2025-01-07 This is the old toCgem function that incorporates the
    # logic for the Cgem unit conversion. I just left this name, but
    # is really intended to be a private function. Looks like adding
    # the __ as a prefix is the way to do it.
    
    def __oldToCgem(self):
        decNeg = False;
        
        if int(self.deg) < 0:
            decNeg = True
            self.deg = -self.deg

        if int(self.deg) > 90 or int(self.deg) < -90:
            raise DecError.message('deg out of range')
        if int(self.min) < 0:
            decNeg = True
            self.min = -int(self.min)
        if int(self.min) < 0 or int(self.min) >= 60:
            raise DecError.msg('min out of range')
        if int(self.sec) < 0:
            decNeg = True
            self.sec = -int(self.sec)
        if  int(self.sec) < 0 or int(self.sec) >= 60:
            raise DecError.msg('sec out of range')

        self.decInSeconds    =  abs(float(self.deg)) * 60.0 * 60.0 + float(self.min) * 60.0 + float(self.sec)

        if decNeg:
            self.decInSeconds = (360.0 * 60.0 * 60.0) - float(self.decInSeconds)

        gotoValue = self.decInSeconds * 12.0 * CgemConverter.conversionFactor
        hexGotoValue = hex(int(gotoValue) << 8)
        strGotoValue = str(hexGotoValue)[2:]
        addCharacters = 8-len(strGotoValue)
        for i in range (0,addCharacters):
            strGotoValue = '0' + strGotoValue       

        self.decCgemUnits = str.upper(strGotoValue)
        return self.decCgemUnits

    # 2025-01-07 Another poorly named fuction. This one takes the
    # internal value of the RA in Cgem units and coverts them to an
    # Declination as [deg,min,sec]
    
    def fromCgem (self, cgemUnits):
        x = int(cgemUnits,16) >> 8
        
        seconds = int(x / 12.0 / CgemConverter.conversionFactor)

        if seconds > 180.0*60.0*60.0:
            seconds = seconds - (360.0*60.0*60.0)
        deg = int(seconds / 3600.0)
        min = int((seconds - (deg * 3600.0)) / 60.0)
        sec = int(seconds - (deg * 3600.0) - (min * 60.0))
        returnValue = str(deg) + 'd' + str(min) + 'm' + str(sec) + 's'
        return [deg, min, sec]

    # 2025-01-07 This sets the Declination for the class in both
    # Dec[deg:min:sec] and in Cgem Units in the variable self.decCgemUnits.

    def set (self, deg, min, sec):
        self.deg = deg
        self.min = min
        self.sec = sec
        self.__oldToCgem()
        return self.decCgemUnits

    # 2025-01-07 getDegMinSec retrieves the current Declination [deg:min:sec]
    # value.

    def getDegMinSec (self):
        return [self.deg, self.min, self.sec]

    # 2025-01-07 getCgemUnits retireves the current Declination in Cgem units.
 
    def getCgemUnits (self):
        return self.decCgemUnits

    # 2025-01-07 This is used more for debugging but allows me to set
    # the Declination in Cgem units directly as a hex value. I'm not even
    # sure if this function is even necessary.
 
    def setHex (self, hex):
        self.decCgemUnits = str.upper(hex)

    #2025-01-07 Math functions:
        
    def __getSeconds(self):
        return (float(self.deg) * 60.0 * 60.0) + (float(self.min)  * 60.0) + float(self.sec)

    def __sub__ (self, y):
        xSeconds = self.__getSeconds()
        ySeconds = y.__getSeconds()
        return xSeconds - ySeconds
    
    def __lt__ (self,y):
        return self.__getSeconds() < y.__getSeconds()

    def __le__ (self,y):
        return self.__getSeconds() <= y.__getSeconds()

    def __eq__ (self,y):
        return self.__getSeconds() == y.__getSeconds()

# The class CovertLst handles conversion to seconds.
# The methods defined in the class are:
# __init__
# getSeconds
# __sub__

class ConvertLst:
    def __init__ (self, hr = 0, min = 0, sec = 0.0):
        self.hr  = hr
        self.min = min
        self.sec = sec

    def getSeconds(self):
        return ((self.hr * 60.0 * 60.0) + (self.min * 60.0) + self.sec) * 15.0

    # define subtracttion
    def __sub__ (self, y):
        xSeconds = self.getSeconds()
        ySeconds = y.getSeconds()
        return xSeconds - ySeconds

# The class CovertAlt handles conversions to sectonds.
# The methods defined in the class are:
# __init__
# getSeconds

class ConvertAlt:
    def __init__ (self, deg = 0.0):
        self.deg = deg
    def getSeconds(self):
        return (float(self.deg) * 60.0 * 60.0)
    
# The class CovertAzi handles conversions to sectonds.
# The methods defined in the class are:
# __init__
# getSeconds

class ConvertAzi:
    def __init__ (self, deg = 0.0):
        self.deg = deg

    def getSeconds(self):
        return (float(self.deg) * 60.0 * 60.0)

# As of 2024-12-20 this code is running on a windows 11 (PC-03) machine.

if __name__ == '__main__':
    
    # Is there a better way to initialize the ra and dec values?
    
    #hr   = input ('raHr   : ')
    #min  = input ('raMin  : ')
    #sec  = input ('raSec  : ')

    #ra = ConvertRa(hr, min, sec)

    ra  = ConvertRa  ('18', '45', '41') # seconds were 40.8
    dec = ConvertDec ('41', '15', '58')
    
    print ('RA   hr min sec      : ', ra.hr,   ' ', ra.min,  ' ', ra.sec)
    print ('Dec deg min sec      : ', dec.deg, ' ', dec.min, ' ', dec.sec)
    
    try:
        raCgemUnits  = ra.oldToCgem()
        print ('raCgemUnits    : ', raCgemUnits)
        print ('RA  fromCgem   : ', ra.fromCgem())
    except:
        print ('ra.oldToCgem failed')

    try:
        decCgemUnits = dec.toCgem()
        print ('decCgemUnits   : ', decCgemUnits)
        print ('Dec fromCgem   : ', dec.fromCgem(decCgemUnits))
    except:
        print ('dec.toCgem failed')

    
    print ('Doing a translation to RA/Dec from numbers from telescope')
    
    cgemRa  = 'C78DC600'
    cgemDec = '1C6B1D00'
    
    print ('cgemRa, cgemDec: ', cgemRa, cgemDec)

    print ('RA : ', ra.fromCgem())
    print ('Dec: ', dec.fromCgem(cgemDec))

    print ()
    print ()
    
    cgemRa  = 'C81F1900'
    cgemDec = '1D584400'
    
    print ('cgemRa, cgemDec: ', cgemRa, cgemDec)

    print ('RA : ', ra.fromCgem())
    print ('Dec: ', dec.fromCgem(cgemDec))

#    print ('RA   hr min sec: ', CovertRa.fromCgem(cgemRa))
#    print ('Dec deg min sec: ', Dec.fromCgem(cgemDec))

    ra  = ConvertRa  ('03', '20', '00')
    dec = ConvertDec ('00', '00', '00')
    
    print ('RA   hr min sec      : ', ra.hr,   ' ', ra.min,  ' ', ra.sec)
    print ('Dec deg min sec      : ', dec.deg, ' ', dec.min, ' ', dec.sec)
    
    try:
        raCgemUnits  = ra.oldToCgem()
        print ('raCgemUnits    : ', raCgemUnits)
        print ('RA  fromCgem   : ', ra.fromCgem())
    except:
        print ('ra.oldToCgem failed')

    try:
        decCgemUnits = dec.toCgem()
        print ('decCgemUnits   : ', decCgemUnits)
        print ('Dec fromCgem   : ', dec.fromCgem(decCgemUnits))
    except:
        print ('dec.toCgem failed')

    print ()
    print ()
    
    ra  = ConvertRa  ('03', '20', '00')
    dec = ConvertDec ('45', '00', '00')
    
    print ('RA   hr min sec      : ', ra.hr,   ' ', ra.min,  ' ', ra.sec)
    print ('Dec deg min sec      : ', dec.deg, ' ', dec.min, ' ', dec.sec)

    try:
        raCgemUnits  = ra.oldToCgem()
        print ('raCgemUnits    : ', raCgemUnits)
        print ('RA  fromCgem   : ', ra.fromCgem())
    except:
        print ('ra.oldToCgem failed')

    try:
        decCgemUnits = dec.toCgem()
        print ('decCgemUnits   : ', decCgemUnits)
        print ('Dec fromCgem   : ', dec.fromCgem(decCgemUnits))
    except:
        print ('dec.toCgem failed')

    print ()
    print ()
    
    ra  = ConvertRa  ('06', '00', '00')
    dec = ConvertDec ('00', '00', '00')
    
    print ('RA   hr min sec      : ', ra.hr,   ' ', ra.min,  ' ', ra.sec)
    print ('Dec deg min sec      : ', dec.deg, ' ', dec.min, ' ', dec.sec)

    try:
        raCgemUnits  = ra.oldToCgem()
        print ('raCgemUnits    : ', raCgemUnits)
        print ('RA  fromCgem   : ', ra.fromCgem())
    except:
        print ('ra.oldToCgem failed')

    try:
        decCgemUnits = dec.toCgem()
        print ('decCgemUnits   : ', decCgemUnits)
        print ('Dec fromCgem   : ', dec.fromCgem(decCgemUnits))
    except:
        print ('dec.toCgem failed')

    print ()
    print ()
    
    ra  = ConvertRa  ('09', '00', '00')
    dec = ConvertDec ('00', '00', '00')
    
    print ('RA   hr min sec      : ', ra.hr,   ' ', ra.min,  ' ', ra.sec)
    print ('Dec deg min sec      : ', dec.deg, ' ', dec.min, ' ', dec.sec)

    try:
        raCgemUnits  = ra.oldToCgem()
        print ('raCgemUnits    : ', raCgemUnits)
        print ('RA  fromCgem   : ', ra.fromCgem())
    except:
        print ('ra.oldToCgem failed')

    try:
        decCgemUnits = dec.toCgem()
        print ('decCgemUnits   : ', decCgemUnits)
        print ('Dec fromCgem   : ', dec.fromCgem(decCgemUnits))
    except:
        print ('dec.toCgem failed')

    print ()
    print ()
    
    cgemRa  = '238E7C00'
    cgemDec = '00033900'
    
    print ('cgemRa, cgemDec: ', cgemRa, cgemDec)

    print ('RA : ', ra.fromCgem())
    print ('Dec: ', dec.fromCgem(cgemDec))

    print ()
    print ()

    cgemRa  = '238F5B00'
    cgemDec = '20012000'
    
    print ('cgemRa, cgemDec: ', cgemRa, cgemDec)

    print ('RA : ', ra.fromCgem())
    print ('Dec: ', dec.fromCgem(cgemDec))

    print ()
    print ()

    cgemRa  = '5553B000'
    cgemDec = 'F8E12600'
    
    print ('cgemRa, cgemDec: ', cgemRa, cgemDec)

    print ('RA : ', ra.fromCgem())
    print ('Dec: ', dec.fromCgem(cgemDec))

    print ()
    print ()

    ra  = ConvertRa  ('08', '00', '00')
    dec = ConvertDec ('10', '00', '00')
    
    print ('RA   hr min sec      : ', ra.hr,   ' ', ra.min,  ' ', ra.sec)
    print ('Dec deg min sec      : ', dec.deg, ' ', dec.min, ' ', dec.sec)

    try:
        raCgemUnits  = ra.oldToCgem()
        print ('raCgemUnits    : ', raCgemUnits)
        print ('RA  fromCgem   : ', ra.fromCgem())
    except:
        print ('ra.oldToCgem failed')

    try:
        decCgemUnits = dec.toCgem()
        print ('decCgemUnits   : ', decCgemUnits)
        print ('Dec fromCgem   : ', dec.fromCgem(decCgemUnits))
    except:
        print ('dec.toCgem failed')

    print ()
    print ()

    ra.setHex('C7582100')
    raFromCgem  = ra.fromCgem()
    print ('raFromCgem: ', raFromCgem)

    decHex      = b'1C761C00'
    decFromCgem = dec.fromCgem(decHex)
    print ('decFromCgem: ', decFromCgem)


