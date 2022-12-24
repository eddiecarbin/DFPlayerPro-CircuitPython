from DFPlayerPro import DFPlayerPro
import board
from time import sleep


print("DFPlayer Pro Test")

player = DFPlayerPro(baudrate=115200)
v = player.begin()
print(v)

sleep(0.5)
# player.switchFunction(DFPlayerPro.MUSIC)
player.setPlayMode(DFPlayerPro.PLAY_MODE_ONE_SONG_PAUSE)

sleep(2.5)
print("looking")
# player.start()
# player.playFileByName("/voices/005sounds.mp3")
# sleep(0.5)
# t = player.getTotalTime()
# print(t)
# sleep(6)

# player.pause()
while True:
    # player.playFileNum(20)
    # t = player.getPlayingFileName()
    # print(t)
    # sleep(3)
    # player.playFileByName("/005sound.wav")
    # sleep(6)
    # player.playFileByName("/008sound.wav")
    # sleep(6)
    # player.playFileByName("/020sound.wav")
    # sleep(6)
    # t = player.getTotalTime()
    # print(t)
    sleep(3)
    # player.playFileByName("/voices/015sounds.mp3")
