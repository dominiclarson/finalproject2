from tkinter import *
from time import strftime
from time import sleep
import checktime

class GUI:
    def __init__(self, window):
        self.window = window
        
        self.dclock = Label(window, font = ('Arial', 50), background = 'black', foreground = '#0080ff')
        self.dclock.grid(column=0,row=0)
        
        self.hrs = StringVar(self.window, '')
        self.mins = StringVar(self.window, '')
        self.frame_hrs = Frame(self.window)
        self.label_hrs = Label(self.frame_hrs, text='Alarm time: ')
        self.entry_hrs = Entry(self.frame_hrs, textvariable=self.hrs, width=3)
        self.label_hrs.grid(column=1,row=0)
        self.entry_hrs.grid(column=2,row=0)
        self.frame_hrs.grid(column=2,row=0)
        
        self.frame_mins = Frame(self.window)
        self.label_mins = Label(self.frame_mins, text=':')
        self.entry_mins = Entry(self.frame_mins, textvariable=self.mins, width=3)
        self.label_mins.grid(column=3,row=0)
        self.entry_mins.grid(column=4,row=0)
        self.frame_mins.grid(column=4,row=0)
        
        self.ampm = StringVar(self.window, 'AM')
        self.menu = OptionMenu(self.window, self.ampm, "AM", "PM")
        self.menu.grid(column=5,row=0)
        
        self.setbutton = Button(self.window, text='SET', command=self.setalarm)
        self.setbutton.grid(column=6,row=0)
        
        
        self.time()
        
    def time(self):
        string = strftime('%I:%M:%S %p')
        self.dclock.config(text = string)
        self.dclock.after(1000, self.time)
        self.dclock.after(1000, checktime.checktime)
    def setalarm(self):
        if self.entry_mins.get() != '' and self.entry_hrs.get() != '':
            try:
                if 1 <= int(self.entry_hrs.get()) <= 12 and 0 <= int(self.entry_mins.get()) <= 59:
                    self.label_hrs.config(text='Alarm set!:')
                    alarm_hrs = int(self.entry_hrs.get())
                    alarm_mins = int(self.entry_mins.get())
                    alarm_ampm = self.ampm.get()
                    checktime.checktime2(alarm_hrs, alarm_mins, alarm_ampm)
                else:
                    self.label_hrs.config(text='Alarm (Error):')
            except Exception as e:
                self.label_hrs.config(text='Alarm (Error):')
                print(e)