
import board
import time
import busio
from time import sleep

# https://learn.adafruit.com/circuitpython-essentials/circuitpython-uart-serial
# https://wiki.dfrobot.com/DFPlayer_PRO_SKU_DFR0768#target_5


class DFPlayerPro(object):

    MUSIC = 1

    # set play modes
    PLAY_MODE_REPEAT_ONE = 1
    PLAY_MODE_REPEAT_ALL = 2
    PLAY_MODE_ONE_SONG_PAUSE = 3
    PLAY_MODE_RANDOMLY = 4
    PLAY_MODE_REPEAT_ALL_IN_FOLDER = 5

    # queries
    QUERY_FILE_NUMBER_CURRENTLY_PLAYING = 1
    QUERY_TOTAL_NUMBER_OF_FILES = 2
    QUERY_TIME_SONG_HAS_PLAYED = 3
    QUERY_TOTAL_TIME_CURRENT_FILE = 4
    QUERY_FILENAME_CURRENT_FILE = 5

    def __init__(self, baudrate=115200, latency=0.100, uart=None):
        if uart is None:
            self._uart = busio.UART(board.TX, board.RX, baudrate=115200)
        else:
            self._uart = uart

        self._latency = latency
        self.pauseFlag = 0
        sleep(1)

    def begin(self):
        cmd = self.pack()
        return self.writeATCommand(cmd)

    def playFileByName(self, name):
        cmd = self.pack("PLAYFILE", name)
        self.writeATCommand(cmd)

    def getTotalTime(self):
        cmd = self.pack("QUERY", "4")
        if ( self.writeATCommand(cmd) ) :        
            str = self.readAck(6)
            if (str != None):
                return str
            else:
                return 0
        else:
            return 0

    def getPlayingFileName(self):
        cmd = self.pack("QUERY", "5")
        if (self.writeATCommand(cmd)):
            str = self.readAck(6)
            if (str != None):
                return str
            else:
                return 0
        else:
            return 0

    def switchFunction(self, function):
        cmd = self.pack("FUNCTION", str(function))
        self.curFunction = function
        self.writeATCommand(cmd)
        self.pauseFlag = 0

    def setPlayMode(self, mode):
        cmd = self.pack("PLAYMODE", str(mode))
        self.writeATCommand(cmd)

    def start(self):
        cmd = self.pack("PLAY", "PP")
        if (self.pauseFlag == 1):
            return False
        self.pauseFlag = 1
        self.writeATCommand(cmd)

    def pause(self):
        cmd = self.pack("PLAY", "PP")
        if (self.pauseFlag == 0):
            return False
        self.pauseFlag = 0
        self.writeATCommand(cmd)

    def setPrompt(self, on):
        if(on == True):
            mode = "ON"
        else:
            mode = "OFF"
        cmd = self.pack("PROMPT", mode)
        self.writeATCommand(cmd)

    def setVolume(self, value):
        cmd = self.pack("VOL", str(value))
        self.writeATCommand(cmd)

    def playFileNum(self, num):
        cmd = self.pack("PLAYNUM", str(num))
        self.writeATCommand(cmd)

    def pack(self, cmd=" ", para=" "):
        atCmd = "AT"
        if (cmd != " "):
            atCmd += "+"
            atCmd += cmd

        if(para != " "):
            atCmd += "="
            atCmd += para

        atCmd += "\r\n"
        return atCmd

    def writeATCommand(self, cmd):
        data = []
        data = bytearray(cmd)
        # self._uart.write(bytes([cmd]))
        result = self._uart.write(data)
        if ( result != None ) :
            return True
        else :
            return False

    def readAck(self, len=0):
        if self._uart.in_waiting:
            buf = self._uart.read()
            if buf is not None:
                data_string = ''.join([chr(b) for b in buf])
                return data_string
        return None
