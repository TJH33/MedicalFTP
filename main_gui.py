# This is the python script that will look after the main GUI, alongside the validation of CSV files as they are downloaded
# Author: Thomas H2


from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime as dt

# this rolls the main window over the screen

window = Tk()

def main():
    # sets the main settings for the window

    window.geometry('600x400')
    window.resizable(False, False)
    window.title("Medical FTP Server")

     
    # Create Label and add some text

    Lower_left = ttk.Label(window,text ='This application comes with two modes, 1. Which allows you to download the CSVs for any given day and \n 2. Which allows you to schedule the downloading of data.')
    Lower_left.place(relx= 0.0, rely=0.0, anchor='nw')

    # sets calendar and time gui

    hour_string = StringVar()
    min_string = StringVar()
    last_value_sec = ''
    last_value = ''

    fone = Frame(window)
    ftwo = Frame(window)

    # Add Calendar

    cal = Calendar(fone, selectmode = 'day',
               year = dt.now().year, month = dt.now().month,
               day = dt.now().day)

    
    # reference = https://pythonguides.com/create-date-time-picker-using-python-tkinter/


    # spinboxes which look after the hours, minutes, seconds counter
    
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

    fone.pack(padx=40, pady=40)
    ftwo.pack(padx=20, pady=20)



    window.mainloop()

if __name__ == '__main__':
    main()
