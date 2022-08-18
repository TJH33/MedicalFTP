# This is the python script that will look after the main GUI, alongside the validation of CSV files as they are downloaded
# Author: Thomas H2

# Libraries 

# for GUI

from tkinter import *
from tkinter.ttk import *
from tkcalendar import Calendar
from tkinter.messagebox import showerror, showwarning, showinfo

#for date-time manipulation

from datetime import datetime as dt

#for ftp connection and validation

import scheduler as sc
import ftplib as ftp
import file_name_validator as fnv
import csv_validator as cv
import directory_logic as dl
import os
import re

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

    #getting files from ftp

    current_date_str = given_date.strftime("%Y%m%d")
    print(current_date_str)

    # logging in using creds
    ftp_conn = ftp.FTP()
    try:

        ftp_conn.connect('192.168.0.21', 2121)
        ftp_conn.login(user='padmin', passwd='Summertime2022!')
    except:
        showinfo("FTP Connection Falied")

    # get all the .csv files in list format

    filename_list = ftp_conn.nlst()
    filename_rel = []
    filename_valid = []
    pwd = os.path.dirname(__file__)
        
    # getting all valid named CSV Files
        
    for file_name in filename_list:
        if fnv.is_valid_filename(file_name) and re.search(current_date_str, file_name):
                with open(file_name, 'wb' ) as file :
                    filename_rel.append(file_name)
                    ftp_conn.retrbinary('RETR %s' % file_name, file.write)
                    file.close()
    
    dl.move_to_temp(filename_rel)
    
    #performing the validation tests on the files

    for filename in filename_rel:
        if cv.validate_csv(os.path.join(pwd, 'Temp', filename) == []):
            filename_valid.append(filename)
    
    # moving to valid

    dl.move_to_valid(filename_valid)


    #close the connection

    ftp_conn.quit()



if __name__ == '__main__':
    main()
