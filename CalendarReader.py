#!/usr/bin/env python

from Tkinter import *

from CalendarFunctions import *
from SoundFunctions import *
from DriveFunctions import *

from datetime import datetime,timedelta
from random import choice

class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
        self.tk.attributes('-fullscreen', True)
        self.frame = Frame(self.tk)
        self.frame.pack()

        self.message = Label(self.tk,text='Agenda do Samuel\nIniciando...',bg='grey',font=('Helvetica', 42, 'bold'))
        self.message.pack(expand=True,fill=BOTH)
        self.clearedEtag = ''
        self.currentEtag = ''
        
        
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.exit_fullscreen)
        self.tk.bind("<Button-1>", self.clean_fullscreen)

        self.tk.after(2000, self.update_fullscreen)

    def update_fullscreen(self, event=None):
        
        nextEvent = getNextTask()
        # print nextEvent
        
        # Nothing in the future, lets just clear everything
        if nextEvent is None:
            self.clean_fullscreen()
            self.tk.after(2000, self.update_fullscreen)
            return

        dtStart = nextEvent['start']['dateTime']
        nextEventStart = datetime.strptime(dtStart[:-6],'%Y-%m-%dT%H:%M:%S')
        deltaStart = (nextEventStart - datetime.now()).total_seconds()

        dtEnd = nextEvent['end']['dateTime']
        nextEventEnd = datetime.strptime(dtEnd[:-6],'%Y-%m-%dT%H:%M:%S')
        deltaEnd = (nextEventEnd - datetime.now()).total_seconds()

        # Something new started
        if deltaStart < 0 and deltaEnd > 2 and nextEvent['etag'] != self.clearedEtag:
            if deltaStart > -10:
                try:
                    soundFile = nextEvent['description']
                    if GetFileFromDrive(soundFile) is not None:
                        PlayBeep(soundFile)
                except:
                    pass
            self.currentEtag = nextEvent['etag']
            colorPallete = ['blue','blue violet','medium sea green','purple','coral','orange','OrangeRed2','dodger blue','gray20','navy','dark green','red3']
            colorName = choice(colorPallete)
            try:
                colorId = nextEvent['colorId']
                # print colorId
                colorName=colorPallete[int(colorId)]
                #print colorName
            except:
                pass
            self.message.config(text='{0}\n\n{1}'.format(nextEvent['summary'],nextEventStart.strftime('%H:%M')),bg=colorName,fg='white')        
            self.message.pack(expand=True,fill=BOTH)
            self.tk.after(2000, self.update_fullscreen)
            return
        elif deltaEnd <=2:
            self.clean_fullscreen()
            self.tk.after(2000, self.update_fullscreen)
            return
            
        # Just wait with whatever you have
        self.tk.after(2000, self.update_fullscreen)
               
    def clean_fullscreen(self, event=None):

        self.clearedEtag = self.currentEtag
        self.message.config(text='Agenda do Samuel',bg='gray',fg='black',anchor=choice(['n','ne','e','se','s','sw','w','nw','center']))        
        self.message.pack(expand=True,fill=BOTH)
        
        
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

    def exit_fullscreen(self, event=None):
        self.tk.destroy()

if __name__ == '__main__':
    w = Fullscreen_Window()
    w.tk.focus_force()
    w.tk.mainloop()
