#!/usr/bin/python3
import time
import os
import datetime
import configparser

config = configparser.ConfigParser()
homePath = os.path.dirname(os.path.realpath(__file__))+'/'
config.read(homePath + 'pydoro.ini')

soundpath = homePath + config["SETTINGS"]["soundpath"]
segments = int(config["SETTINGS"]["segments"])
breaklength = int(config["SETTINGS"]["breaklength"])
setbreaklength = int(config["SETTINGS"]["setbreaklength"])
worklength = int(config["SETTINGS"]["worklength"])


def runSegment(minutes, displayTime, isBreak):
    message = ''
    if(displayTime):
        printTime()
    if(isBreak):
        message += ' Break, '
    else:
        message += ' Work, '
    message += str(minutes) + ' minutes'
    print(message)
    time.sleep(minutes*60)
    os.system("aplay " + soundpath + " -q")

def printTime():
    now = time.asctime( time.localtime(time.time()) )
    print(now)

for x in range(1, segments + 1):
    runSegment(worklength, True, False)
    if x == segments:
        runSegment(setbreaklength, True, True)
    else:
        runSegment(breaklength, True, True)
