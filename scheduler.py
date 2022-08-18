# This script downloads the files on a scheduled basis 
# Author: Thomas H2
# References are in line the script file

#Modules imported for scheduling tasks

from apscheduler.schedulers.blocking import BlockingScheduler 
from datetime import datetime as dt

# Modules imported for ftp connection

import ftplib as ftp

#function will start the scheduling at a given date

def schedule_event(given_time, is_e_day):
    scheduler = BlockingScheduler()
    scheduler.start()
    # determines if there is already another job

    # starts the jobs
    present = dt.now()
    if given_time <= present and is_e_day:
        scheduler.add_job(ftp_job, trigger='cron', hour='0', day_of_week='*', id='ftp_job')
        return True
    elif given_time <= present and not is_e_day:
        scheduler.add_job(ftp_job, trigger='cron', hour=str(given_time.hour), day=str(given_time.day), year=str(given_time.year))


def ftp_job():
    # get the current date-time

    current_date = dt.now()

    # logging in using anonymous creds

    ftp_conn = ftp.FTP('ip_address')

    ftp_conn.login()
    
    ftp.dir()

    return True
