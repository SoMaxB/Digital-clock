from tkinter import *
from tkinter.font import Font
import time

# Functions

# Function to close the window
def quitwin(event):
    root.destroy()
    quit()

# Create a function that will return current time in nice format
def timeformat():
    ctime = time.localtime(time.time()) #Get the current time data
    hour = ctime.tm_hour   #Get the hour data
    minute = ctime.tm_min  #Get the minute data
    second = ctime.tm_sec  #Get the second data

    # These two part let the number always in two digits
    if minute < 10:
        minute = '0'+str(minute)
    if second < 10:
        second = '0'+str(second)

    return str(hour) + ':' + str(minute) + ':' + str(second) #Return the time with the format 88:88:88

#Make the weekday, day, month and year formatting function
def dateformat():
    ctime = time.localtime(time.time())
    year = ctime.tm_year
    month = ctime.tm_mon
    day = ctime.tm_mday
    weekday = ctime.tm_wday

    wdaylist = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    mlist = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#When we call the month list we need to be careful. The month list index starts with 0 but the month module starts with 1. So we need to substract the index by 1 when calling the list element.
    return wdaylist[weekday] + ' ' + str(day) + ' ' + mlist[month-1] + ' ' + str(year)



#Create window
root = Tk()
root.wm_attributes('-transparentcolor', 'white') #Make the window transparent
root.geometry('550x230+500+500') #Set size of the window
root.configure(bg='white') #Set the window color to white
root.overrideredirect(True) #This line of code will get rid of the window border, now we need to bind a key to close the window (window.bind(key,function).

timefont = Font(size=100, family='Bahnschrift SemiBold')
datefont = Font(size=30, family='Bahnschrift SemiBold')

#Create a label that show up the hour, minute and second, don't create de fg (Foreground) white (FFFFFF), we set the white as transparent!
timeshow = Label(root, text=timeformat(), font=timefont, bg='white', fg='#FFFFFE')
dateshow = Label(root, text=dateformat(), font=datefont, bg='white', fg='#FFFFFE')
timeshow.pack()
dateshow.pack()

root.bind('<F12>', quitwin) #Bind a key to close the window (window.bind(key,function).

#Add while loop to refresh time always
while True:
    timeshow.config(text=timeformat())
    timeshow.update()
    dateshow.config(text=dateformat())
    dateshow.update()
