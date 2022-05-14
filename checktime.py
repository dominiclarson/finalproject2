import winsound
from time import strftime

hours = 0
minutes = 0
period = ''

def checktime():
    """
    Method used to check the system time against the set alarm time.
    :param hours: Time in hours.
    :param minutes: Time in minutes.
    :param period: Time period in AM or PM.
    """
    global hours
    global minutes
    global period
    if hours == int(strftime('%I')) and minutes == int(strftime('%M')) and period == strftime('%p'):
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)

def checktime2(hrs, mins, ampm):
    """
    Method used to initialize variables as global.
    """
    global hours
    global minutes
    global period
    hours = hrs
    minutes = mins
    period = ampm
