import winsound
from time import strftime

hours = 0
minutes = 0
period = ''

def checktime():
    global hours
    global minutes
    global period
    if hours == int(strftime('%I')) and minutes == int(strftime('%M')) and period == strftime('%p'):
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)

def checktime2(hrs, mins, ampm):
    global hours
    global minutes
    global period
    hours = hrs
    minutes = mins
    period = ampm
