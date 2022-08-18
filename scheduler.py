# This script downloads the files on a scheduled basis 
# Author: Thomas H2
# References are in line the script file

#Modules imported for scheduling tasks

from apscheduler.schedulers.blocking import BlockingScheduler 
from datetime import datetime as dt


# Modules imported for ftp connection

import ftplib as ftp

# Modules imported for validation

import file_name_validator as fnv
import csv_validator as cv
import directory_logic as dl
import os
import re

#function will start the scheduling at a given date

def schedule_event(given_time, is_e_day):
    scheduler = BlockingScheduler()
    scheduler.start()
    # determines if there is already another job

    # starts the jobs

    present = dt.now()
    if given_time <= present and is_e_day:
        scheduler.add_job(lambda: ftp_job(is_e_day), trigger='cron', hour='0', day_of_week='*', id='ftp_job')
        return True
    elif given_time <= present and not is_e_day:
        scheduler.add_job(lambda: ftp_job(is_e_day), trigger='cron', hour=str(given_time.hour), day=str(given_time.day), year=str(given_time.year))
        return True


def ftp_job(is_e_day):
    # getting files from ftp
    
    if is_e_day:
        fetch_date = dt.now() - 1
    else:
        fetch_date = dt.now()

    current_date_str = f"^MED_DATA_" + fetch_date.strftime("%Y%m%d")

    # logging in using creds

    ftp_conn = ftp.FTP()
    ftp_conn.connect('192.168.0.21', 2121)
    ftp_conn.login(user='padmin', passwd='Summertime2022!')

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
                    ftp.retrbinary('RETR %s' % file_name, file.write)
                    file.close()
    
    dl.move_to_temp(filename_rel)
    
    #performing the validation tests on the files

    for filename in filename_rel:
        if cv.validate_csv(os.path.join(pwd, 'Temp', filename) == []):
            filename_valid.append(filename)
    
    # moving to valid

    dl.move_to_valid(filename_valid)


    #close the connection

    ftp_conn.close()
    ftp_conn.quit()
