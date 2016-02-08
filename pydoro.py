import time
import os
import datetime
import configparser

config = configparser.ConfigParser()
config.read('pydoro.ini')

soundpath = config["SETTINGS"]["soundpath"]
segments = int(config["SETTINGS"]["segments"])
breaklength = int(config["SETTINGS"]["breaklength"])
setbreaklength = int(config["SETTINGS"]["setbreaklength"])
worklength = int(config["SETTINGS"]["worklength"])


def runSegment(minutes, displayTime):
    time.sleep(minutes*60)
    os.system("aplay " + soundpath + " -q")
    if(displayTime):
        printTime();

def printTime():
    now = time.asctime( time.localtime(time.time()) )
    print(now);

for x in range(1, segments + 1):
    runSegment(worklength, True)
    if x == segments:
        runSegment(setbreaklength, True)
    else:
        runSegment(breaklength, True)
