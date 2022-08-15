# This script downloads the files on a scheduled basis 
# Author: Thomas H2
# References are in line the script file


#Modules imported for GUI 

from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar

#Modules imported for scheduling tasks

from apscheduler.schedulers.background import BackgroundScheduler 
from datetime import datetime as dt

# Modules imported for ftp connection

import ftplib as ftp

#sets the window's properties

window = Tk()

def main():

    # strings for spinbox

    hour_string = StringVar()
    min_string = StringVar()
    last_value_sec = ''
    last_value = ''

    # window geometry

    window.geometry('600x400')
    window.resizable(False, False)
    window.title("Scheduler")

    fone = Frame(window)
    ftwo = Frame(window)

    # Add Calendar

    cal = Calendar(fone, selectmode = 'day',
               year = dt.now().year, month = dt.now().month,
               day = dt.now().day)

    # in order to be feature complete -> A seconds counter needs to be added
    #reference = https://pythonguides.com/create-date-time-picker-using-python-tkinter/
    
    min_sb = Spinbox(
        ftwo,
        from_=0,
        to=23,
        wrap=True,
        textvariable=hour_string,
        width=2,
        state="readonly",
        justify=CENTER
    )

    hour_sb = Spinbox(
        ftwo,
        from_= 0,
        to = 59,
        wrap=True,
        textvariable=min_string,
        width=2,
        justify=CENTER
    )

    sec_sb = Spinbox(
       ftwo,
       from_ = 0,
       to=59,
       wrap=True,
       textvariable=hour_sb,
       width=2,
       justify=CENTER
    )

    sec = Spinbox(
        ftwo,
        from_= 0,
        to=59,
        wrap=True,
        textvariable=sec_sb,
        width=2,
        justify=CENTER
    )

    cal.pack(pady = 20)
    min_sb.pack(side=LEFT, fill=X, expand=True)
    hour_sb.pack(side=LEFT, fill=X, expand=True)
    sec_sb.pack(side=LEFT, fill=X, expand=True)
    sec.pack(side=LEFT, fill=X, expand=True)

    fone.pack()
    ftwo.pack()

    window.mainloop()

#function will start the scheduling at a given date

def schedule_event(given_time):
    present = dt.now()
    if given_time <= present:
        scheduler = BackgroundScheduler()
        scheduler.add_job(ftp_job, 'cron', day_of_week=given_time.weekday())
    else:
        return False


def ftp_job():
    # get the current date-time

    current_date = dt.now()




    # logging in using anonymous creds

    ftp_conn = ftp.FTP('ip_address')
    ftp_conn.login()






if __name__ == '__main__':
    main()
