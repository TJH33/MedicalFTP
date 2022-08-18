# This is the python script that will look after the main GUI, alongside the validation of CSV files as they are downloaded
# Author: Thomas H2

# Libraries 

from tkinter import *
from tkinter.ttk import *
from tkcalendar import Calendar
from datetime import datetime as dt
import scheduler as sc
import ftplib as ftp


# this rolls the main window over the screen

window = Tk()

def main():
    # sets the main settings for the window

    window.geometry('600x400')
    window.resizable(False, False)
    window.title("Medical FTP Server")

     
    # Create Label and add some text

    intro_label = Label(window,text ='This application comes with two modes, 1. Which allows you to download the CSVs for any given day and \n 2. Which allows you to schedule the downloading of data.')
    intro_label.place(relx= 0.0, rely=0.0, anchor='nw')


    # Add Calendar

    cal = Calendar(window, selectmode = 'day',
               year = dt.now().year, month = dt.now().month,
               day = dt.now().day)
    
    cal.pack(pady=40)

    # styling and organising buttons

    btn_schedule_eday = Button(window, text='Schedule Every Day', command=lambda: schedule_event(given_date=cal.selection_get(), every_day_switch=True)).pack(anchor='s')
    btn_schedule = Button(window, text='Schedule at Calendar Date', command=lambda: schedule_event(given_date=cal.selection_get(), every_day_switch=False))
    btn_CSV = Button(window, text='Get CSV Data For Calendar Date', command=lambda: download_data(given_date=cal.selection_get()))
    btn_schedule.pack(side=LEFT, anchor='se')
    btn_CSV.pack(side=RIGHT, anchor='sw')


    window.mainloop()

# procedure which goes to perform the schedling task

def schedule_event(given_date, every_day_switch):
    if every_day_switch:
        sc.schedule_event(given_time=given_date, every_day_switch=True)
    else:
        sc.schedule_event(given_time=given_date, every_day_switch=False)

def download_data(given_date):
    # getting files from ftp

    files = None

    # logging in using anonymous creds

    ftp_conn = ftp.FTP('ip_address')

    ftp_conn.login()
    
    ftp.dir()


if __name__ == '__main__':
    main()