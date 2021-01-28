import time
import os

while True:
    os.system("fswebcam -r 1280x720 -S 60 --jpeg 50 --banner-colour '#FF000000' --line-colour '#FF000000' --timestamp '%Y-%m-%d %H:%M:%S' --font 'sans:32'--save `date +%Y%m%d-%H%M%S`.jpg")
    #os.system("fswebcam -c HW14_fswebcam.conf")
    time.sleep(5)
