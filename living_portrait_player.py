#!/usr/bin/env python3
#Created by scarethetots
from gpiozero import MotionSensor
import sys
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

files = sys.argv[1]
slength = '1440'
swidth = '900'
print("Starting up....")
tgr = 0
try:
    VIDEO_PATH = Path(files)
    player = OMXPlayer(VIDEO_PATH,  args=['--no-osd', '--loop', '--win', '0 0 {0} {1}'.format(slength, swidth)])
    pir = MotionSensor(4)
    sleep(1)
    print("Ready to trigger")
    while True:
        player.pause()
        if pir.motion_detected:
            print("trigger count {}".format(tgr))
            player.play()
            sleep(player.duration())
            tgr = tgr + 1
        else:
            pass
        player.set_position(0.0)


except KeyboardInterrupt:
    player.quit()
    sys.exit()
